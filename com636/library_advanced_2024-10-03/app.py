from flask import Flask
from flask import render_template
from flask import request
from flask import redirect
from flask import url_for
import re
from datetime import datetime
import mysql.connector
from mysql.connector import FieldType
import connect

app = Flask(__name__)

dbconn = None
connection = None

def getCursor():
    global dbconn
    global connection
    connection = mysql.connector.connect(user=connect.dbuser, \
    password=connect.dbpass, host=connect.dbhost, \
    database=connect.dbname, autocommit=True)
    dbconn = connection.cursor()
    return dbconn

@app.route("/")
def home():
    cursor = getCursor()
    # Show the top 3 books by number of loans
    qstr = """select bc.bookid, min(b.image) as image, count(*) as bookcount
                from books b
                inner join bookcopies bc on b.bookid = bc.bookid
                inner join loans l on bc.bookcopyid = l.bookcopyid
                group by bc.bookid
                order by count(*) desc
                limit 3;"""
    cursor.execute(qstr)
    top3 = cursor.fetchall()
    return render_template("home.html", top3=top3)

@app.route("/listbooks", methods=['GET'])
def listbooks():
    cursor = getCursor()
    # Shows the loan form above the book list if /listbooks?loan has a value using GET method
    loan_value = request.args.get('loan')   # Returns the value of 'loan' from GET method
    show_loan = loan_value is not None     # Returns True if loan has a value, else False
    if show_loan:
        # List of borrowers for loan dropdown
        qstr = "SELECT * FROM borrowers;"
        cursor.execute(qstr)
        borrower_list = cursor.fetchall()
        # List of book copies for loan dropdown
        qstr = """SELECT * FROM bookcopies 
                    INNER JOIN books on books.bookid = bookcopies.bookid 
                    WHERE bookcopyid not in (SELECT bookcopyid FROM loans WHERE returned <> 1 or returned is NULL);"""
        cursor.execute(qstr)
        book_copies = cursor.fetchall()
    else:
        borrower_list = []      # Need a value so not undefined... 
        book_copies = []        #    in render_template()
    # Pass current date for loan date
    todaydate = datetime.now().date()  # Also needs a value, so alway pass the value
    
    # Pass an error flag to page if ?loan=error from GET method
    loan_error = (loan_value == 'error')    # loan_error set to True if loan_value equals 'error', False otherwise

    # List of book titles
    qstr = "SELECT bookid, booktitle, author, category, yearofpublication FROM books;"
    cursor.execute(qstr)
    book_list = cursor.fetchall()
    #print(book_list)
    return render_template("booklist.html", show_loan=show_loan, loan_error=loan_error, loandate=todaydate, 
                borrowers=borrower_list, book_copies=book_copies, book_list=book_list)    


@app.route("/bookdetails", methods=["GET"])
def bookdetails():
    bookid = request.args.get('bookid')
    cursor = getCursor()
    qstr = "SELECT * FROM books WHERE bookid = %s;"
    qargs = (bookid,)   # Remember to use a final comma to indicate this is a tuple with only one item
    cursor.execute(qstr,qargs)
    book_details = cursor.fetchone()
    #print(bookDetails)
    return render_template("bookdetails.html", book_details = book_details)    


