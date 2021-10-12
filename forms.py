from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, BooleanField, SubmitField, TextAreaField, RadioField, SelectField
from wtforms.validators import DataRequired,Required
from wtforms.fields.html5 import EmailField, DateField, DecimalField,IntegerRangeField
from wtforms.widgets import ListWidget, RadioInput
opciones = [('1', 'opcion 1'), ('2', 'opcion 2'), ('3', 'opcion 3'), ('4', 'opcion 4'), ('5', 'opcion 5')]
roles = [('usuario', 'Usuario'), ('administrador', 'Administrador'), ('superAdministrador', 'Super Administrador')]

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
    
class FormUsuario(FlaskForm):
    #datos personales
    documento = StringField('Cédula: ', validators=[DataRequired(message='No dejar vacío,completar')])
    nombre = StringField('Nombre: ', validators=[DataRequired(message='No dejar vacío,completar')])
    apellidos = StringField('Apellidos: ', validators=[DataRequired(message='No dejar vacío,completar')])
    tipo_genero = RadioField('Genero:', choices=[('Masculino','M'),('Femenino','F')], option_widget=None)
    fechaNacimiento = DateField('Fecha Nacimiento:')
    ciudadNacimiento = SelectField(u'Ciudad de Nacimiento:', choices=opciones)
    #acceso
    user = StringField('Usuario: ', validators=[DataRequired(message='No dejar vacío,completar')])
    password = PasswordField('Contraseña: ', validators=[DataRequired(message='No dejar vacío,completar')])
    rol = SelectField(u'rol:', choices=roles)
    #datos de contacto
    telefono = StringField('Telefono: ', validators=[DataRequired(message='No dejar vacío,completar')])
    direccion = StringField('Dirección: ', validators=[DataRequired(message='No dejar vacío,completar')])
    ciudadResidencia = SelectField(u'Ciudad de Residencia:', choices=opciones)
    email = EmailField('E-mail: ')
    #datos de contrato
    tipoContrato = SelectField(u'Tipo de Contrato:', choices=opciones)
    cargo = SelectField(u'Cargo:', choices=opciones)
    fechaInicio = DateField('Fecha Inicio:')
    fechaFinalizacion = DateField('Fecha Finalización:')
    dependencia = SelectField(u'Dependencia:', choices=opciones)
    salario = DecimalField('Salario: ')
    estado = RadioField('Estado Contrato:', choices=[('activo','Activo'),('inactivo','Inactivo')])
    
    #Acciones
    guardar = SubmitField('  Guardar')
    editar = SubmitField('  Editar')
    
class FormRetroalimentacion(FlaskForm):
    #fecha
    fechaEvaluacion = DateField('Fecha de Evaluación:')
    #empleado
    documento = StringField('Cédula: ')
    nombre = StringField('Nombre: ')
    apellidos = StringField('Apellidos: ')
    #retroalimentacion
    puntaje = DecimalField('Puntaje Final: ')
    retroalimentacion = TextAreaField('Comentarios: ')
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
    contrato = SelectField(u'Seleccionar Contrato:', choices=opciones)
    tipoContrato = StringField('Tipo de Contrato:')
    cargo = StringField('Cargo:')
    fechaInicio = StringField('Fecha Inicio:')
    fechaFinalizacion = StringField('Fecha Finalización:')
    dependencia = StringField('Dependencia:')
    salario = StringField('Salario: ')
    estado = StringField('Estado Contrato:')
    #retroalimentacion
    puntaje = StringField('Puntaje Final: ')
    retroalimentacion = TextAreaField('Comentarios: ')
