from flask import Flask, render_template, request, flash, session,redirect,url_for
from forms import FormContacto,FormLogin,FormRestablecer,FormRetroalimentacion,FormUsuario,FormUsuarioFinal,FormRecovery
from usuarios import editar_usuario, insertar_usuario, verificar_usuario,lista_usuarios,lista_usuarios_superadmin
from usuarios import obtener_correo,eliminar_usuario_persona,consulta_recovery,reestablecer_pass
from personas import consultar_persona, insertar_persona, verificar_persona, insertar_persona, verificar_idPersona,eliminar_persona,consultar_persona_contrato,consultar_UsuarioFinal, editar_persona
from contrato import insertar_contrato,eliminar_contrato_persona, editar_contrato
from evaluacion import insertar_evaluacion, editar_evaluacion
from evaluacion import consultar_evaluacion, evaluaciones_persona, eliminar_evaluacion

import yagmail as yagmail
import os
from db import get_db
from _sqlite3 import Error
from datetime import datetime

app = Flask(__name__)

app.secret_key = os.urandom(24)



@app.before_request
def session_management():
    session.permanent = True

@app.route('/')
@app.route('/home')
def index():
    session.clear()
    session["usuario"] = "unknown"
    session["rol"] = 0
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

@app.route('/politicas')
def politicas():
    return render_template('politicas.html', titulo="politicas")

@app.route('/recuperarpass', methods=["GET","POST"])
def recuperar():
    formlogin = FormLogin()
    formRestablecer = FormRestablecer()
    if request.method == 'POST':
        username = request.form['username']
        datos=obtener_correo(username)
        correo = datos[0]
        documento = datos[1]

        yag = yagmail.SMTP('brf.noreply@gmail.com', 'Uninorte43!')
        link="http://127.0.0.1:5000/recovery/"+correo+"/"+documento
        yag.send(to=correo, subject="Password recovery", contents= 'Use this link to change your password.' + link)

        return render_template('login.html', titulo="login", form=formlogin)    
    return render_template('recuperarpass.html', titulo="recuperar contraseña", form=formRestablecer)

@app.route('/recovery/<string:correo>/<string:doc>', methods=["GET","POST"])
def recovery(correo,doc):
    formRecovery = FormRecovery()
    if request.method == 'POST':
        id=consulta_recovery(correo,doc)
        password = request.form['password']
        repassword = request.form['repassword']
        if password != repassword:
            error = 'Las contraseñas deben ser iguales'
            flash( error )
            return render_template('recovery.html', titulo="recuperando contraseña", form=formRecovery)
        else:
            if reestablecer_pass(id[0],password):
                return redirect("/login")
    return render_template('recovery.html', titulo="recuperando contraseña", form=formRecovery)
    

@app.route('/mainadmin')
def administrador():
    if session["usuario"]!="unknown" and session["rol"]!=0:
        if session["rol"]=="superAdministrador":
            usuarios=lista_usuarios_superadmin()
            if usuarios is None:
                usuarios =""
        elif session["rol"]=="administrador":
            usuarios=lista_usuarios()
            if usuarios is None:
                usuarios =""
        return render_template('mainadmin.html', titulo="main admininstrador",lista=usuarios)    
    else:
        return redirect("/")

