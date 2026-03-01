from flask import Flask, render_template, request, redirect, url_for, session
from werkzeug.security import generate_password_hash, check_password_hash
import mysql.connector

mydb = mysql.connector.connect(
  host="localhost",
  user="flask",
  password="P@ssw0rd!",
  database="flask"
)
mycursor = mydb.cursor()



app = Flask(__name__)
app.secret_key = 'secret_key_here'



# Home page with login status and links to login/register or logout
@app.route('/')
def home():
    if 'username' in session:
        return render_template("raiz.html")
    return redirect(url_for('login'))


# Registration page to create new users
@app.route('/register', methods=['GET', 'POST'])
def register():
    if request.method == 'POST':
        username = request.form['username']
        email = request.form['email']
        password = request.form['password']
        password = generate_password_hash(password)

        mycursor = mydb.cursor()

        # 1. Aqui hacemos un INSERT a la base de datos con los datos recopilados del formulario
        sql = "INSERT INTO usuarios (nom_usu , email , contraseña) VALUES (%s, %s, %s)"
        val = (username , email , password)
        mycursor.execute (sql,val)

        #2. Hacemos un COMMIT para guardarlos en la base de datos 
        mydb.commit()

        #3. Redireccionamos a la URL de login para que inicie sesion
        return redirect(url_for('login'))
    return render_template('register.html')



# Login page to authenticate users
@app.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        username = request.form['username']
        password = request.form['password']

        mycursor = mydb.cursor()
        
        # 1. Buscamos solo el hash de la contraseña de ese usuario
        sql = 'SELECT contraseña FROM usuarios WHERE nom_usu = %s'
        mycursor.execute(sql, (username,))
        resultado = mycursor.fetchone()

        # 2. Comprobamos si el usuario existe en la base de datos
        if resultado is not None:
            # Extraemos el string del hash de la tupla
            hashed_password = resultado[0]

            # 3. Comprobamos si la contraseña coincide con el hash
            if check_password_hash(hashed_password, password):
                # Login exitoso: guardamos en la sesión
                session['username'] = username
                return render_template("index.html")
            else:
                # Contraseña incorrecta
                return "<h1>Las credenciales usadas con incorrectas, prueba de nuevo o registrate</h1>"
        else:
            # El usuario no existe
            return "<h1>Este nombre de usuario no esta registrado</h1>"

    # Si el método es GET, simplemente renderiza el formulario
    return render_template('login.html')


@app.route('/form_resum', methods=['GET', 'POST'])
def form_resum():
    if 'username' in session:
        if request.method == 'POST':
            nombre = request.form['nombre']
            apellido = request.form ['apellido']
            carrera = request.form ['carrera']
            opinion = request.form ['opinion']

            mycursor = mydb.cursor()

            sql = "INSERT INTO encuestas (nombre , apellido , titulo , opinion) VALUES (%s, %s, %s, %s)"
            val = (nombre , apellido , carrera , opinion)
            mycursor.execute(sql,val) 

            mydb.commit()
            
            return render_template('index.html')
            
        # Si el método es GET, simplemente mostramos el formulario
        return render_template('form_resum.html')
    return redirect(url_for('login'))


@app.route('/about_me')
def about_me():
    return render_template('about_me.html')



# Logout route to clear the session and redirect to home
@app.route('/logout')
def logout():
    session.pop('username', None)
    return render_template('raiz.html')



# to execute flask app run in code
if __name__ == '__main__':
    app.run(debug=True)
