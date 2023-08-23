import mysql.connector

conn = mysql.connector.connect(host="localhost",user="root",passwd="Vishal#1358",database="Thor")
cur = conn.cursor()

cur.execute("create table students(rollno int primary key,sname varchar(15),percentage float,branch varchar(10))")

conn.close()