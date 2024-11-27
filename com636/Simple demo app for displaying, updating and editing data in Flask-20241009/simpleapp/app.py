from flask import Flask
from flask import render_template
from flask import request
from flask import redirect
from flask import url_for
import mysql.connector
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

@app.route("/people")
def people():
    """An example of a simple function to get data from MySQL and send that to an HTML page to display."""
    connection = getCursor()        # Create the cursor connection, using the getCursor function, which we will provide for you.
    qstr = "SELECT * FROM people;"  # The query to send to MySQL Server, stored in qstr.
    connection.execute(qstr)        # Execute the SQL query in qstr
    people = connection.fetchall()        # Returns all rows from the query - as a list of tuples (one tuple per row).
    return render_template("people.html", people = people)  # Render (create) the page 'people.html' and send the list of tuples returned
                                                            #   from database as 'people'


@app.route("/person", methods=['GET'])  # Uses the GET method to extract the data from the URL (after the ? in the URL)
def person():
    """A function that:
            - Reads the data from the URL using the GET method (e.g., /person?id=123)
            - Returns the data from the query dynamically to only match the ID on the URL that was clicked."""
    connection = getCursor()
    id = request.args.get('id')         # request.args is a dictionary, containing the info after ? in the link person?id=123
    qstr = "SELECT * FROM people WHERE id = %s;"
    qargs = (id,)   # the items in this tuple are placed into the SQL query where the %s markers are, in the order they appear in the query
    connection.execute(qstr,qargs)      # Note the second qargs argument, which provides the data to match the %s markers in the qstr 
    person = connection.fetchone()      # Returns only one row from the query - as a tuple.
    return render_template("person.html", person=person)

@app.route("/person/edit", methods=['GET'])
def person_edit():
    """This function returns the same data as the person function above (but it renders a different HTML page: person_edit.html)"""
    connection = getCursor()
    id = request.args.get('id')
    qstr = "SELECT * FROM people where id = %s;"
    qargs = (id,)
    connection.execute(qstr,qargs)
    person = connection.fetchone()
    return render_template("person_edit.html", person=person)   # This page displays a form that can return data.

@app.route("/person/edit/update", methods=['POST'])   
def person_edit_update():
    """This function uses the POST method to read the data updated on the form created by the person_edit.html page.
        It uses an UPDATE query to change the data in the database.
        It then redirects to the /person page for that person id to confirm that the changes were successfully made."""
    connection = getCursor()
    formvals = request.form    # Returns a dictionary of {form-element-name: value} pairs
    qstr = """update people         
                set name = %s, room = %s					
                where id = %s;"""   # This UPDATE query updates the person to the values on the form
    qargs = (formvals['name'], formvals['room'], formvals['id'])    # 3 parameters to match the 3 %s markers in the order the appear in the query
    connection.execute(qstr,qargs)          # The query executes here, but UPDATE queries make the changes in the database, but don't send any
                                            #   data back to Python - so there is no data to assign to a variable from fetchall() or fetchone()
    return redirect("/person?id="+formvals['id'])   # redirect is like clicking a link on a web page, which is then handled by app.py as a route.
                                                    #    In this case, we're reloading the person details page using the GET method (/person?id=123)
                                                    #    so that the user can confirm that the changes were made

@app.route("/person/add")
def person_add():
    """This function renders a page with a form to add a new person. It doesn't need any data to create the form though 
    because the form will be blank when the page loads.  So this function only needs one line, to render the page."""
    return render_template("person_add.html")   

@app.route("/person/add/insert", methods=['POST'])
def person_add_insert():
    """This function uses the POST method to read the data for a new perosn entered on to the form created by the person_add.html page.
        It uses an INSERT INTO query to add a new row to the table.  It doesn't include an id value, because this is automatically 
        assigned a unique value by the database.
        It then redirects to the /people page to confirm that the new person is now saved in the database."""
    connection = getCursor()
    formvals = request.form     # Returns a dictionary of the data from the form corresponding to the input field names on the form, 
                                #    e.g.: {'name':'Petra', 'room':'T115'}
    qstr = """insert into people(name, room)
                            values(%s, %s);"""  # Inserts the new person into a row in the people table (the id is automatically assigned)
    qargs = (formvals['name'], formvals['room'])    # These are the two values from the request.form dictionary
    connection.execute(qstr,qargs)      # Executes the query and adds the row, but no data is returned to Python
    new_id = connection.lastrowid       # A trick to get the new id created by the database for the new row
    return redirect("/person?id="+str(new_id))   # redirect to person details page to confirm the person was added successfully.

