// CONTACTO

document.addEventListener("DOMContentLoaded", function() {
    document.getElementById("contact_form").addEventListener('submit', validar_formulario); 
});

function validar_formulario(evento){
    evento.preventDefault();
    var nombre = document.getElementById('author').value;
    var mail = document.getElementById('email').value;
    var asunto = document.getElementById('subject').value;
    var mensaje = document.getElementById('mensaje').value;

    if(nombre.length == 0) {
        alert('No has escrito el Nombre. Es un campo obligatorio..!');
        return;
    }

    if(mail.length == 0) {
        alert('No has escrito el Correo. Es un campo obligatorio..!');
        return;
    }

    if(asunto.length == 0) {
        alert('No has escrito el Asunto. Es un campo obligatorio..!');
        return;
    }

    if(mensaje.length == 0) {
        alert('No has escrito ningún Mensaje para Contactarte. Es un campo obligatorio..!');
        return;
    }

    re=/^\w+([\.-]?\w+)@\w+([\.-]?\w+)(\.\w{2,3})+$/
	if(!re.exec(mail)){
		alert('Debe ingresar un Email válido!');
        mail.focus();
        return false; 
	}
    alert('El mensaje se ha enviado Exitosamente..!');
    document.getElementById('author').value=""
    document.getElementById('email').value=""
    document.getElementById('subject').value=""
    document.getElementById('mensaje').value=""
    this.reset();
    
}
// LOGIN
function validar_login() {
    var formulario = document.getElementById("formLogin");
    var user = document.getElementById('username');
    var password = document.getElementById('password');
    var politica = document.getElementById('politicas');
  
    if(user.value ==""){
        alert("El campo Nombre está vacío");
        user.focus();
        return false;
    }else{
        if(password.value==""){
            alert("El campo Password está vacío");
            password.focus();
            return false;
        }else{
            if(politica.checked==false){
                alert(" Por favor Marque la opción de políticas")
                return false;
            }else{
                alert("Enviando el formulario");
                formulario.submit();
                return true;
            }

        }
    }
  }

/*document.addEventListener("DOMContentLoaded", function() {
    var formulario = document.getElementById("formLogin");
    formulario.addEventListener('submit', validar_login); 
});
function validar_login(evento){
    evento.preventDefault();
    var formulario = document.getElementById("formLogin");
    var user = document.getElementById('username');
    var password = document.getElementById('password');
    var politaca = document.getElementById('politicas');

    if(user.value ==""){
        alert("El campo Nombre está vacío");
        user.focus();
        return false;
    }
    else{

       if(password.value==""){
           alert("El campo Password está vacío");
           password.focus();
           return false;
       }
       else{
            if(politaca.checked==false){
                alert(" Por favor Marque la opción de políticas")
                return false;
            }
          /* else if(user.value == "admin" ){
               window.location.href='/mainadmin';
               alert("Bienvenido Usuario Administrador..!");
               return true;
           }
           else if(user.value == "user"){
                window.location.href='/mainusuario/1';
                alert("Bienvenido User..!");
                return true;
           }

           else{ 
               //alert("Usuario no Registrado..!")
               //return false;
               formulario.submit();
               return true;
            }

       }
    }
}*/

//OLVIDO DE CONTRASENA
function validar_Olvido() {
    var formulario = document.getElementById("formRecuperarPass");
    var user =document.getElementById('username');
    if(user.value ==""){
        alert("El campo usuario está vacío");
        user.focus();
        return false;
    }else{
        alert("Enviando para recuperación");
        formulario.submit();
        return true;
    }
  }

/*document.addEventListener("DOMContentLoaded", function() {
    document.getElementById("tooplate_content1").addEventListener('submit', validar_Olvido); 
});
function validar_Olvido(evento){
        evento.preventDefault();
        var user = document.getElementById('username');
        if(user.value=="admin"){
            alert("Password Restablecido..!")
            this.submit();
        }else{
            alert("Usuario NO registrado..!")
            return false;
        }
       
    }*/
    
