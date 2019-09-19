""""
ENCRIPTAR COOKIES
====================
"""
from flask import Flask, request, make_response, redirect, render_template, session
from flask_wtf import FlaskForm
from wtforms.fields import StringField, PasswordField, SubmitField
from wtforms.validators import DataRequired # se puede modificar a nuestro gusto

from flask_bootstrap import Bootstrap

app = Flask(__name__)
app.config["SECRET_KEY"] = "SUPER SECRETO" # encriptacion con clave

# nuestra clase de Uusario y contraseña
class LoginFormulario(FlaskForm):
    # variables globales
    usuario = StringField("Nombre de usuario: ", validators=[DataRequired()])
    password = PasswordField("Contraseña de usuario: ", validators=[DataRequired()])
    botonEnviar = SubmitField("Enviar")



# pagina de robo de informacion al usuario
# donde redirigimos al usuario a /inicio
@app.route("/")
def home():
    ip = request.remote_addr
    envio = make_response(redirect("/inicio"))
    # envio.set_cookie("user_ip", ip)
    # Guardando la informacion en la sesion
    # en vez de la cookie
    session["user_ip"] = ip
    

    return envio

# funcion con ruta virtual /inicio
@app.route("/inicio")
def inicio():
    
    # recuperarCookie = request.cookies.get("user_ip")
    recuperarCookie = session.get("user_ip")
    loginform = LoginFormulario()

    context = {
        "cookie": recuperarCookie,
        "loginForm": loginform,


    }
    
    # return "Ya estamos en inicio {}".format(recuperarCookie) # render_template("inicio.html")
    return render_template("inicio.html", **context) # diccionario abierto

# punto de entrada
if __name__ == '__main__':
    app.run("127.0.0.1", 5000, debug=True)
