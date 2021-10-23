from db import get_db,close_db
from sqlite3 import Error

def insertar_evaluacion(idPersona,year,month,conocimiento,actitud,habilidad,puntaje,feedback):
    db=get_db()
    try:
        cursor = db.cursor()
        strsql = "insert into performances (idPerson,year,month,knowledge,acttitude,skillfulness,finalScore,feedback) VALUES(?,?,?,?,?,?,?,?)"
        cursor.execute(strsql, [idPersona,year,month,conocimiento,actitud,habilidad,puntaje,feedback])
        db.commit()
        valor = True
        close_db()
        return valor

    except Error:
        valor = False
    close_db()
    return valor

def consultar_evaluacion(year,month,id):
    db=get_db()
    try:
        cursor = db.cursor()
        strsql ="select * FROM performances where year=? and month=? and idPerson= ?"
        cursor.execute(strsql, [year,month,id])
        persona = cursor.fetchone()
        return persona
    except Error:
        close_db()
    close_db()

def eliminar_evaluacion(id):
    db=get_db()
    try:
        cursor = db.cursor()
        strsql = "delete from performances where idPerson = ?"
        cursor.execute(strsql, [id])
        db.commit()
        valor = True
        close_db()
        return valor
    except Error:
        valor = False
    close_db()
    return valor