//Eliminar
function eliminarUsuario(valor){
    val=confirm("¿Está seguro que desea Eliminar este Usuario ?")
    if (val) {
        window.location.href='/mainadmin/eliminar/'+valor;
        alert("Usuario Eliminado Exitosamente")
        return true   
    }else{
        return false
    }
    
}

//CREAR USUARIO

document.addEventListener("DOMContentLoaded", function() {
    document.getElementById("formcrearusuario").addEventListener('submit', crearUsuario); 
});
function crearUsuario(evento){
    
    evento.preventDefault();
    var documento = document.formcrearusuario.documento.value
    var nombre = document.formcrearusuario.nombre.value
    var apellidos = document.formcrearusuario.apellidos.value
    var tipo_genero = document.formcrearusuario.tipo_genero
    var fechaNacimiento = document.getElementById('documento')
    var ciudadNacimiento = document.getElementById('ciudadNacimiento').selectedIndex
    
    var user = document.getElementById('user').value
    var password = document.getElementById('password')
    var rol = document.getElementById('rol')
   
    var telefono = document.getElementById('telefono').value
    var direccion = document.getElementById('direccion').value
    var ciudadResidencia = document.getElementById('ciudadResidencia').selectedIndex
    var email = document.getElementById('email').value
    
    var tipoContrato = document.getElementById('tipoContrato').selectedIndex
    var cargo = document.getElementById('cargo').selectedIndex
    var fechaInicio = document.getElementById('fechaInicio').value
    var fechaFinalizacion = document.getElementById('documento')
    var dependencia = document.getElementById('dependencia').selectedIndex
    var salario = document.getElementById('salario').value
    var estado = document.formcrearusuario.estado
    
   if(isNaN(documento) || documento.length < 5){
       alert("Seleccione un Número de identidad correcto");
       return false;
   }

   if (/^\s+$/.test(nombre) || nombre.length==0){
       alert("Nombre incorreto")
       return false;
   }

   if (/^\s+$/.test(apellidos) || apellidos.length==0){
    alert("Apellidos incorrectos")
    return false
}

var seleccionado = false;
for(var i=0; i<tipo_genero.length; i++) {
  if(tipo_genero[i].checked) {
    seleccionado = true;
    break;
  }
}

if(!seleccionado) {
    alert("No ha seleccionado el Género")
  return false;
}

if(ciudadNacimiento == null || ciudadNacimiento ==0){
    alert(" Seleccione una Ciudad de Nacimiento")
    return false
}


if(user.length == 0) {
    alert("El campo Usuario está vacío")
    user.focus();
    return false;
}
if(password.value==""){
    alert("El campo Password está vacío");
    password.focus();
    return false;
}

if(email.length == 0) {
    alert('No ha escrito el Correo. Es un campo obligatorio..!');
    return false;
}


re=/^\w+([\.-]?\w+)@\w+([\.-]?\w+)(\.\w{2,3})+$/
if(!re.exec(email)){
    alert('Debe ingresar un Email válido!');
    email.focus();
    return false; 
}

if( !(/^\d{9}$/.test(telefono)) ) {
    alert("Ingresa un Teléfono válido")
    return false;
  }

if(direccion==""){
    alert("El campo dirección está vacío");
    direccion.focus();
    return false;
}

if(ciudadResidencia == null || ciudadResidencia ==0){
    alert(" Seleccione una Ciudad de Residencia")
    return false;
}

if(tipoContrato == null || tipoContrato ==0){
    alert(" Seleccione un Tipo de Contrato")
    return false;
}

if(cargo == null || cargo==0){
    alert(" Seleccione un Cargo")
    return false;
}

if(dependencia == null || dependencia ==0){
    alert(" Seleccione una Dependencia")
    return false;
}

if(isNaN(salario) || salario.length < 5){
    alert("Seleccione el Salario");
    return false;
}

var seleccionado = false;
for(var i=0; i<estado.length; i++) {
  if(estado[i].checked) {
    seleccionado = true;
    break;
  }
}

if(!seleccionado) {
    alert("No ha seleccionado Estado del Contrato")
  return false;
}

if(fechaInicio==""){
    alert("Seleccione una Fecha de inicio");
    fechaInicio.focus();
    return false;
}

function validar_fecha(){
    fechaHoy=""
    if(fechaInicio < fechaHoy ){
        alert("la fecha de inicio no puede ser anterior a la fecha actual");
        return false
    }
    if(fechaFinalizacion <= fechaHoy || fechaFinalizacion <= fechaInicio){
        alert("la fecha de finalizacion no puede ser igual a la fecha de inicio o anterior a la fecha actual");
        return false
    }
}

function validar_nac(){
    fechaHoy=""
    if(fechaNacimiento >=  fechaHoy ){
        alert("la fecha de inicio no puede ser anterior a la fecha actual");
        return false
    }
   //comparar la fecha actual menos 18 annos 
}


///////////////////////////////
let date = new Date()

let day = date.getDate()
let month = date.getMonth() + 1
let year = date.getFullYear()

if(month < 10){
  console.log(`${day}-0${month}-${year}`)
}else{
  console.log(`${day}-${month}-${year}`)
}


/////////////////////

val=confirm("¿Está Seguro que desea Crear el Usuario?")
if(val){
    this.submit();
    //window.location.href='/mainadmin';
    alert("Usuario creado..!");
    return true
}else{
    return false
}


}

