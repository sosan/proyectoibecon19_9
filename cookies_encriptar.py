""""
ENCRIPTAR COOKIES
====================
"""
from flask import Flask, request, make_response, redirect, render_template, session, flash
from flask_wtf import FlaskForm
from wtforms.fields import StringField, PasswordField, SubmitField
from wtforms.validators import DataRequired, Regexp, InputRequired  # se puede modificar a nuestro gusto
from wtforms.validators import ValidationError, DataRequired, Email, EqualTo, Length
import logging
import redis

logger = logging.getLogger(__name__)
logginCount = 0

from flask_bootstrap import Bootstrap

app = Flask(__name__)
app.config["SECRET_KEY"] = "SUPER SECRETO"  # encriptacion con clave

# conexion redis db
red = redis.Redis(host='redis-19111.c55.eu-central-1-1.ec2.cloud.redislabs.com', port=19111,
                  password="NNXYsaSfer3od5xZRqlApthvppdW9Y4f", db=0)
red.set("hola", "123")  # done


# nuestra clase de Uusario y contraseña


class LoginFormulario(FlaskForm):
    # variables globales
    usuario = StringField("Nombre de usuario:", validators=[DataRequired(), Length(1, 64)])

    password = PasswordField("Contraseña de usuario:", validators=[DataRequired(),
                                                                   Length(5, 18)
                                                                  # ,Regexp('^[A-Za-z][A-Za-z0-9_.]*$', 0, "Usernames must have only letters, numbers, dots or underscores"),
                                                                  # EqualTo('password2',
    #                                                                       message='Passwords must match.')
                                                                   ]
    )
    password2 = PasswordField("Confirma Contraseña: ")
    botonEnviar = SubmitField("Enviar")

    error = ""
    loginOrRegister = ""  # state=> login / register / none

    def validate_username(self, field):
        pass
        # if User.query.filter_by(username=field.data).first():
        #     raise ValidationError('Username already in use.')


def redirectToHome():
    envio = make_response(redirect("/inicio"))
    return envio


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


countGlobal = 0


# funcion con ruta virtual /inicio
@app.route("/inicio", methods=["GET", "POST"])
def inicio():
    # recuperarCookie = request.cookies.get("user_ip")

    try:
        recuperarCookie = session.get("user_ip")
        loginform = LoginFormulario()

        context = {
            "cookie": recuperarCookie,
            "loginForm": loginform,  # clase loginform
            "count": countGlobal

        }

        # return "Ya estamos en inicio {}".format(recuperarCookie) # render_template("inicio.html")
        return render_template("new/login_register_modal.html", resultado=context)  # diccionario abierto

    except:
        return render_template("errorgeneral.html", resultado=context)  # diccionario abierto


@app.route("/resultado_form_register", methods=["POST", "GET"])
def result():
    # if not request.form.validate_on_submit():
    #     return render_template('index.html', resultado=request.form, error="NOt submit correctly")

    if request.method == 'POST' and request.form != None:
        formulario = request.form
        if formulario["usuario"] == "" or formulario["password"] == "":
            return redirectToHome()
        else:
            usuario = formulario["usuario"]

            if red.hexists("users", usuario) == True:
                # mensaje de ya existe....
                error = "Invalid credentials"
                flash('FLASH. INVALID CREDENTIALS.')  # se podria sustituir por error???
                return render_template("new/register_user_formulario.html", resultado=formulario, error=error)
            else:
                red.hset("users", usuario, formulario["password"])  # cambiarlo por hash
                return render_template("resultado_form_register.html", resultado=formulario)
    else:
        return redirectToHome()


# errores
@app.errorhandler(404)
def error404(error):
    return "<h1>pagina no encontrado</h1>"


@app.route("/inicio2", methods=["GET", "POST"])
def inicio2():
    #    try:

    ip = request.remote_addr
    session["user_ip"] = ip

    recuperarCookie = session.get("user_ip")
    loginform = LoginFormulario()

    context = {
        "cookie": recuperarCookie,
        "loginForm": loginform,
        "count": countGlobal
    }

    # return "Ya estamos en inicio {}".format(recuperarCookie) # render_template("inicio.html")
    return render_template("inicio.html", **context)  # diccionario abierto


# punto de entrada
if __name__ == '__main__':
    app.run("127.0.0.1", 5000, debug=True)
