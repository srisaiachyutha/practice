import sqlite3
conn=sqlite3.connect('svec.db')
cur=conn.cursor()
try:
     query="insert into students values('17121a05h3','achyutha','cse',1234567891)"
     cur.execute(query)
     conn.commit()#for commiting 
except Exception as e:
     print(e)
finally:
     print('values are updated')
     cur.close()
     conn.close()
     
