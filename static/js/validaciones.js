// validacion CONTACTO

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
// Validacion LOGIN
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
                //alert("Enviando el formulario");
                formulario.submit();
                return true;
            }
        }
    }
  }

//OLVIDO DE CONTRASENA
function validar_Olvido() {
    var formulario = document.getElementById("formRecuperarPass");
    var user =document.getElementById('username');
    if(user.value ==""){
        alert("El campo usuario está vacío");
        user.focus();
        return false;
    }else{
        alert("Enviando informacion a su correo");
        formulario.submit();
        return true;
    }
  }

//Recuperacion de contraseña
function validar_recovery(){
    var formulario = document.getElementById("formRecovery");
    var password =document.getElementById('password');
    var repassword =document.getElementById('repassword');
    if(password.value != repassword.value){
        alert("Las contraseñas no son iguales");
        password.value=""
        repassword.value=""
        password.focus();
        return false;
    }else{
        alert("Contraseña Recuperada");
        formulario.submit();
        return true;
    }
}
    
//Eliminar usuario
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
function validar_crear_usuario() {
    var formulario = document.getElementById("formcrearusuario");
    
    //datos personales
    var documento = document.getElementById('documento');
    var nombre = document.getElementById('nombre');
    var apellidos = document.getElementById('apellidos');
    var tipo_genero = document.getElementsByName('tipo_genero');
    var fechaNacimiento = document.getElementById('fechaNacimiento');
    var ciudadNacimiento = document.getElementById('ciudadNacimiento');
    //datos de acceso 
    var user = document.getElementById('user');
    var password = document.getElementById('password');
    var rol = document.getElementById('rol');
    //datos de contacto
    var telefono = document.getElementById('telefono');
    var direccion = document.getElementById('direccion');
    var ciudadResidencia = document.getElementById('ciudadResidencia');
    var email = document.getElementById('email');
    //datos de contrato
    var tipoContrato = document.getElementById('tipoContrato').selectedIndex;
    var cargo = document.getElementById('cargo').selectedIndex;
    var fechaInicio = document.getElementById('fechaInicio');
    var fechaFinalizacion = document.getElementById('fechaFinalizacion');
    var dependencia = document.getElementById('dependencia').selectedIndex;
    var salario = document.getElementById('salario');
    var estado = document.getElementsByName('estado');

    if(!isNaN(documento) || documento.length < 5||!(/^\d{5,}$/.test(documento.value))){
        alert("Seleccione un Número de identidad correcto");
        documento.focus();
        return false;
    }else{
        if (/^\s+$/.test(nombre.value) || nombre.length <= 2){
            alert("Nombre Incorrecto");
            nombre.focus();
            return false;
        }else{
            if (/^\s+$/.test(apellidos.value) || apellidos.length <=2 ){
                alert("Apellidos incorrectos");
                apellidos.focus();
                return false;
            }else{
                var selec = false;
                for(var i=0; i<tipo_genero.length; i++) {
                    if(tipo_genero[i].checked) {
                        selec = true;
                        break;
                    }
                }
                if(!selec) {
                    alert("No ha seleccionado el Género");
                    return false;
                }else{
                    if(fechaNacimiento.value==""||!validar_nac(fechaNacimiento.value)){
                        alert("Seleccione una Fecha de Nacimiento Correcta");
                        fechaNacimiento.focus();
                        return false;
                    }else{
                        if(ciudadNacimiento.selectedIndex == null || ciudadNacimiento.selectedIndex == 0 || ciudadNacimiento.value == "        ---"){
                            alert(" Seleccione una Ciudad de Nacimiento");
                            return false;
                        }else{
                            if(user.value==""||user.length <=2){
                                alert("El usuario está vacío");
                                direccion.focus();
                                return false;
                            }else{
                                if(password.value==""||password.length <=2){
                                    alert("El password está vacío");
                                    direccion.focus();
                                    return false;
                                }else{
                                    if(rol.selectedIndex == null || rol.selectedIndex == 0 || rol.value == "        ---"){
                                        alert(" Seleccione un rol para el usuario");
                                        return false;
                                    }else{
                                        if( !(/^\d{7,}$/.test(telefono.value))) {
                                            alert("Ingresa un Teléfono válido")
                                            telefono.focus();
                                            return false;
                                          }else{
                                            if(direccion.value==""){
                                                alert("El campo dirección está vacío");
                                                direccion.focus();
                                                return false;
                                            }else{
                                                re=/^\w+([\.-]?\w+)@\w+([\.-]?\w+)(\.\w{2,3})+$/
                                                if(!re.exec(email.value)||email.value==""){
                                                    alert('Debe ingresar un Email válido!');
                                                    email.focus();
                                                    return false; 
                                                }else{
            
                                                    if(ciudadResidencia == null || ciudadResidencia ==0 || ciudadResidencia =="        ---"){
                                                        alert(" Seleccione una Ciudad de Residencia")
                                                        return false;
                                                    }else{
                                                        if(tipoContrato == null || tipoContrato ==0 || tipoContrato =="        ---"){
                                                            alert(" Seleccione un Tipo de Contrato")
                                                            return false;
                                                        }else{
                                                            if(cargo == null || cargo==0 || cargo =="        ---"){
                                                                alert(" Seleccione un Cargo")
                                                                return false;
                                                            }else{
                                                                if(fechaInicio.value==""){
                                                                    alert("Seleccione una Fecha de Inicio Correcta");
                                                                    fechaInicio.focus();
                                                                    return false;
                                                                }else{
                                                                    if(!validar_fecha_finalizacion(fechaFinalizacion.value,fechaInicio.value)){
                                                                        alert("Seleccione una Fecha de Finalización Correcta");
                                                                        fechaFinalizacion.focus();
                                                                        return false;
                                                                    }else{
                                                                        if(dependencia == null || dependencia ==0 || dependencia =="        ---"){
                                                                            alert(" Seleccione una Dependencia")
                                                                            return false;
                                                                        }else{
                                                                            if(!isNaN(salario) || salario.length < 5 || salario.value <= 0 || salario.value == ""){
                                                                                alert("Ingrese un Salario correcto");
                                                                                return false;
                                                                            }else{
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
                                                                                }else{
                                                                                    val=confirm("¿Está Seguro que desea crear este Usuario?")
                                                                                    if(val){
                                                                                        formulario.submit();
                                                                                        alert("Usuario creado..!");
                                                                                        return true
                                                                                    }else{
                                                                                        return false
                                                                                    }
                                                                                }
                                                                            }
                                                                        }
                                                                    }
                                                                }
                                                            }
                                                        }
                                                    }
                                                }
                                            }
                                        }
                                    } 
                                }
                            }
                        }
                    }
                }
            }      
        }
    }
}




