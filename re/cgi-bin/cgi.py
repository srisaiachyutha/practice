import sqlite3
conn=sqlite3.connect('svec.db')


cur=conn.cursor()#executing query
try:
     query="create table students(rollno text,name text,branch text,phoneno integer)"
     cur.execute(query)
     print('created the database...')
except Exception as e:
     print(e)
finally:
     print('successfully created...')
     cur.close()
     conn.close()
