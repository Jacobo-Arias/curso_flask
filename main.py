from flask import Flask, request, make_response, redirect

app = Flask(__name__) #esta es la linea 3

@app.route('/')
def index():
    user_ip = request.remote_addr #la ip del usuario, la que se detecta en la request

    response = make_response(redirect('/hello'))
    response.set_cookie('user_ip', user_ip)
    # Guarda la ip en las cookies con el nombre de user_ip

    return response

@app.route('/hello') #Este decorador es de la variable app de la linea 3
def hello():
    #Obtiene la ip del usuario de las coocies con el nombre/identificador
    # "user_ip"
    user_ip = request.cookies.get('user_ip')
    return f"Hello world from flask, yout ip is {user_ip}"

"""
En la terminal correr "flask run"
Por defecto busca "wsgi.py" o "app.py"
para cambiar esto y que corra el "main.py" se modificar la variable del sistema

En la terminal correr
export FLASK_APP=main.py
Sin espacios
"""