//EDITAR USUARIOS

function validar_editar_usuario() {
    var formulario = document.getElementById("formeditarusuario");
    //datos personales
    var documento = document.getElementById('documento');
    var nombre = document.getElementById('nombre');
    var apellidos = document.getElementById('apellidos');
    var tipo_genero = document.getElementsByName('tipo_genero');
    var fechaNacimiento = document.getElementById('fechaNacimiento');
    var ciudadNacimiento = document.getElementById('ciudadNacimiento').selectedIndex;
    
    //datos de contacto
    var telefono = document.getElementById('telefono');
    var direccion = document.getElementById('direccion');
    var ciudadResidencia = document.getElementById('ciudadResidencia').selectedIndex;
    var email = document.getElementById('email');
    
    //datos de contrato
    var tipoContrato = document.getElementById('tipoContrato').selectedIndex;
    var cargo = document.getElementById('cargo').selectedIndex;
    var fechaInicio = document.getElementById('fechaInicio');
    var fechaFinalizacion = document.getElementById('fechaFinalizacion').value;
    var dependencia = document.getElementById('dependencia').selectedIndex;
    var salario = document.getElementById('salario');
    var estado = document.getElementsByName('estado');



    if(!isNaN(documento) || documento.length < 5||!(/^\d{5,}$/.test(documento.value))){
        alert("Seleccione un Número de identidad correcto");
        documento.focus();
        return false;
    }else{
        if (/^\s+$/.test(nombre) || nombre.length <= 2){
            alert("Nombre Incorrecto");
            nombre.focus();
            return false;
        }else{
            if (/^\s+$/.test(apellidos) || apellidos.length <=2 ){
                alert("Apellidos incorrectos");
                apellidos.focus();
                return false
            }else{
                var seleccionado = false;
                for (var i = 0; i < tipo_genero.length; i++) {
                    if (tipo_genero[i].checked) {
                        // get value, set checked flag or do whatever you need to
                        seleccionado = true;
                        break       
                    }
                }
                if(seleccionado != true) {
                    alert("No ha seleccionado el Género");
                    return false;
                }else{
                    if(fechaNacimiento.value==""||!validar_nac(fechaNacimiento.value)){
                        alert("Seleccione una Fecha de Nacimiento Correcta");
                        fechaNacimiento.focus();
                        return false;
                    }else{
                        if(ciudadNacimiento == null || ciudadNacimiento ==0 || ciudadNacimiento =="        ---"){
                            alert(" Seleccione una Ciudad de Nacimiento")
                            return false
                        }else{
                            if( !(/^\d{7,}$/.test(telefono.value))) {
                                alert("Ingresa un Teléfono válido")
                                telefono.focus();
                                return false;
                              }else{
                                if(direccion.value==""){
                                    alert("El campo dirección está vacío");
                                    direccion.focus();
                                    return false;
                                }else{
                                    re=/^\w+([\.-]?\w+)@\w+([\.-]?\w+)(\.\w{2,3})+$/
                                    if(!re.exec(email.value)||email.value==""){
                                        alert('Debe ingresar un Email válido!');
                                        email.focus();
                                        return false; 
                                    }else{

                                        if(ciudadResidencia == null || ciudadResidencia ==0 || ciudadResidencia =="        ---"){
                                            alert(" Seleccione una Ciudad de Residencia")
                                            return false;
                                        }else{
                                            if(tipoContrato == null || tipoContrato ==0 || tipoContrato =="        ---"){
                                                alert(" Seleccione un Tipo de Contrato")
                                                return false;
                                            }else{
                                                if(cargo == null || cargo==0 || cargo =="        ---"){
                                                    alert(" Seleccione un Cargo")
                                                    return false;
                                                }else{
                                                    if(fechaInicio.value==""){
                                                        alert("Seleccione una Fecha de Inicio Correcta");
                                                        fechaInicio.focus();
                                                        return false;
                                                    }else{
                                                        if(!validar_fecha_finalizacion(fechaFinalizacion.value,fechaInicio.value)){
                                                            alert("Seleccione una Fecha de Finalización Correcta");
                                                            fechaFinalizacion.focus();
                                                            return false;
                                                        }else{
                                                            if(dependencia == null || dependencia ==0 || dependencia =="        ---"){
                                                                alert(" Seleccione una Dependencia")
                                                                return false;
                                                            }else{
                                                                if(!isNaN(salario) || salario.length < 5 || salario.value < 0){
                                                                    alert("Ingrese un Salario correcto");
                                                                    return false;
                                                                }else{
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
                                                                    }else{
                                                                        val=confirm("¿Está Seguro que desea Editar al Usuario?")
                                                                        if(val){
                                                                            formulario.submit();
                                                                            alert("Usuario editado..!");
                                                                            return true
                                                                        }else{
                                                                            return false
                                                                        }
                                                                    }
                                                                }
                                                            }
                                                        }
                                                    }
                                                }

                                            }
                                        }
                                    }
                                }
                            }
                        }
                    }
                }
            }
        }
    }
}
var hoy = new Date();
var fechaHoy = hoy.getFullYear() + '-' + ( hoy.getMonth() + 1 ) + '-' + hoy.getDate();
///validacion de fechas
function validar_fecha_inicio(fechaInicio){
    if(fechaInicio < fechaHoy ){
        return false;
    }else{
        return true;
    }
}