// EVALUAR

/*
document.addEventListener("DOMContentLoaded", function() {
    document.getElementById("formevaluar").addEventListener('submit', Evaluar); 
});

function Evaluar(evento){
    evento.preventDefault();
    var fechaEvaluacion = document.getElementById('fechaEvaluacion').value
    
    var documento = document.getElementById('documento').value
    var nombre = document.getElementById('nombre').value
    var apellidos = document.getElementById('documento').value
    
    var puntaje = document.getElementById('puntaje').value
    var retroalimentacion = document.getElementById('retroalimentacion').value
    
    var conocimiento = document.getElementById('conocimiento')
    var actitud = document.getElementById('actitud')
    var habilidad = document.getElementById('hablidad')
    


    if(fechaEvaluacion==""){
        alert("Seleccione una Fecha de Evaluación");
        fechaEvaluacion.focus();
        return false;
    }

    if(isNaN(documento) || documento.length < 5){
        alert("Capture un Número de documento válido");
        return false;
    }
 
    if (/^\s+$/.test(nombre) || nombre.length==0){
        alert("Capture caracteres válidos en el campo Nombre ");
        return false;
    }
 
    if (/^\s+$/.test(apellidos) || apellidos.length==0){
     alert("Capture caracteres válidos en el campo Apellidos");
     return false;
    }

    if(isNaN(puntaje) || puntaje.length == 0){
        alert("Capture Puntaje, es un campo requerido en la Evaluación");
        puntaje.focus();
        return false;
    }
    if(retroalimentacion==""){
        alert("Capture Retroalimentación final, es un campo requerido en la Evaluación");
        retroalimentacion.focus();
        return false;
    }

    val=confirm("¿Está seguro que desea realizar esta evaluación?")
    if(val){
        window.location.href='/mainadmin';
        alert("Usuario evaluado..!");
        return true
    }else{
        return false
    }
  
    }
*/

function puntaje_final(){
    
    var conocimiento = document.getElementById('conocimiento').value
    var actitud = document.getElementById('actitud').value
    var habilidad = document.getElementById('habilidad').value
    var puntaje = document.getElementById('puntaje')
    var suma=(parseInt(conocimiento) + parseInt(actitud)+parseInt(habilidad))/3
    
    puntaje.value=suma.toFixed(2)

}
//EDITAR USUARIOS

