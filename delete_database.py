import mysql.connector

conn = mysql.connector.connect(host="localhost",user="root",passwd="Vishal#1358",database="vishal")
cur = conn.cursor()

# cur.execute("delete from student where percentage<90")  # delete the particular data
# cur.execute("alter table student drop column branch")     # delete the particular column
cur.execute("drop table student")       # delete the table
conn.commit()

conn.close()