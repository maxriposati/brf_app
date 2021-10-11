from flask import Flask, render_template, request


app = Flask(__name__)

@app.route('/')
@app.route('/home')
def homepage():
        return render_template('index.html')

@app.route('/mision')
def mision():
    return render_template('mision.html')

@app.route('/vision')
def vision():
    return render_template('vision.html')

@app.route('/servicios')
def servicios():
    return render_template('servicios.html')

@app.route('/contacto')
def contacto():
    return render_template('contacto.html')

@app.route('/politicas')
def politicas():
    return render_template('politicas.html')

@app.route('/recuperarpass')
def recuperar():
    return render_template('olvidarpass.html')

@app.route('/login',methods=['GET','POST'])
def login():
    return render_template('login.html')

@app.route('/mainadmin')
def administrador():
    return render_template('mainadmin.html')

@app.route('/mainadmin/crear')
def crear():
    return render_template('crearusuario.html')

@app.route('/mainadmin/editar/<int:id>')
def editar(id):
    return render_template('editarusuario.html')

@app.route('/mainadmin/evaluar/<int:id>')
def evaluar(id):
    return render_template('evaluacion.html')

@app.route('/mainusuario/<int:id>')
def usuario(id):
    return render_template('mainusuario.html')
	

if __name__ == "__main__":
    app.run(host='0.0.0.0', port=8080)




