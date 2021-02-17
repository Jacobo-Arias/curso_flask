from flask_testing import TestCase
from flask import current_app, url_for

from main import app

class MainTest(TestCase):
    # el metodo create_app viene de TestCase por lo que se debe crear la app
    # que importamos de main y se establece en modo TESTING 
    def create_app(self):
        app.config['TESTING'] = True
        # Desactiva la segurdad "Cross-site request forgery" para poder hacer los tests
        # esta seguridad previene de sufrir ataques de inserción de códigos de comandos
        app.config['WTF_CSRF_ENABLED'] = False
        return app

    # verifica que la current_app que es algo de flak referente a
    # la app existente no sea nula
    def test_app_exists(self):
        self.assertIsNotNone(current_app)

    # verifica que la app esté en modo testing
    def test_app_mode_testing(self):
        self.assertTrue(current_app.config['TESTING'])

    # verifica que el index redireccione a hello
    def test_index_redirects(self):
        response = self.client.get(url_for('index'))
        self.assertRedirects(response,url_for('hello'))
    
    # verifica el metodo get de hello funcione bien
    # *el código 200 significa que todo ha ido bien
    def test_hello_get(self):
        response = self.client.get(url_for('hello'))
        self.assert200(response)
    
    # verifica que una vez enviado un form lo redireccione a index
    # por eso se crea un fake form y se manda como el parametro data
    # al metodo post de client
    def test_hello_post(self):
        response = self.client.post(url_for('hello'))
        self.assertTrue(response.status_code, 405)


    def test_auth_blueprin_exist(self):
        # Que efectivamente exista un blueprint llamado auth
        self.assertIn('auth', self.app.blueprints)

    def test_auth_login_get(self):
        self.client.get(url_for('auth.login'))
        # No se guarda la petición en la variable response porque con llamarla
        # y mediante el paquete blinker por debja identifica que el template usado
        # si fue login.html, por eso solo hay que mandarle un parametro
        # el cual es el nombre del template
        self.assertTemplateUsed('login.html')

    def test_auth_login_template(self):
        self.client.get(url_for('auth.login'))

        self.assertTemplateUsed('login.html')

    def test_auth_login_post(self):
        fake_form = {
            'username':'fake',
            'password' : 'fake-password'
            }
        
        response = self.client.post(url_for('auth.login'), data = fake_form)
        self.assertRedirects(response, url_for('index'))

    #* Para esto debo tener instalado el blinker    
    def test_user_registered_flashed_message(self):
        fake_form = {
            'username': 'vijoin',
            'password': '123456'
        }
        self.client.post(url_for('auth.login'), data=fake_form)
        message = 'Usuario registrado correctamente'
        self.assertMessageFlashed(message)