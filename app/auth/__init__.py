from flask import Blueprint

# auth va a ser un blueprint que se va a llamar 'auth'
# y va a tener un prefijo que va a ser /auth y eso significa que todas
# las rutas que comiencen con /auth van a ser redirigidas a este blueprint
# y en este blueprint vamos a crear views que van a vivir en /auth/login o
# /auth/singup o /auth/logout
auth = Blueprint('auth', __name__, url_prefix='/auth')

# por eso las vistas se importan al final, las vistas son como las rutas
# que se tienen en main.py
from . import views

