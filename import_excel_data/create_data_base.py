import mysql.connector

conn = mysql.connector.connect(host="localhost",user="root",passwd="Vishal#1358")
c = conn.cursor()
c.execute("create database Thor")
c.execute("show databases")
for i in c:
    print(i)