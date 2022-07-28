import mysql.connector as conn

try:
    mydb = conn.connect(host="localhost", user="root", passwd="Slugger@8978")
    cursor = mydb.cursor()
    s = "insert into rakesh1.rakdetails values(101, 'Rakesh Uikey', 'rakeshuikey@gmail.com', 100, 30)"
    cursor.execute(s)
    cursor.execute(s)
    cursor.execute(s)
    cursor.execute(s)
    cursor.execute(s)
    cursor.execute(s)
    mydb.commit()
    cursor.execute("select * from rakesh1.rakdetails")
    for i in cursor.fetchall():
        print(i)

except Exception as e:

    print(str(e))

finally:
    mydb.close()