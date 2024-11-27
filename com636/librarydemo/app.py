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
    return render_template("home.html")

@app.route("/listbooks")
def listbooks():
    connection = getCursor()
    connection.execute("SELECT bookid, booktitle, author, category, yearofpublication FROM books;")
    bookList = connection.fetchall()
    #print(bookList)
    return render_template("booklist.html", booklist = bookList)    

@app.route("/bookdetails", methods=["GET"])
def bookdetails():
    bookid = request.args.get('bookid')
    connection = getCursor()
    sql = "SELECT * FROM books WHERE bookid = %s;"
    parameters = (bookid,)
    connection.execute(sql,parameters)
    bookDetails = connection.fetchall()
    #print(bookDetails)
    return render_template("bookdetails.html", bookDetails = bookDetails)    

@app.route("/loanbook")
def loanbook():
    todaydate = datetime.now().date()
    connection = getCursor()
    connection.execute("SELECT * FROM borrowers;")
    borrowerList = connection.fetchall()
    sql = """   SELECT * FROM bookcopies 
                INNER JOIN books on books.bookid = bookcopies.bookid 
                WHERE bookcopyid not in (SELECT bookcopyid FROM loans WHERE returned <> 1 or returned is NULL);"""
    connection.execute(sql)
    bookList = connection.fetchall()
    return render_template("addloan.html", loandate = todaydate,borrowers = borrowerList, books= bookList)

@app.route("/loan/add", methods=["POST"])
def addloan():
    borrowerid = request.form.get('borrower')
    bookid = request.form.get('book')
    loandate = request.form.get('loandate')
    cur = getCursor()
    cur.execute("INSERT INTO loans (borrowerid, bookcopyid, loandate, returned) VALUES(%s,%s,%s,0);",(borrowerid, bookid, str(loandate),))
    return redirect("/currentloans")

@app.route("/listborrowers")
def listborrowers():
    connection = getCursor()
    connection.execute("SELECT * FROM borrowers;")
    borrowerList = connection.fetchall()
    return render_template("borrowerlist.html", borrowerlist = borrowerList)

@app.route("/currentloans")
def currentloans():
    connection = getCursor()
    sql=""" select br.borrowerid, br.firstname, br.familyname,  
                l.borrowerid, l.bookcopyid, l.loandate, l.returned, b.bookid, b.booktitle, b.author, 
                b.category, b.yearofpublication, bc.format 
            from books b
                inner join bookcopies bc on b.bookid = bc.bookid
                    inner join loans l on bc.bookcopyid = l.bookcopyid
                        inner join borrowers br on l.borrowerid = br.borrowerid 
            order by br.familyname, br.firstname, l.loandate;"""
    connection.execute(sql)
    loanList = connection.fetchall()
    return render_template("currentloans.html", loanlist = loanList)

@app.route("/currentloans/filter", methods=["POST"])
def currentloansfilter():
    bookTitle = request.form.get('book')
    connection = getCursor()
    sql=""" select br.borrowerid, br.firstname, br.familyname,  
                l.borrowerid, l.bookcopyid, l.loandate, l.returned, b.bookid, b.booktitle, b.author, 
                b.category, b.yearofpublication, bc.format 
            from books b
                inner join bookcopies bc on b.bookid = bc.bookid
                    inner join loans l on bc.bookcopyid = l.bookcopyid
                        inner join borrowers br on l.borrowerid = br.borrowerid
            where b.booktitle like %s
            order by br.familyname, br.firstname, l.loandate;"""
    parameters = (f'%{bookTitle}%',)
    connection.execute(sql,parameters)
    #print(connection.statement)
    loanList = connection.fetchall()
    return render_template("currentloans.html", loanlist = loanList, booktitle = bookTitle)

#Need to allow GET method too for times when the page first loads from the link, otherwise get an error
@app.route("/currentloansv2", methods=['POST','GET'])   
def currentloansv2():
    bookid = request.form.get('book')
    #if bookid can be converted to an integer, convert to integer, otherwise set to None.
    try:
        bookid=int(bookid)
    except:
        bookid=None
    connection = getCursor()
    sql1 = """ select br.borrowerid, br.firstname, br.familyname,  
                l.borrowerid, l.bookcopyid, l.loandate, l.returned, b.bookid, b.booktitle, b.author, 
                b.category, b.yearofpublication, bc.format 
            from books b
                inner join bookcopies bc on b.bookid = bc.bookid
                    inner join loans l on bc.bookcopyid = l.bookcopyid
                        inner join borrowers br on l.borrowerid = br.borrowerid """
    #Only insert the where clause if this function call came from a form submit (POST) and the book id is not empty
    if request.method == 'POST' and bookid is not None:
        sql2 = "where b.bookid = %s"
        parameters = (bookid,)
    else:
        sql2 = ""
        parameters = ()
    sql3 = "order by br.familyname, br.firstname, l.loandate;"""
    #Combine all of the SQL parts into one SQL string. SQL2 will be "" if no value passed.  Spaces avoid errors if no space between the strings.
    sql = sql1 + ' ' + sql2 + ' ' +sql3
    #print(sql)
    connection.execute(sql, parameters)
    loanList = connection.fetchall()
    #print(connection.statement)
    connection = getCursor()
    sql=""" select distinct b.bookid, b.booktitle
            from books b
                inner join bookcopies bc on b.bookid = bc.bookid
                    inner join loans l on bc.bookcopyid = l.bookcopyid
                        inner join borrowers br on l.borrowerid = br.borrowerid
            order by b.booktitle;"""
    connection.execute(sql)
    bookList = connection.fetchall()
    return render_template("currentloansv2.html", loanlist = loanList, booklist = bookList, bookid=bookid)      #bookid is used to make sure the selected book is shown in the dropdown when the page reloads
