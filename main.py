from flask import Flask

app = Flask(__name__) #esta es la linea 3

@app.route('/') #Este decorador es de la variable app de la linea 3
def hello():
    return "Hello world from flask"

"""
En la terminal correr "flask run"
Por defecto busca "wsgi.py" o "app.py"
para cambiar esto y que corra el "main.py" se modificar la variable del sistema

En la terminal correr
export FLASK_APP=main.py
Sin espacios
"""