import mysql.connector

conn = mysql.connector.connect(host="localhost",user="root",passwd="Vishal#1358",database="vishal")

cur = conn.cursor()
cur.execute("create table student(rollno int not null primary key, sname varchar(20) not null, branch varchar(15) not null)")
conn.close()