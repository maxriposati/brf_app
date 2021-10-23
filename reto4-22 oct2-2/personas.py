
from logging import debug
from db import get_db,close_db
from sqlite3 import Error

def consultar_persona(id):
    db=get_db()
    try:
        cursor = db.cursor()
        strsql ="select * FROM persons where id= ?"
        cursor.execute(strsql, [id])
        persona = cursor.fetchone()
        return persona
    except Error:
        close_db()
    close_db()
    
def consultar_persona_contrato(id):
    db=get_db()
    try:
        cursor = db.cursor()
        strsql ="select * from persons join contracts on persons.id=contracts.idPerson where persons.id= ?"
        cursor.execute(strsql, [id])
        persona = cursor.fetchone()
        return persona
    except Error:
        close_db()
    close_db()

def verificar_persona(document): #Para verificar existencia en la tabla persons antes de crearlo
    db=get_db()
    try:
        cursor = db.cursor()
        strsql ="select * FROM persons where document=?"
        cursor.execute(strsql, [document])
        persona = cursor.fetchone() #trae resultado
        return persona
        
    except Error:
        close_db()
    close_db()

def insertar_persona(documento,nombre,apellidos,tipo_genero,fechaNacimiento,ciudadNacimiento,telefono,direccion,ciudadResidencia,email):
    db=get_db()
    try:
        cursor = db.cursor()
        strsql = "insert into persons (document, name, surname, gender, dateBirth, cityBirth, phone, address, cityResidence,email) VALUES(?,?,?,?,?,?,?,?,?,?)"
        cursor.execute(strsql, [documento,nombre,apellidos,tipo_genero,fechaNacimiento,ciudadNacimiento,telefono,direccion,ciudadResidencia,email])
        db.commit()
        valor = True
        close_db()
        return valor

    except Error:
        valor = False
    close_db()
    return valor
    
def verificar_idPersona(document): #Para verificar existencia en la tabla persons antes de crearlo
    db=get_db()
    try:
        cursor = db.cursor()
        strsql ="select id FROM persons where document=?"
        cursor.execute(strsql, [document])
        idPersona = cursor.fetchone() #trae resultado
        return idPersona
        
        
    except Error:
        close_db()
    close_db()
    
def lista_personas_contratos():
    db=get_db()
    try:
        cursor = db.cursor()
        strsql ="select id, name, charge, dependence, admissionDate, leaveDate from contracts join persons on contracts.idPerson=persons.id  "
        cursor.execute(strsql)
        personas = cursor.fetchall()     
    except Error:
        close_db()
    close_db()
    return personas

def eliminar_persona(id):
    db=get_db()
    try:
        cursor = db.cursor()
        strsql = "delete from persons where id = ?"
        cursor.execute(strsql, [id])
        db.commit()
        valor = True
        close_db()
        return valor
    except Error:
        valor = False
    close_db()
    return valor

def consultar_UsuarioFinal(id):
    db=get_db()
    try:
        cursor = db.cursor()
        strsql ="select document, name, surname, gender, dateBirth, cityBirth, phone, address, cityResidence, email, typeContract, charge , admissionDate, leaveDate, dependence, salary, availability from users join persons on users.idPerson=persons.id join contracts on contracts.idPerson=persons.id  where id = ?"
        cursor.execute(strsql, [id])
        persona = cursor.fetchone()
        return persona
    except Error:
        close_db()
    close_db()

def editar_persona(documento,nombre,apellidos,tipo_genero,fechaNacimiento,ciudadNacimiento,telefono,direccion,ciudadResidencia,email,id):
    db=get_db()
    try:
        cursor = db.cursor()
        strsql ="update persons SET document=?, name=?, surname=?, gender=?, dateBirth=?, cityBirth=?, phone=?, address=?, cityResidence=?,email=? where id=?"
        cursor.execute(strsql,[documento,nombre,apellidos,tipo_genero,fechaNacimiento,ciudadNacimiento,telefono,direccion,ciudadResidencia,email,id])
        db.commit()
        valor=True
        close_db()
        return valor
    except Error:
        valor=False
        close_db()
    close_db()
    return valor
