from db import get_db,close_db
from sqlite3 import Error

def insertar_contrato(idPersona,cargo,fechaInicio,fechaFinalizacion,tipoContrato,dependencia,salario,estado):
    db=get_db()
    try:
        cursor = db.cursor()
        strsql = "insert into contracts (idPerson,charge,admissionDate,leaveDate,typeContract,dependence,salary,availability) VALUES(?,?,?,?,?,?,?,?)"
        cursor.execute(strsql, [idPersona,cargo,fechaInicio,fechaFinalizacion,tipoContrato,dependencia,salario,estado])
        db.commit()
        valor = True
        close_db()
        return valor

    except Error:
        valor = False
    close_db()
    return valor

def eliminar_contrato_persona(id):
    db=get_db()
    try:
        cursor = db.cursor()
        strsql = "delete from contracts where idPerson = ?"
        cursor.execute(strsql, [id])
        db.commit()
        valor = True
        close_db()
        return valor
    except Error:
        valor = False
    close_db()
    return valor