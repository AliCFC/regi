#!C:\Program Files\Python37-32\python.exe
print("Content-Type: text/html")
print()

import cgi
import mysql.connector

print("<h1>Welcom to Python web programing</h1>")
print("<hr/>")
print("<h2>Using Input Tags</h2>")

form=cgi.FieldStorage()

roll=form.getvalue("roll")
name=form.getvalue("name")
id=form.getvalue("ID")

con=mysql.connector.connect( host='localhost', user='',   passwd="", database="mylogin")
mycursor=con.cursor()
sql= 'insert into student(roll,name,ID) values(%s,%s,%s)'
val=(roll,name,id)
mycursor.execute(sql, val)
con.commit()

mycursor.close()
con.close()
print("<h1>Record Inserted Succefully</h1>")
