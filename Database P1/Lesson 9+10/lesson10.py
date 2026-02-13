import mysql.connector
import datetime

mydb = mysql.connector.connect(
  host="localhost",
  user="root",
  password="Byih1111",
  database="transport"
)

def select():
  userInput = input("Enter something here: ")
  mycursor = mydb.cursor()
  mycursor.execute(f"SELECT route, bound, name_en FROM routestop INNER JOIN stops ON routestop.stop=stops.stop WHERE route='{userInput}' AND bound='I' AND service_type='1'")
  myresult = mycursor.fetchall()
  if len(myresult) == 0:
    print("no result")
  else:
    for x in myresult:
      print(x)

def updateUser():
  mycursor = mydb.cursor()
  mycursor.execute(f"CREATE TABLE IF NOT EXISTS users (userid int AUTO_INCREMENT NOT NULL, username VARCHAR(255) NOT NULL UNIQUE, createdTime DATETIME NOT NULL, updatedTime DATETIME NOT NULL, PRIMARY KEY(userid))")
  mycursor.close()

def favourite():
  mycursor = mydb.cursor()
  mycursor.execute(f"CREATE TABLE IF NOT EXISTS favourite (recordId int AUTO_INCREMENT NOT NULL, userid int NOT NULL, route VARCHAR(255) NOT NULL, bound VARCHAR(255) NOT NULL, service_type int, PRIMARY KEY(recordId), FOREIGN KEY (userid) REFERENCES users(userid))")
  mycursor.close()

def createUser(username):
  mycursor = mydb.cursor()
  sql = f"INSERT INTO users (username, createdTime, updatedTime) VALUES ('{username}', '{datetime.datetime.utcnow()}', '{datetime.datetime.utcnow()}')"
  mycursor.execute(sql)
  mydb.commit()
  print(mycursor.rowcount, "record inserted.")
  mycursor.close()

def addFavorites(userId, route, bound):
  mycursor = mydb.cursor()
  sql = f"INSERT INTO favourite (userId, route, bound, service_type) VALUES ('{userId}','{route}', '{bound}', {1})"
  mycursor.execute(sql)
  mydb.commit()
  print(mycursor.rowcount, "record inserted.")
  mycursor.close()

updateUser()
favourite()

def login():
  global userId
  command1 = input("Select Sign Up or Login: ")
  mycursor = mydb.cursor(buffered=True)
  condition = True
  if command1 == "Sign Up":
    while condition:
      username = input("Enter your desired username (Input return to return to main menu): ")
      mycursor.execute(f"SELECT COUNT(*) FROM users WHERE users.username='{username}'")
      if username == "return":
        mycursor.close()
        condition = False
        login()
      elif mycursor.fetchall()[0][0] == 0:
        createUser(username)
        print("Username Created")
        mycursor.execute(f"SELECT users.userid FROM users WHERE users.username='{username}'")
        userId = mycursor.fetchall()
        condition = False
      else:
        print("Username Taken")
  elif command1 == "Login":
    username = input("Enter your username (Input return to return to main menu): ")
    mycursor.execute(f"SELECT COUNT(*) FROM users WHERE users.username='{username}'")
    while condition:
      if username == "return":
        mycursor.fetchall()
        mycursor.close()
        condition = False
        login()
      elif mycursor.fetchall() != 0:
        mycursor.execute(f"SELECT users.userid FROM users WHERE users.username='{username}'")
        userId = mycursor.fetchall()
        print("Logged In")
        condition = False
      else:
        print("Username does not exist")
  else:
    print("Invalid Action")
    login()
  mycursor.close()

def addFavourites():
  

login()
print(userId)