# Second loan page
@app.route("/loan", methods=['GET','POST'])
def loan():
    borrower_id = request.form.get('borrower')
    book_id = request.form.get('book')
    book_copy_id = request.form.get('book_copy')
    loan_date = request.form.get('loandate')

    # If there is a borrower_id and a book_copy_id then there is enough info to borrow the book
    #   i.e., add a record in the loans table.
    if borrower_id!=None and book_copy_id!=None:
        cursor = getCursor()
        # Good to add an error handler here (try/except) in case INSERT fails.
        qstr = "INSERT INTO loans (borrowerid, bookcopyid, loandate, returned) VALUES(%s,%s,%s,0);"
        qargs = (borrower_id, book_copy_id, str(loan_date))
        cursor.execute(qstr,qargs)
        return redirect(url_for('loansbyborrower'))
    else:
        cursor = getCursor()
        # Shows the loan form above the book list if /listbooks?loan has a value using GET method
        # List of borrowers for loan dropdown
        qstr = "SELECT * FROM borrowers;"
        cursor.execute(qstr)
        borrowers = cursor.fetchall()

        # List of books for loan dropdown - only shows books that have a copy available.
        cursor = getCursor()
        qstr = """SELECT DISTINCT b.bookid, b.booktitle, b.author
                    FROM bookcopies bc
                    INNER JOIN books b on b.bookid = bc.bookid 
                    WHERE bc.bookcopyid not in (SELECT bookcopyid FROM loans WHERE returned <> 1 or returned is NULL);"""
        cursor.execute(qstr)
        books = cursor.fetchall()

        # Show book details if there is a book id selected
        cursor = getCursor()
        qstr = "SELECT * FROM books WHERE bookid = %s;"
        qargs = (book_id,)
        cursor.execute(qstr,qargs)
        book_details = cursor.fetchone()

        # Show book copies dropdown if there is a book id selected
        cursor = getCursor()
        # Get available copies of the selected book
        qstr = """SELECT bc.bookcopyid, bc.bookid, bc.format
                    FROM bookcopies bc
                    WHERE bc.bookid = %s
                    and bc.bookcopyid not in 
                        (SELECT bookcopyid FROM loans WHERE returned <> 1 or returned is NULL);"""
        qargs = (book_id,)
        cursor.execute(qstr,qargs)
        book_copies = cursor.fetchall()
    # Pass current date for loan date
        todaydate = datetime.now().date()  # Also needs a value, so always pass the value
    
    return render_template("loan.html", loandate=todaydate, borrowers=borrowers, 
                           books=books, book_copies=book_copies, book_details=book_details,
                           borrower_id=borrower_id,book_id=book_id, book_copy_id=book_copy_id )    


@app.route("/loan/add", methods=["POST"])
def addloan():
    borrower_id = request.form.get('borrower')
    book_copy_id = request.form.get('book_copy')
    loan_date = request.form.get('loandate')
    cur = getCursor()
    qstr = "INSERT INTO loans (borrowerid, bookcopyid, loandate, returned) VALUES(%s,%s,%s,0);"
    qargs = (borrower_id, book_copy_id, str(loan_date))
    try:
        cur.execute(qstr,qargs)
    except:
        return redirect(url_for('listbooks')+"?loan=error")
    return redirect(url_for('loansbyborrower'))


@app.route("/loan/return", methods=["GET"])
def loan_return():
    loan_id = request.args.get('loan_id')
    cur = getCursor()
    qstr = "UPDATE loans SET returned = '1' WHERE loanid = %s;"
    qargs = (loan_id,)
    cur.execute(qstr,qargs)
    return redirect(url_for('loansbyborrower'))


@app.route("/borrowers")
def borrowers():
    cursor = getCursor()
    qstr = "SELECT * FROM borrowers;"
    cursor.execute(qstr)
    borrowers = cursor.fetchall()
    return render_template("borrowers.html", borrowers = borrowers)


@app.route("/borrower", methods=['GET'])
def borrower():
    cursor = getCursor()
    borrower_id = request.args.get('id')
    qstr = "SELECT * FROM borrowers where borrowerid = %s;"
    qargs = (borrower_id,)
    cursor.execute(qstr,qargs)
    borrower = cursor.fetchone()
    return render_template("borrower.html", borrower=borrower)

@app.route("/borrower/edit", methods=['GET'])
def borrower_edit():
    cursor = getCursor()
    borrower_id = request.args.get('id')
    qstr = "SELECT * FROM borrowers where borrowerid = %s;"
    qargs = (borrower_id,)
    cursor.execute(qstr,qargs)
    borrower = cursor.fetchone()
    return render_template("borroweredit.html", borrower=borrower)

@app.route("/borrower/edit/update", methods=['POST'])
def borrower_edit_update():
    cursor = getCursor()
    formvals = request.form    # Returns a dictionary of {formelementname: value} pairs
    qstr = """update borrowers 
                set firstname=%s, familyname=%s, dateofbirth=%s, address=%s, 
                    suburb=%s, city=%s, postcode=%s					
                where borrowerid = %s;"""
    qargs = (formvals['first_name'], formvals['last_name'], formvals['dob'], formvals['address'], 
             formvals['suburb'], formvals['city'], formvals['postcode'], formvals['id'])
    cursor.execute(qstr,qargs)
    return redirect("/borrower?id="+formvals['id'])

