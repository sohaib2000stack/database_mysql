import mysql.connector

mydb = mysql.connector.connect(
  host="127.0.0.1",
  user="root",
  password="",
  database="test2"
)

mycursor = mydb.cursor()

sql = "INSERT INTO employee (id, name, age, year, Address) VALUES (%s, %s, %s, %s, %s)"
val =("2", "sohaib", "24", "2000", "fb area")
mycursor.execute(sql, val)

mydb.commit()

print(mycursor.rowcount, "record inserted.")













