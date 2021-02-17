conda deactivate
source venv/bin/activate

# export GOOGLE_CLOUD_PROJECT="flask-platzi-304617"

# FLASK_APP es para tomar a main como el archivo principal cuando se corre el 
# servidor, por defecto es app.py
export FLASK_APP=main.py
export FLASK_DEBUG=1
# FLASK_DEBUG es para activar el modo debugger, y así no tener que apagar
# y prender el server cada vez que se efectúe un cambio
export FLASK_ENV=development
# Se usa para activar el modo development de flask ya que por defecto
# es modo production
flask run
