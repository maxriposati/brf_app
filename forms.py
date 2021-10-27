from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, BooleanField, SubmitField, TextAreaField, RadioField, SelectField, HiddenField
from wtforms.validators import DataRequired,Required
from wtforms.fields.html5 import EmailField, DateField, DecimalField,IntegerRangeField
import pandas as pd
from sodapy import Socrata 


# Consultando la API del portal de datos abiertos de Colombia
def ciudades():
    client = Socrata("www.datos.gov.co", None)
    result = client.get("xdk5-pm3f", limit = 2000)
    df = pd.DataFrame.from_records(result)
    cities = list(df["municipio"])
    cities.append("        ---")
    return sorted(cities)


ciudades_op=ciudades()
contrato_op = [('      ---', '      ---'), ('Fijo', 'Fijo'), ('Indefinido', 'Indefinido'), ('Prestación de Servicios', 'Prestación de Servicios'), ('Aprendizaje', 'Aprendizaje'), ('Obra o Labor', 'Obra o Labor')]
cargo_op = [('      ---', '      ---'), ('Directivo', 'Directivo'), ('Jefatura', 'Jefatura'), ('Operativo', 'Operativo'), ('Asistente', 'Asistente'), ('Auxiliar', 'Auxiliar')]
dependencia_op = [('      ---', '      ---'), ('Mercadeo', 'Mercadeo'), ('Comercial', 'Comercial'), ('Talento Humano', 'Talento Humano'), ('Producción', 'Producción'), ('Financiero', 'Financiero'), ('Almacén', 'Almacén')]
roles = [('      ---', '      ---'), ('usuario', 'Usuario'), ('administrador', 'Administrador'), ('superAdministrador', 'Super Administrador')]
months = [('      ---', '      ---'), ('Enero', 'Enero'), ('Febrero', 'Febrero'), ('Marzo', 'Marzo'), ('Abril', 'Abril'), ('Mayo', 'Mayo'),('Junio', 'Junio'),('Julio', 'Julio'),('Agosto', 'Agosto'),('Septiembre', 'Septiembre'),('Octubre', 'Octubre'), ('Noviembre', 'Noviembre'),('Diciembre', 'Diciembre')]
years = [('      ---', '      ---'),(2021, 2021), (2022, 2022), (2023, 2023)]

class FormContacto(FlaskForm):
    author = StringField('Nombre: ', validators=[DataRequired(message='No dejar vacío,completar')])
    email = StringField('Email: ', validators=[DataRequired(message='No dejar vacío,completar')])
    subject = StringField('Asunto: ', validators=[DataRequired(message='No dejar vacío,completar')])
    mensaje = TextAreaField('Mensaje: ')
    enviar = SubmitField('Enviar')
    
class FormLogin(FlaskForm):
    username = StringField('Usuario: ', validators=[DataRequired(message='No dejar vacío,completar')])
    password = PasswordField('Contraseña: ', validators=[DataRequired(message='No dejar vacío,completar')])
    politicas = BooleanField('Declaro haber leído y acepto las políticas de privacidad y protección de datos', validators=[Required(message='Debe seleccionar')])
    submit = SubmitField('Ingresar')
    
class FormRestablecer(FlaskForm):
    username = StringField('Usuario: ', validators=[DataRequired(message='No dejar vacío,completar')])
    restablecer = SubmitField('    Restablecer')
    
class FormRecovery(FlaskForm):
    password = StringField('Nueva Contraseña: ', validators=[DataRequired(message='No dejar vacío,completar')])
    repassword = StringField('Repita Contraseña: ', validators=[DataRequired(message='No dejar vacío,completar')])
    guardar = SubmitField('    Guardar')
    
