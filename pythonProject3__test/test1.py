import mysql.connector as conn

mydb = conn.connect(host = "localhost" , user ="root" , passwd = "Slugger@8978" )

print(mydb)