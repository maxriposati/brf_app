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

    if(email.length == 0) {
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
		alert('Debes ingresar un email electrónico valido!');
        mail.focus();
        return false; 
	}
    alert('El mensaje se ha enviado exitosamente');
    this.reset();
  
    
}
// LOGIN

document.addEventListener("DOMContentLoaded", function() {
    document.getElementById("formLogin").addEventListener('submit', validar_login); 
});
function validar_login(evento){
    evento.preventDefault();
    var user = document.getElementById('username');
    var password = document.getElementById('password');
    var politaca = document.getElementById('politicas');
    if(user.value ==""){
        alert("El campo de Nombre esta vacio");
        user.focus();
        return false;
    }
    else{

       if(password.value==""){
           alert("El campo de password esta vacio");
           password.focus();
           return false;
       }
       else{
            if(politaca.checked==false){
                alert(" Por favor Marque la opcion de politicas")
                return false;
        }
           else if(user.value == "admin" ){
               window.location.href="/mainadmin";
               alert("Bienvenido Usuario Administrador");
               return true;
           }
           else if(user.value == "user"){
                window.location.href='/mainusuario';
                return true;
           }

           else{ alert("Usuario no Regsitrado")
           
           return false;
        }

       }
    }
}

//OLVIDO DE CONTRASENA

document.addEventListener("DOMContentLoaded", function() {
    document.getElementById("formOlvido").addEventListener('submit', validar_Olvido); 
});
function validar_Olvido(evento){
        evento.preventDefault();
        var user = document.getElementById('username');
        if(user.value=="admin"){
            alert("Password restablecido")
            this.submit();
        }else{
            alert("Usuario no registrado")
            return false;
        }
       
    }

//MAIN ADMINISTRADOR
function eliminarUsuario(){
    confirm("Esta Seguro que desea eliminar el usuario")
}