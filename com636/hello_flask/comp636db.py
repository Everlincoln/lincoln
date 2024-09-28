import connect, mysql.connector
print("import done - establishing connection")
conn = mysql.connector.connect(user=connect.dbuser, \
     password=connect.dbpass, host=connect.dbhost, database=connect.dbname, autocommit=True)
print(f"connection done - {conn}")
with conn:
        cur = conn.cursor()
        sql = "select * from people;"
        cur.execute(sql)    # Executes the query
        dbPeople = cur.fetchall()   # Passes the results of the query into a list of tuples
        print(f"dbPeople: {dbPeople}")