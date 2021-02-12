from flask import request, make_response, redirect, render_template, url_for

from flask import session 
# se importa session el cual se utiliza para guardar, a traves de varias peticiones,
# información de manera segura, como las cookies que las encripta
from flask_bootstrap import Bootstrap
# flask bootstrap es basicamente para darle diseño y funciona con el framework bootstrap
# en este caso tengo instalados flask_bootstrap y flask_bootstrap4 y si desisntalo
# uno de ellos no funicona no se por que
import unittest
from app.forms import LoginForm

from app import create_app

app = create_app()

todos = ['Comprar café','Enviar solicitud','Enviar productos']



# Se crea el comando en la consola de comandos con la librería cli que viene
# en la app, dicha linea es test y se corre flask test y así correr los tests
# * flask test
@app.cli.command()
def test():
    # se llama la librería unitest con el cargador de tests y los busca
    # "descubre" en la carpeta tests, carpeta donde se guardarán los archivos
    # de test cuyo nombre debe iniciar con test_
    tests = unittest.TestLoader().discover('tests')
    unittest.TextTestRunner().run(tests)


@app.errorhandler(404)
def not_found(error):
    return render_template('404.html',error=error)

@app.errorhandler(500)
def server_error(error):
    return render_template('500.html',error=error)

@app.route('/')
def index():
    # TODO: para probar el error 500 hay que poner la variable de entorno 
    # TODO: FLASK_DEBUG=0 y lanzar el servidor
    # TODO: raise(Exception(500))
    user_ip = request.remote_addr #la ip del usuario, la que se detecta en la request

    response = make_response(redirect('/hello'))
    # Guarda la ip en la session con el nombre de user_ip
    session['user_ip'] = user_ip

    return response

@app.route('/hello', methods = ['GET']) #Este decorador es de la variable app de la linea 3
def hello():
    # Obtiene la ip del usuario de las session con el nombre/identificador
    # "user_ip"
    user_ip = session.get('user_ip')

    login_form = LoginForm()
    username = session.get('username')

    context = {
        'user_ip': user_ip,
        'todos': todos,
        'username':username
    }

    # if login_form.validate_on_submit():
    #     username = login_form.username.data
    #     session['username'] = username

    #     # Envia un nuevo mensaje flash (emergente) y en la plantilla base se accede
    #     # a este con el metodo get_flashed_messages
    #     flash("Usuario registrado correctamente")

    #     return redirect(url_for('index'))
    #     #si hay un submit efectivo redirecciona a index para que cargue toda la informacion

    return render_template('hello.html', **context)
    # Renderiza el template de la carpeta templates y se le manda 
    # la variable user_ip referenciandola como user_ip para poderla
    # usar en la plantilla

"""
En la terminal correr "flask run"
Por defecto busca "wsgi.py" o "app.py"
para cambiar esto y que corra el "main.py" se modificar la variable del sistema

En la terminal correr
export FLASK_APP=main.py
Sin espacios
"""