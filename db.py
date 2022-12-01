import mysql.connector

mydb = mysql.connector.connect(host="localhost",
            user="root", passwd="98399653zX*", database="nyc_taxi")

mycursor  = mydb.cursor()

mycursor.execute("select * from yellow_trip_jan")

results= mycursor.fetchone()

for i in results:
    print(i)

