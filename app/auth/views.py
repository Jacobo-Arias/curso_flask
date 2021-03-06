from flask import render_template, flash, redirect, url_for, session
from app.forms import LoginForm
from . import auth

from flask_login import login_user, current_user, login_required, logout_user
from werkzeug.security import check_password_hash, generate_password_hash

from app.mongo_services import get_user, user_put
from app.models import UserData, UserModel

@auth.route('/login', methods = ['GET','POST'])
def login():

    # Esta bloque if es para que lo redireccione al index si ya está logueado
    # e intenta entrara a la página de login
    if current_user.is_authenticated:
        return redirect(url_for('index'))
    login_form = LoginForm()
    context = {
        'login_form':login_form
    }
    if login_form.validate_on_submit():
        username = login_form.username.data
        password = login_form.password.data
        user_doc = get_user(username)

        if user_doc is not None:
            password_from_db = user_doc['password']

            if check_password_hash(password_from_db, password):
                user_data = UserData(username,password)
                user = UserModel(user_data)

                login_user(user)

                flash("Bienvenido de nuevo")

                redirect(url_for('hello'))

            else:
                flash("Contraseña equivocada")
        else:
            # Envia un nuevo mensaje flash (emergente) y en la plantilla base se accede
            # a este con el metodo get_flashed_messages
            flash("Usuario no encontrado")
            


        return redirect(url_for('index'))
        #si hay un submit efectivo redirecciona a index para que cargue toda la informacion
    return render_template('login.html', **context)

#se aceptan los dos metodos porque el get regresa la forma y el post la obtiene
@auth.route('/singup', methods = ['GET','POST'])
def singup():
    singup_form = LoginForm()
    context = {
        'singup_form':singup_form
    }

    if singup_form.validate_on_submit():
        username = singup_form.username.data
        password = singup_form.password.data

        user_doc = get_user(username)

        if user_doc is None:
            password_hash = generate_password_hash(password)
            user_data = UserData(username, password_hash)
            user_put(user_data)

            user = UserModel(user_data)

            login_user(user)
            flash("Bienvenido!")
            return redirect(url_for('hello'))
        
        else:
            flash("El usuario ya existe!")

    return render_template('singup.html',**context)

@auth.route('/logout')
# este decorador dice que se debe estar logineado para poder acceder a logout
@login_required
def logout():
    logout_user()
    flash("Regresa pronto")
    return redirect(url_for('auth.login'))