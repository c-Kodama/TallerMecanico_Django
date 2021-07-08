document.getElementById("btn__registrarse").addEventListener("click", register)
document.getElementById("btn__iniciar__sesion").addEventListener("click", iniciarSesion)
window.addEventListener("resize", anchoPagina)

//Declarar variables
var container_login_registro = document.querySelector(".container__login__registro")
var formulario_login = document.querySelector(".formulario__login")
var formulario_registro = document.querySelector(".formulario__registro")
var background_box_login = document.querySelector(".background__box__login")
var background_box_registro = document.querySelector(".background__box__Registro")

function anchoPagina(){
    if(window.innerWidth > 850){
        background_box_login.style.display ="block";
        background_box_registro.style.display ="block";
    }else{
        background_box_registro.style.display ="block";
        background_box_registro.style.opacity ="1";
        background_box_login.style.display ="none";
        formulario_login.style.display ="block";
        formulario_registro.style.display ="none";
        container_login_registro.style.left ="0px";;
    }
}

anchoPagina();

function iniciarSesion(){

    if(window.innerWidth > 850){
        formulario_registro.style.display = "none";
        container_login_registro.style.left ="10px";
        formulario_login.style.display ="block";
        background_box_registro.style.opacity ="1";
        background_box_login.style.opacity ="0";
    }else{
    formulario_registro.style.display = "none";
    container_login_registro.style.left ="0px";
    formulario_login.style.display ="block";
    background_box_registro.style.display ="block";
    background_box_login.style.display ="none";
    }
    
}

function register(){
    if(window.innerWidth >850 ){formulario_registro.style.display = "block";
    container_login_registro.style.left ="410px";
    formulario_login.style.display ="none";
    background_box_registro.style.opacity ="0";
    background_box_login.style.opacity ="1";
    }else{
    formulario_registro.style.display = "block";
    container_login_registro.style.left ="0px";
    formulario_login.style.display ="none";
    background_box_registro.style.display ="none";
    background_box_login.style.display ="block";
    background_box_login.style.opacity ="1";
    }
    
}
