""""
ENCRIPTAR COOKIES
====================
"""
from flask import Flask, request, make_response, redirect, render_template
from flask_bootstrap import Bootstrap

app = Flask(__name__)


# pagina de robo de informacion al usuario
# donde redirigimos al usuario a /inicio
@app.route("/")
def home():
    ip = request.remote_addr
    envio = make_response(redirect("/inicio"))
    envio.set_cookie("user_ip", ip)
    return envio

# funcion con ruta virtual /inicio
@app.route("/inicio")
def inicio():
    return render_template("inicio.html")


# punto de entrada
if __name__ == '__main__':
    app.run("127.0.0.1", 5000, debug=True)
