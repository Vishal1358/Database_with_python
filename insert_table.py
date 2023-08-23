import mysql.connector

conn = mysql.connector.connect(host="localhost", user="root", passwd="Vishal#1358", database="vishal")
cur = conn.cursor()

q = "insert into student(rollno,sname,branch)values(%s,%s,%s)"
v = [(503, "Megha", "MEC"),(504,"Moin","EEE"),(505, "Ramesh", "MEC"),(501,"Suhas","EEE"),(502,"Nandu","AERO")]

# cur.execute("create table student(rollno int not null primary key, sname varchar(20) not null, branch varchar(10) not null)")

try:
    cur.executemany(q, v)
    conn.commit()
except:
    conn.rollback()

conn.close()