@app.route('/mainadmin/crear', methods=["GET","POST"])
def crear():
    formUser = FormUsuario()
    if request.method== 'POST':
        document=request.form['documento']
        persona=verificar_persona(document)
        
        if persona is None:
            #table persona
            documento = request.form['documento']
            nombre = request.form['nombre']
            apellidos = request.form['apellidos']
            tipo_genero = request.form['tipo_genero']
            fechaNacimiento = request.form['fechaNacimiento']
            ciudadNacimiento = request.form['ciudadNacimiento']
            telefono = request.form['telefono']
            direccion = request.form['direccion']
            ciudadResidencia = request.form['ciudadResidencia']
            email = request.form['email']

            valor=insertar_persona(documento,nombre,apellidos,tipo_genero,fechaNacimiento,ciudadNacimiento,telefono,direccion,ciudadResidencia,email)

            #tabla user
            password = request.form['password']
            rol = request.form['rol']
            user = request.form['user']
            idPersona = verificar_idPersona(documento)
            
            valor2= insertar_usuario(password,rol,user,idPersona[0])

            #tabla contrato
            cargo = request.form['cargo']
            fechaInicio = request.form['fechaInicio']
            fechaFinalizacion = request.form['fechaFinalizacion']
            tipoContrato = request.form['tipoContrato']
            dependencia = request.form['dependencia']
            salario = request.form['salario']
            estado = request.form['estado']

            valor3= insertar_contrato(idPersona[0],cargo,fechaInicio,fechaFinalizacion,tipoContrato,dependencia,salario,estado)
            
            if valor==True and valor2==True:           
                return redirect("/mainadmin")
            
        else:
            error='El documento ya existe'
            flash(error)
            #return render_template('crearusuario.html', titulo="crear usuario", form=formUser)            
    return render_template('crearusuario.html', titulo="crear usuario", form=formUser)



@app.route('/mainadmin/editar/<int:id>', methods=["GET","POST"])
def editar(id):
    formUser = FormUsuario() 
    if request.method== 'POST':
        
        documento = request.form['documento']
        nombre = request.form['nombre']
        apellidos = request.form['apellidos']
        tipo_genero = request.form['tipo_genero']
        fechaNacimiento = request.form['fechaNacimiento']
        ciudadNacimiento = request.form['ciudadNacimiento']
        telefono = request.form['telefono']
        direccion = request.form['direccion']
        ciudadResidencia = request.form['ciudadResidencia']
        email = request.form['email']

        valor=editar_persona(documento,nombre,apellidos,tipo_genero,fechaNacimiento,ciudadNacimiento,telefono,direccion,ciudadResidencia,email,id)

        #tabla contrato
        cargo = request.form['cargo']
        fechaInicio = request.form['fechaInicio']
        fechaFinalizacion = request.form['fechaFinalizacion']
        tipoContrato = request.form['tipoContrato']
        dependencia = request.form['dependencia']
        salario = request.form['salario']
        estado = request.form['estado']

        valor2= editar_contrato(cargo,fechaInicio,fechaFinalizacion,tipoContrato,dependencia,salario,estado,id)
            
        if valor2==True and valor==True:        
            return redirect("/mainadmin")

    else:
        if session["usuario"]!="unknown" and session["rol"]!=0:
            datos=consultar_persona_contrato(id)
            formUser.ciudadNacimiento.default=datos[6]
            formUser.ciudadResidencia.default=datos[9]
            formUser.tipoContrato.default=datos[16]
            formUser.cargo.default=datos[13]
            formUser.dependencia.default=datos[17]
            formUser.process()
            return render_template('editarusuario.html', titulo="editar usuario", id=id, info=datos, form=formUser)
        else:
            return redirect("/")


@app.route('/mainadmin/eliminar/<int:id>')
def eliminar(id):
    if session["usuario"]!="unknown" and session["rol"]!=0:
        evaluaciones=evaluaciones_persona(id)
        if evaluaciones is None:
            if eliminar_contrato_persona(id):
                if eliminar_persona(id):
                    if eliminar_usuario_persona(id):
                        return redirect("/mainadmin")    
        else:
            if eliminar_evaluacion(id):
                if eliminar_contrato_persona(id):
                    if eliminar_persona(id):
                        if eliminar_usuario_persona(id):
                            return redirect("/mainadmin")   
    else:
        return redirect("/")



