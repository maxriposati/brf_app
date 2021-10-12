from flask import Flask, render_template, request
from forms import FormContacto,FormLogin,FormRestablecer,FormRetroalimentacion,FormUsuario,FormUsuarioFinal
import os

app = Flask(__name__)

app.secret_key = os.urandom(24)

@app.route('/')
@app.route('/home')
def index():
    return render_template('index.html', titulo="home")

@app.route('/mision')
def mision():
    return render_template('mision.html', titulo="mision")

@app.route('/vision')
def vision():
    return render_template('vision.html', titulo="vision")

@app.route('/servicios')
def servicios():
    return render_template('servicios.html', titulo="servicios")

@app.route('/contacto', methods=["GET","POST"])
def contacto():
    formcontacto = FormContacto()
    return render_template('contacto.html', titulo="contacto", form=formcontacto)

@app.route('/login', methods=["GET","POST"])
def login():
    formlogin = FormLogin()
    formFinalUser = FormUsuarioFinal()
    if request.method == 'POST':
        username = request.form['username']
        password = request.form['password']
        if username=="admin" and password=="admin":
            return render_template('mainadmin.html', titulo="main admininstrador")
        elif username=="user" and password=="user":
            id = 1
            return render_template('mainusuario.html', titulo="main usuario", id=id, form=formFinalUser)
        else:
            return render_template('login.html', titulo="login", form=formlogin)
            
    return render_template('login.html', titulo="login", form=formlogin)
            
            

@app.route('/politicas')
def politicas():
    return render_template('politicas.html', titulo="politicas")

@app.route('/recuperarpass', methods=["GET","POST"])
def recuperar():
    formlogin = FormLogin()
    formRestablecer = FormRestablecer()
    if request.method == 'POST':
        return render_template('login.html', titulo="login", form=formlogin)    
    return render_template('recuperarpass.html', titulo="recuperar contraseña", form=formRestablecer)

@app.route('/mainadmin')
def administrador():
    return render_template('mainadmin.html', titulo="main admininstrador")

@app.route('/mainadmin/crear')
def crear():
    formUser = FormUsuario()
    return render_template('crearusuario.html', titulo="crear usuario", form=formUser)

@app.route('/mainadmin/editar/<int:id>')
def editar(id=1):
    return render_template('editarusuario.html', titulo="editar usuario", id=id)

@app.route('/mainadmin/evaluar/<int:id>')
def evaluar(id):
    formEvaluar = FormRetroalimentacion()
    return render_template('evaluacion.html', titulo="evaluar usuario", id=id, form=formEvaluar)

@app.route('/mainusuario/<int:id>')
def usuario(id=1):
    formFinalUser = FormUsuarioFinal()
    return render_template('mainusuario.html', titulo="main usuario", id=id, form=formFinalUser)




