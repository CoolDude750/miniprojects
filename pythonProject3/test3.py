import mysql.connector as conn
try:
    mydb = conn.connect(host="localhost", user="root", passwd="Slugger@8978",use_pure='true')

    cursor = mydb.cursor()
    cursor.execute("select employee_id, emp_mailid from rakesh1.rakdetails")
    l = []
    for i in cursor.fetchall():
        l.append(i)
    print(l)
    print(type(l[0]))

except Exception as e:
    mydb.close()
    print(str(e))

