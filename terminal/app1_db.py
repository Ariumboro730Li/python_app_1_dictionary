import mysql.connector

mydb = mysql.connector.connect(
  host = "localhost",
  user = "root",
  password = "Ariumboro@20milyar",
  database = "belajar_python"
)

while True:
  word = input("Enter Word = ")
  mycursor = mydb.cursor()
  query = mycursor.execute(f"select definition from dictionary where expression like '%{word}%' ")
  results = mycursor.fetchall()

  if results:
    for result in results:
        print(result)
  else:
    print("Word didn't EXISTS")
