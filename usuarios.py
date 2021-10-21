from werkzeug.security import generate_password_hash, check_password_hash
from db import get_db,close_db
from sqlite3 import Error

def lista_usuarios():
    db=get_db()
    try:
        cursor = db.cursor()
        strsql ="select id, name, surname, document, charge, dependence, admissionDate, leaveDate from users join persons on users.idPerson=persons.id join contracts on persons.id=contracts.idPerson where users.rol='usuario'"
        cursor.execute(strsql)
        usuarios = cursor.fetchall()
        return usuarios
    except Error:
        close_db()
    close_db()
    

def lista_usuarios_superadmin():
    db=get_db()
    try:
        cursor = db.cursor()
        strsql ="select id, name, surname, document, charge, dependence, admissionDate, leaveDate from users join persons on users.idPerson=persons.id join contracts on persons.id=contracts.idPerson"
        cursor.execute(strsql)
        usuarios = cursor.fetchall()
        
    except Error:
        close_db()
    close_db()
    return usuarios

def consultar_usuario(id):
    db=get_db()
    try:
        cursor = db.cursor()
        strsql ="select * FROM users where idUser= ?"
        cursor.execute(strsql, [id])
        usuario = cursor.fetchone()
        return usuario
    except Error:
        close_db()
    close_db()
    
def consulta_recovery(correo,doc):
    db=get_db()
    try:
        cursor = db.cursor()
        strsql ="select idUser from users join persons on users.idPerson=persons.id where persons.email=? and persons.document=?"
        cursor.execute(strsql, [correo,doc])
        usuario = cursor.fetchone()
        return usuario
    except Error:
        close_db()
    close_db()
    

def verificar_usuario(user,password):
    db=get_db()
    try:
        cursor = db.cursor()
        strsql ="select * FROM users where user=?"
        cursor.execute(strsql, [user])
        usuario = cursor.fetchone()
        if usuario is None:
            return usuario
        else:
            checked=check_password_hash(usuario[1],password)
            if checked:
                return usuario
    except Error:
        close_db()
    close_db()
    
    

def insertar_usuario(password,rol,user,idPersona):
    db=get_db()
    try:
        password=generate_password_hash(password)
        cursor = db.cursor()
        strsql = "insert into users (password, rol, user, idPerson) values(?, ?, ?, ?)"
        cursor.execute(strsql, [password, rol ,user,idPersona])
        db.commit()
        valor = True
        close_db()
        return valor

    except Error:
        valor = False
    close_db()
    return valor

def editar_usuario(id,rol,usuario,persona,contrasena):
    db=get_db()
    try:
        password=generate_password_hash(contrasena)
        cursor = db.cursor()
        strsql = "update users set rol = ?, user = ?, password = ?, idPerson = ? where idUser= ?"
        cursor.execute(strsql, [rol, usuario, password, persona, id])
        db.commit()
        valor = True
        close_db()
        return valor
    except Error:
        valor = False
    close_db()
    return valor

def reestablecer_pass(id,contrasena):
    db=get_db()
    try:
        password=generate_password_hash(contrasena)
        cursor = db.cursor()
        strsql = "update users set password = ? where idUser= ?"
        cursor.execute(strsql, [password, id])
        db.commit()
        valor = True
        close_db()
        return valor
    except Error:
        valor = False
    close_db()
    return valor

def eliminar_usuario(id):
    db=get_db()
    try:
        cursor = db.cursor()
        strsql = "delete from users where idUser = ?"
        cursor.execute(strsql, [id])
        db.commit()
        valor = True
        close_db()
        return valor
    except Error:
        valor = False
    close_db()
    return valor

def eliminar_usuario_persona(id):
    db=get_db()
    try:
        cursor = db.cursor()
        strsql = "delete from users where idPerson = ?"
        cursor.execute(strsql, [id])
        db.commit()
        valor = True
        close_db()
        return valor
    except Error:
        valor = False
    close_db()
    return valor

def obtener_correo(username):
    db=get_db()
    try:
        cursor = db.cursor()
        strsql ="SELECT email,document FROM users JOIN persons on users.idPerson=persons.id WHERE users.user=?"
        cursor.execute(strsql, [username])
        correo = cursor.fetchone() #trae resultado
        return correo   
    except Error:
        close_db()
    close_db()