from flask import request, make_response, redirect, render_template, url_for, flash

from flask import session 
# se importa session el cual se utiliza para guardar, a traves de varias peticiones,
# información de manera segura, como las cookies que las encripta
from flask_bootstrap import Bootstrap
# flask bootstrap es basicamente para darle diseño y funciona con el framework bootstrap
# en este caso tengo instalados flask_bootstrap y flask_bootstrap4 y si desisntalo
# uno de ellos no funicona no se por que
import unittest

from flask_login import login_required, current_user
from app.forms import TodoForm, DeleteToDoForm, UpdateToDoForm

from app.firestore_service import update_todo, get_todos, put_todo, delete_todo

from app import create_app

app = create_app()



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

@app.route('/hello', methods = ['GET','POST']) #Este decorador es de la variable app de la linea 3
@login_required #no se puede acceder hasta haberse logueado
def hello():
    # Obtiene la ip del usuario de las session con el nombre/identificador
    # "user_ip"
    user_ip = session.get('user_ip')
    # current user es una funcion de flask-login que nos permite acceder
    # a la información del usuario actual logueado
    username = current_user.id 

    todo_form = TodoForm()
    delete_form = DeleteToDoForm()
    update_form = UpdateToDoForm()

    context = {
        'user_ip': user_ip,
        'todos': get_todos(user_id=username),
        'username':username,
        'todo_form':todo_form,
        'delete_form':delete_form,
        'update_form':update_form,
    }

    if todo_form.validate_on_submit():
        put_todo(user_id=username, description=todo_form.description.data)
        
        flash("Tarea creada con éxito")
        return redirect(url_for('index'))

    return render_template('hello.html', **context)
    # Renderiza el template de la carpeta templates y se le manda 
    # la variable user_ip referenciandola como user_ip para poderla
    # usar en la plantilla

@app.route('/todos/delete/<todo_id>',methods=['GET','POST'])
def delete(todo_id):
    user_id = current_user.id
    delete_todo(user_id=user_id, todo_id=todo_id)
    return redirect(url_for('hello'))

@app.route('/todos/update/<todo_id>/<int:done>',methods=['GET','POST'])
def update(todo_id, done):
    user_id = current_user.id
    update_todo(user_id=user_id,todo_id=todo_id,done=done)
    
    return redirect(url_for('hello'))    


"""
En la terminal correr "flask run"
Por defecto busca "wsgi.py" o "app.py"
para cambiar esto y que corra el "main.py" se modificar la variable del sistema

En la terminal correr
export FLASK_APP=main.py
Sin espacios
"""