class FormUsuario(FlaskForm):
    #datos personales
    documento = StringField('Cédula: ', validators=[DataRequired(message='No dejar vacío,completar')])
    nombre = StringField('Nombre: ', validators=[DataRequired(message='No dejar vacío,completar')])
    apellidos = StringField('Apellidos: ', validators=[DataRequired(message='No dejar vacío,completar')])
    tipo_genero = RadioField('Genero:', choices=[('M','M'),('F','F')])
    fechaNacimiento = DateField('Fecha Nacimiento:')
    ciudadNacimiento = SelectField(u'Ciudad de Nacimiento:', choices=ciudades_op)
    #acceso
    user = StringField('Usuario: ', validators=[DataRequired(message='No dejar vacío,completar')])
    password = PasswordField('Contraseña: ', validators=[DataRequired(message='No dejar vacío,completar')])
    rol = SelectField(u'rol:', choices=roles)
    #datos de contacto
    telefono = StringField('Telefono: ', validators=[DataRequired(message='No dejar vacío,completar')])
    direccion = StringField('Dirección: ', validators=[DataRequired(message='No dejar vacío,completar')])
    ciudadResidencia = SelectField(u'Ciudad de Residencia:', choices=ciudades_op, default="        ---")
    email = EmailField('E-mail: ')
    #datos de contrato
    tipoContrato = SelectField(u'Tipo de Contrato:', choices=contrato_op, default="        ---")
    cargo = SelectField(u'Cargo:', choices=cargo_op, default="        ---")
    fechaInicio = DateField('Fecha Inicio:')
    fechaFinalizacion = DateField('Fecha Finalización:')
    dependencia = SelectField(u'Dependencia:', choices=dependencia_op, default="        ---")
    salario = DecimalField('Salario: ')
    estado = RadioField('Estado Contrato:', choices=[('activo','Activo'),('inactivo','Inactivo')])
    
    #Acciones
    guardar = SubmitField('  Guardar')
    editar = SubmitField('  Editar')
    
class FormRetroalimentacion(FlaskForm):
    #fecha
    anoEvaluacion = SelectField(u'Año:', choices=years, default="        ---")
    mesEvaluacion = SelectField(u'Mes:', choices=months, default="        ---")
    #empleado
    documento = StringField('Cédula: ')
    nombre = StringField('Nombre: ')
    apellidos = StringField('Apellidos: ')
    #retroalimentacion
    puntaje = DecimalField('Puntaje Final: ')
    retroalimentacion = TextAreaField('Comentarios: ', validators=[DataRequired(message='No dejar vacío,completar')])
    #calificacion
    conocimiento = IntegerRangeField('Conocimiento: ')
    actitud = IntegerRangeField('Actitud: ')
    habilidad = IntegerRangeField('Habilidad: ')
    #Acciones
    guardar = SubmitField('  Guardar')
    editar = SubmitField('  Editar')
        
class FormUsuarioFinal(FlaskForm):
    #datos personales
    documento = StringField('Cédula: ')
    nombre = StringField('Nombre: ')
    apellidos = StringField('Apellidos: ')
    tipo_genero = StringField('Genero')
    fechaNacimiento = StringField('Fecha Nacimiento:')
    ciudadNacimiento = StringField('Ciudad de Nacimiento:')
    #datos de contacto
    telefono = StringField('Telefono: ')
    direccion = StringField('Dirección: ')
    ciudadResidencia = StringField('Ciudad de Residencia: ')
    email = StringField('E-mail: ')
    #datos de contrato
    contrato = SelectField(u'Seleccionar Contrato:', choices=contrato_op)
    tipoContrato = StringField('Tipo de Contrato:')
    cargo = StringField('Cargo:')
    fechaInicio = StringField('Fecha Inicio:')
    fechaFinalizacion = StringField('Fecha Finalización:')
    dependencia = StringField('Dependencia:')
    salario = StringField('Salario: ')
    estado = StringField('Estado Contrato:')
    #retroalimentacion
    anoEvaluacion = SelectField(u'Año:', choices=years, default="        ---")
    mesEvaluacion = SelectField(u'Mes:', choices=months, default="        ---")
    puntaje = StringField('Puntaje Final: ')
    retroalimentacion = TextAreaField('Comentarios: ')
    
    ver = SubmitField('  Consultar')
