from flask import render_template, flash, redirect, url_for, session
from app.forms import LoginForm
from . import auth

@auth.route('/login', methods = ['GET','POST'])
def login():
    login_form = LoginForm()
    context = {
        'login_form':login_form
    }
    if login_form.validate_on_submit():
        username = login_form.username.data
        session['username'] = username

        # Envia un nuevo mensaje flash (emergente) y en la plantilla base se accede
        # a este con el metodo get_flashed_messages
        flash("Usuario registrado correctamente")

        return redirect(url_for('index'))
        #si hay un submit efectivo redirecciona a index para que cargue toda la informacion
    return render_template('login.html', **context)