/*

document.addEventListener("DOMContentLoaded", function() {
    document.getElementById("formeditarusuario" ).addEventListener('submit', EditarUsuario); 
});
function EditarUsuario(evento){
    evento.preventDefault();
    var formulario = document.getElementById("formeditarusuario");
    var documento = document.formeditarusuario.documento.value
    var nombre = document.formeditarusuario.nombre.value
    var apellidos = document.formeditarusuario.apellidos.value
    var tipo_genero = document.formeditarusuario.tipo_genero
    var fechaNacimiento = document.getElementById('documento')
    var ciudadNacimiento = document.getElementById('ciudadNacimiento').selectedIndex
    

    var telefono = document.getElementById('telefono').value
    var direccion = document.getElementById('direccion').value
    var ciudadResidencia = document.getElementById('ciudadResidencia').selectedIndex
    var email = document.getElementById('email').value
    
    var tipoContrato = document.getElementById('tipoContrato').selectedIndex
    var cargo = document.getElementById('cargo').selectedIndex
    var fechaInicio = document.getElementById('fechaInicio').value
    var fechaFinalizacion = document.getElementById('documento')
    var dependencia = document.getElementById('dependencia').selectedIndex
    var salario = document.getElementById('salario').value
    var estado = document.formeditarusuario.estado
    
   if(isNaN(documento) || documento.length < 5){
       alert("Seleccione un número de identidad correcto");
       return false;
   }

   if (/^\s+$/.test(nombre) || nombre.length==0){
       alert("Nombre incorrecto")
       return false;
   }

   if (/^\s+$/.test(apellidos) || apellidos.length==0){
    alert("Apellidos incorrectos")
    return false
}

var seleccionado = false;
for(var i=0; i<tipo_genero.length; i++) {
  if(tipo_genero[i].checked) {
    seleccionado = true;
    break;
  }
}

if(!seleccionado) {
    alert("No ha seleccionado Género")
  return false;
}

if(ciudadNacimiento == null || ciudadNacimiento ==0){
    alert(" Seleccione una Ciudad de Nacimiento")
    return false
}



if(email.length == 0) {
    alert('No ha escrito el Correo. Es un campo obligatorio..!');
    return;
}


re=/^\w+([\.-]?\w+)@\w+([\.-]?\w+)(\.\w{2,3})+$/
if(!re.exec(email)){
    alert('Debe ingresar un Email válido!');
    email.focus();
    return false; 
}

if( !(/^\d{9}$/.test(telefono)) ) {
    alert("Ingrese un Teléfono válido")
    return false;
  }

if(direccion==""){
    alert("El campo Dirección está vacío");
    direccion.focus();
    return false;
}

if(ciudadResidencia == null || ciudadResidencia ==0){
    alert(" Seleccione Ciudad de Residencia")
    return false;
}

if(tipoContrato == null || tipoContrato ==0){
    alert(" Seleccione Tipo de Contrato")
    return false;
}

if(cargo == null || cargo==0){
    alert(" Seleccione un Cargo")
    return false;
}

if(dependencia == null || dependencia ==0){
    alert(" Seleccione una Dependencia")
    return false;
}

if(isNaN(salario) || salario.length < 5){
    alert("Seleccione el Salario");
    return false;
}

var seleccionado = false;
for(var i=0; i<estado.length; i++) {
  if(estado[i].checked) {
    seleccionado = true;
    break;
  }
}

if(!seleccionado) {
    alert("No ha seleccionado Estado del contrato")
  return false;
}

if(fechaInicio==""){
    alert("Seleccione fecha de inicio");
    fechaInicio.focus();
    return false;
}

val=confirm("¿Está seguro que desea Editar el usuario?")
if(val){
    //window.location.href='/mainadmin';
    alert("Usuario editado..!");
    return true
}else{
    return false
}

} */