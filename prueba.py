import mysql.connector

mydb = mysql.connector.connect(
  host="localhost",
  user="flask",
  password="P@ssw0rd!",
  database="flask"
)

mycursor = mydb.cursor()


#PRUEBA 1
# sql = "INSERT INTO usuarios (nom_usu, email, contraseña) VALUES (%s,%s,%s)"
# val = ("Hans", "hans@proven.cat" , "P@ssw0rd!")


# PRUEBA 2
# sql1 = ("SELECT contraseña FROM usuarios WHERE nom_usu = %s")
# val1 = ('arman', )

# mycursor.execute(sql1,val1)

# resultado = mycursor.fetchone()

# for x in resultado:
#     print(x)