function validar_fecha_finalizacion(fechaFinalizacion,fechaInicio){
    if(fechaFinalizacion <= fechaHoy || fechaFinalizacion <= fechaInicio){
        return false;
    }else{
        return true;
    }
}

function validar_nac(fechaNacimiento){
    if(fechaNacimiento >=  fechaHoy ){
        return false;
    }else{
        return true;
    }

}

// validacion EVALUAR
function validar_evaluacion() {
    
    var formulario = document.getElementById("formevaluar");

    var anoEvaluacion = document.getElementById('anoEvaluacion');
    var mesEvaluacion = document.getElementById('mesEvaluacion');
    
    var conocimiento = document.getElementById('conocimiento');
    var actitud = document.getElementById('actitud');
    var habilidad = document.getElementById('hablidad');
    var puntaje = document.getElementById('puntaje');
    var retroalimentacion = document.getElementById('retroalimentacion');
    //alert("entro en la funcion validar evaluacion 3");
    
    if(anoEvaluacion.selectedIndex == null || anoEvaluacion.selectedIndex ==0 || anoEvaluacion.selectedIndex =="        ---"){
        alert(" Seleccione el año a evaluar")
        return false;
    }else{
        if(mesEvaluacion.selectedIndex == null || mesEvaluacion.selectedIndex ==0 || mesEvaluacion.selectedIndex =="        ---"){
            alert(" Seleccione el mes a evaluar")
            return false;
        }else{
            if(puntaje.value==""){
                alert("verifique puntaje final, es un campo requerido en la Evaluación");
                retroalimentacion.focus();
                return false;
            }else{
                    val=confirm("La calificacion final es de: "+puntaje.value+", confirma la nota y la retroalimentación ?")
                    if(val){
                        //formulario.submit();
                        alert("Usuario evaluado..!");
                        return true;
                    }else{
                        return false;
                    }   
            }
        }
    }
}

