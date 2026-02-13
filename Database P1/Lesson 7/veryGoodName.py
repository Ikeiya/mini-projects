import mysql.connector

try:
  mydb = mysql.connector.connect(
    host="localhost",
    user="root",
    password="Byih1111",
    database="transport"
  )
except Exception as ex:
  print(ex)
else:
  print("Success")

userInput = input("Enter something here: ")

mycursor = mydb.cursor()

mycursor.execute(f"SELECT route, bound, name_en FROM routestop INNER JOIN stops ON routestop.stop=stops.stop WHERE route='{userInput}' AND bound='I' AND service_type='1'")

myresult = mycursor.fetchall()

if len(myresult) == 0:
  print("no result")
else:
  for x in myresult:
    print(x)