@app.route("/borrower/add")
def borrower_add():
    return render_template("borroweradd.html")

@app.route("/borrower/add/insert", methods=['POST'])
def borrower_add_insert():
    cursor = getCursor()
    formvals = request.form    # Returns a dictionary of {formelementname: value} pairs
    qstr = """insert into borrowers(firstname, familyname, dateofbirth, address, suburb, city, postcode)
                            values(%s, %s, %s, %s, %s, %s, %s);"""
    qargs = (formvals['first_name'], formvals['last_name'], formvals['dob'], formvals['address'], 
             formvals['suburb'], formvals['city'], formvals['postcode'])
    cursor.execute(qstr,qargs)
    return redirect("/borrowers")


##############################################################
# Borrower - using combined page
@app.route("/borrowers-combined")
def borrowers_combined():
    cursor = getCursor()
    qstr = "SELECT * FROM borrowers;"
    cursor.execute(qstr)
    borrowers = cursor.fetchall()
    return render_template("borrowers_combined.html", borrowers = borrowers)


@app.route("/borrower-combined", methods=['GET'])
def borrower_combined():
    cursor = getCursor()
    borrower_id = request.args.get('id')
    mode = request.args.get('mode')
    if mode not in ('edit','add'): 
        mode = 'display'
    if mode != 'add':
        qstr = "SELECT * FROM borrowers where borrowerid = %s;"
        qargs = (borrower_id,)
        cursor.execute(qstr,qargs)
        borrower = cursor.fetchone()
    else:
        borrower = ()
    return render_template("borrower_combined.html", mode=mode, borrower=borrower)

############################################################
# loansbyborrower
@app.route("/loansbyborrower")  
def loansbyborrower():
    """Lists all loans grouped by borrower. This page uses Jinja's groupby filter (advanced).
    """
    cursor = getCursor()
    qstr = """ select br.borrowerid, br.firstname, br.familyname,  
                l.borrowerid, l.bookcopyid, l.loandate, l.returned, b.bookid, b.booktitle, b.author, 
                b.category, b.yearofpublication, bc.format, l.loanid 
            from books b
                inner join bookcopies bc on b.bookid = bc.bookid
                    inner join loans l on bc.bookcopyid = l.bookcopyid
                        inner join borrowers br on l.borrowerid = br.borrowerid 
            order by br.familyname, br.firstname, l.loandate;"""
    cursor.execute(qstr)
    loan_list = cursor.fetchall()
    return render_template("loansbyborrower.html", loan_list = loan_list)      

@app.route("/loansbyborrower_groupby")  
def loansbyborrower_groupby():
    """Lists all loans grouped by borrower. This page uses Jinja's groupby filter (advanced).
    """
    cursor = getCursor()
    qstr = """ select br.borrowerid, br.firstname, br.familyname,  
                l.borrowerid, l.bookcopyid, l.loandate, l.returned, b.bookid, b.booktitle, b.author, 
                b.category, b.yearofpublication, bc.format 
            from books b
                inner join bookcopies bc on b.bookid = bc.bookid
                    inner join loans l on bc.bookcopyid = l.bookcopyid
                        inner join borrowers br on l.borrowerid = br.borrowerid 
            order by br.familyname, br.firstname, l.loandate;"""
    cursor.execute(qstr)
    loan_list = cursor.fetchall()
    return render_template("loansbyborrower_groupby.html", loan_list = loan_list)      

############################################################
# Current Loans V1
@app.route("/currentloans")
def currentloans():
    """Lists all of the current loans.
    Uses currentloansfilter() when a value is typed in the filter field to add a WHERE clause to the query.
    """
    cursor = getCursor()
    qstr=""" select br.borrowerid, br.firstname, br.familyname,  
                l.borrowerid, l.bookcopyid, l.loandate, l.returned, b.bookid, b.booktitle, b.author, 
                b.category, b.yearofpublication, bc.format 
            from books b
                inner join bookcopies bc on b.bookid = bc.bookid
                    inner join loans l on bc.bookcopyid = l.bookcopyid
                        inner join borrowers br on l.borrowerid = br.borrowerid 
            order by br.familyname, br.firstname, l.loandate;"""
    cursor.execute(qstr)
    loan_list = cursor.fetchall()
    return render_template("currentloans.html", loan_list = loan_list)


