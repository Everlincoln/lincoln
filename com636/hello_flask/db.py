import connect, mysql.connector
print("import done - establishing connection")
conn = mysql.connector.connect(user=connect.dbuser, \
     password=connect.dbpass, host=connect.dbhost, database=connect.dbname, autocommit=True)
print(f"connection done - {conn}")
with conn:
     cur = conn.cursor()
     cur.execute("select * from orders limit 5;")
     select_result = cur.fetchall()
     print(f"{select_result[0]}")
     print(select_result)
     print(type(select_result))
     for result in select_result:
          print(f"\nResult type: {type(result)}")
          print(f"Result: {result}")
          for entry in result:
               print(f"   Entry: {entry}  {type(entry)}")


