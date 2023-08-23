import mysql.connector

conn = mysql.connector.connect(host="localhost", user="root", passwd="Vishal#1358", database="vishal")
cur = conn.cursor()

cur.execute("ALTER TABLE student ADD percentage FLOAT(5) default '90'")     # adding column
cur.execute("alter table student add grade varchar(5)")     # adding column
conn.commit()

conn.close()