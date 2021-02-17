from flask.app import Flask
from flask_bootstrap import Bootstrap
from flask_login import LoginManager
from .auth import auth
from .config import Config
from .models import UserModel

# es el login manager el cual va a inicializar la app y permite cargar
# l el usuario
login_manager = LoginManager()
# la ruta donde va a direccionar cuando se requera el login
login_manager.login_view = 'auth.login'


# este decorador lo que hace es usar la librería flask-login
# que ya había importado previamente, y con el método user_loader de esa
# librería recargo el id del usuario que ya tengo almacenado en la sesión para
# devolver el objeto correspondiente a ese usuario.
@login_manager.user_loader
def load_user(username):
    return UserModel.query(username)

def create_app():
    app = Flask(__name__)
    bootstrap = Bootstrap(app)

    app.config.from_object(Config)

    # login manager inicializando la app
    login_manager.init_app(app)

    # Se registra el nuevo blueprint auth
    app.register_blueprint(auth)

    return app