import mysql.connector as conn
try:
    mydb = conn.connect(host="localhost", user="root", passwd="Slugger@8978")
    cursor = mydb.cursor()
    print(mydb.is_connected())
    #cursor.execute("create database rakesh1")
    #cursor.execute("show databases")
    #s  = "create table rakesh1.rakdetails(employee_id int(10), emp_name varchar(80), emp_mailid varchar(80),emp_salary int(6), emp_attendence int(3))"
    q1 = cursor.execute("select * from rakesh1.rakdetails")
    print(q1)

except Exception  as e:
    mydb.close()
    print(str(e))