//calculo puntaje 
function puntaje_final(){
    
    var conocimiento = document.getElementById('conocimiento').value
    var actitud = document.getElementById('actitud').value
    var habilidad = document.getElementById('habilidad').value
    var puntaje = document.getElementById('puntaje')
    var suma=(parseInt(conocimiento) + parseInt(actitud)+parseInt(habilidad))/3
    
    puntaje.value=suma.toFixed(2)

}

//validacion mes y año para visualizacion de la evaluacion del usuario
function validar_fechas_usuario() {
    var formulario = document.getElementById("formUsuarioFinal");

    var anoEvaluacion = document.getElementById('anoEvaluacion');
    var mesEvaluacion = document.getElementById('mesEvaluacion');
    var puntaje = document.getElementById('puntaje');

    if(anoEvaluacion.selectedIndex == null || anoEvaluacion.selectedIndex ==0 || anoEvaluacion.selectedIndex =="        ---"){
        alert(" Seleccione el año para la busqueda")
        return false;
    }else{
        if(mesEvaluacion.selectedIndex == null || mesEvaluacion.selectedIndex ==0 || mesEvaluacion.selectedIndex =="        ---"){
            alert(" Seleccione el mes para la busqueda")
            return false;
        }else{
            formulario.submit();
            return true;
        }
    }
}
//validacion mes y año para edicion de la evaluacion del usuario
function actualizar_evaluacion(id,anno,mes){
    
    var anoEvaluacion = document.getElementById('anoEvaluacion');
    var mesEvaluacion = document.getElementById('mesEvaluacion');
    //alert(mesEvaluacion.value);

    if(anoEvaluacion.selectedIndex == null || anoEvaluacion.selectedIndex == 0 || anoEvaluacion.value =="        ---"){
        alert(" Seleccione el año para la busqueda");
        return false;
    }else{
        if(mesEvaluacion.selectedIndex == null || mesEvaluacion.selectedIndex == 0 || mesEvaluacion.value =="        ---"){
            alert(" Seleccione el mes para la busqueda");
            return false;
        }else{
            window.location.href='/mainadmin/evaluar/'+id+'/'+anno+'/'+mes;
            return true  
        }
    }

}