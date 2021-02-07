from flask import Flask, request, make_response, redirect, render_template

app = Flask(__name__) #esta es la linea 3

todos = ['Comprar café','Enviar solicitud','Enviar productos']

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
    response.set_cookie('user_ip', user_ip)
    # Guarda la ip en las cookies con el nombre de user_ip

    return response

@app.route('/hello') #Este decorador es de la variable app de la linea 3
def hello():
    # Obtiene la ip del usuario de las coocies con el nombre/identificador
    # "user_ip"
    user_ip = request.cookies.get('user_ip')

    context = {
        'user_ip': user_ip,
        'todos': todos
    }

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