@app.route("/currentloans/filter", methods=["POST"])    # POST method required to read input from filter field in form
def currentloansfilter():
    """Lists all of the current loans using the same template page, but with an added where clause in the query.
    """
    bookTitle = request.form.get('book')
    cursor = getCursor()
    # A WHERE clause is added to the query using the SQL LIKE operator for partial text matches
    qstr=""" select br.borrowerid, br.firstname, br.familyname,  
                l.borrowerid, l.bookcopyid, l.loandate, l.returned, b.bookid, b.booktitle, b.author, 
                b.category, b.yearofpublication, bc.format 
            from books b
                inner join bookcopies bc on b.bookid = bc.bookid
                    inner join loans l on bc.bookcopyid = l.bookcopyid
                        inner join borrowers br on l.borrowerid = br.borrowerid
            where b.booktitle like %s
            order by br.familyname, br.firstname, l.loandate;"""
    # The % characters here are wildcards in MySQL that work with the LIKE operator
    qargs = (f'%{bookTitle}%',)
    cursor.execute(qstr,qargs)
    #print(cursor.statement)
    loan_list = cursor.fetchall()
    return render_template("currentloans.html", loan_list = loan_list, booktitle = bookTitle)


############################################################
# Current Loans V2
@app.route("/currentloansv2", methods=['POST','GET'])  #Need to allow GET method too for times when the page first loads from the link, otherwise get an error
def currentloansv2():
    """An alternative to currentloans() that filters by book from a dropdown list instead.
    Unlike currentloans() version 1, uses the same function to display the original page and filtered page.
    It dynamically adds the WHERE clause into the query string when the HTML form returns a value.
    """
    bookid = request.form.get('book')
    #if bookid can be converted to an integer, convert to integer, otherwise set to None.
    try:
        bookid=int(bookid)
    except:
        bookid=None
    cursor = getCursor()
    qstr1 = """ select br.borrowerid, br.firstname, br.familyname,  
                l.borrowerid, l.bookcopyid, l.loandate, l.returned, b.bookid, b.booktitle, b.author, 
                b.category, b.yearofpublication, bc.format 
            from books b
                inner join bookcopies bc on b.bookid = bc.bookid
                    inner join loans l on bc.bookcopyid = l.bookcopyid
                        inner join borrowers br on l.borrowerid = br.borrowerid """
    # Only insert the where clause in qstr if this function call came from a form submit (POST) and the book id is not empty
    # Filter the list with a WHERE clause - but not if the empty '<Select a book>' option is selected, which shows all books again
    if request.method == 'POST' and bookid is not None:     
        qstr2 = "where b.bookid = %s"   # Add this to the qstr if a bookid is passed
        qargs = (bookid,)               # Add bookid to the qargs passed to execute()
    else:                       # Otherwise, there is no WHERE clause and no qargs to pass
        qstr2 = ""                  # qstr2 is an empty string
        qargs = ()                  #    and qargs is also empty
    qstr3 = "order by br.familyname, br.firstname, l.loandate;"""
    # Combine all of the qstr parts into one qstr string. qstr2 will be "" if no value passed.  Spaces avoid errors if no space between the strings.
    qstr = qstr1 + ' ' + qstr2 + ' ' +qstr3
    #print(qstr)                    # Uncomment to see the query string
    cursor.execute(qstr, qargs)
    loan_list = cursor.fetchall()
    #print(cursor.statement)    # Shows the SQL statement that was executed
    cursor = getCursor()
    qstr=""" select distinct b.bookid, b.booktitle
            from books b
                inner join bookcopies bc on b.bookid = bc.bookid
                    inner join loans l on bc.bookcopyid = l.bookcopyid
                        inner join borrowers br on l.borrowerid = br.borrowerid
            order by b.booktitle;"""
    cursor.execute(qstr)
    book_list = cursor.fetchall()
    return render_template("currentloansv2.html", loan_list = loan_list, book_list = book_list, bookid=bookid)      #bookid is used to make sure the selected book is shown in the dropdown when the page reloads