@app.route('/mainadmin/evaluar/<int:id>', methods=["GET","POST"])
def evaluar(id):
    formEvaluar = FormRetroalimentacion()
    if request.method== 'POST':
           #fecha
        anoEvaluacion = request.form['anoEvaluacion']
        mesEvaluacion = request.form['mesEvaluacion']
        #retroalimentacion
        puntaje = request.form['puntaje']
        retroalimentacion = request.form['retroalimentacion']
        #calificacion
        conocimiento = request.form['conocimiento']
        actitud = request.form['actitud']
        habilidad = request.form['habilidad']  

        valor=insertar_evaluacion(id,anoEvaluacion,mesEvaluacion,conocimiento,actitud,habilidad, puntaje,retroalimentacion )

        if valor==True:        
            return redirect("/mainadmin")
    
    else:
        if session["usuario"]!="unknown" and session["rol"]!=0:
            datos=consultar_persona_contrato(id)
            return render_template('evaluacion.html', titulo="Evaluar usuario", id=id, info=datos, form=formEvaluar,x="Guardar")
        else:
            return redirect("/")

        
@app.route('/mainadmin/evaluar/<int:id>/<string:anno>/<string:mes>', methods=["GET"])
def edit_evaluar(id,anno,mes):
    formEvaluar = FormRetroalimentacion()
    
    if session["usuario"]!="unknown" and session["rol"]!=0:
        formEvaluar.anoEvaluacion.data=anno
        formEvaluar.mesEvaluacion.data=mes
        evaluacion=consultar_evaluacion(anno,mes,id)
        if evaluacion is None:
            error = "El Usuario no tiene evaluacion en el mes: "+anno+" y el año: "+mes
            flash( error )
            datos=consultar_persona_contrato(id)
            return render_template('evaluacion.html', titulo="Evaluar usuario", id=id, info=datos, form=formEvaluar,x="Guardar")
        else:
            formEvaluar.puntaje.data=evaluacion[7]
            formEvaluar.retroalimentacion.data=evaluacion[8]
            datos=consultar_persona_contrato(id)
            return render_template('evaluacion.html', titulo="Evaluar usuario", id=id, info=datos, form=formEvaluar,x="Editar")
    else:
        return redirect("/")


@app.route('/mainusuario/<int:id>', methods=["GET","POST"])
def usuario(id):
    datos=consultar_UsuarioFinal(id)
    formFinalUser = FormUsuarioFinal()
    if request.method == 'POST':
        year = request.form['anoEvaluacion']
        month = request.form['mesEvaluacion']
        evaluacion = consultar_evaluacion(year,month,id)
        if evaluacion is None:
            formFinalUser.anoEvaluacion.default=year
            formFinalUser.mesEvaluacion.default=month
            formFinalUser.puntaje.data=""
            formFinalUser.retroalimentacion.data=""
            error = "El Usuario no tiene evaluacion en el mes: "+month+" y el año: "+year
            flash( error )
            return render_template('mainusuario.html', titulo="main usuario", id=id, form=formFinalUser,usuario=datos,evaluacion="")
        else:
            formFinalUser.anoEvaluacion.default=year
            formFinalUser.mesEvaluacion.default=month
            formFinalUser.retroalimentacion.data=evaluacion[8]
            return render_template('mainusuario.html', titulo="main usuario", id=id, form=formFinalUser,usuario=datos,evaluacion=evaluacion)
    else:
        if session["usuario"]!="unknown" and session["rol"]!=0:
            return render_template('mainusuario.html', titulo="main usuario", id=id, form=formFinalUser,usuario=datos,evaluacion="")
        else:
            return redirect("/")


@app.route('/login', methods=["GET","POST"])
def login():
    formlogin = FormLogin()
    formFinalUser = FormUsuarioFinal()
    if request.method == 'POST':
        username = request.form['username']
        password = request.form['password']
        usuario = verificar_usuario(username,password)
        
        if usuario is None:
            error = "Usuario o contraseña inválidos"
            flash( error )
            return render_template('login.html', titulo="login", form=formlogin)
        else:
            persona=consultar_persona(usuario[4])
            session.clear()
            session["usuario"] = (persona[3]+", "+persona[2]).upper()
            session["rol"] = usuario[2]
            id = str(usuario[4])
            if session["rol"]=="usuario":
                return redirect("/mainusuario/"+id )
            else:    
                return redirect("/mainadmin")
    return render_template('login.html', titulo="login", form=formlogin)


@app.route("/logout")
def logout():
  session.clear()
  session["usuario"] = "unknown"
  session["rol"] = 0
  return redirect("/")


    


