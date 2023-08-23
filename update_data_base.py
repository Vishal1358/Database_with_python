import mysql.connector

conn = mysql.connector.connect(host="localhost", user="root", passwd="Vishal#1358", database="vishal")
cur = conn.cursor()

cur.execute("update student set grade='A+' where percentage >=90")
cur.execute("update student set percentage=85 where rollno=501")
conn.commit()
conn.close()
