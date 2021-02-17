from wtforms.fields import StringField, PasswordField, SubmitField
from wtforms.validators import DataRequired
from flask_wtf import FlaskForm


class LoginForm(FlaskForm):
    username = StringField('Nombre Usuario', validators=[DataRequired()])
    password = PasswordField('Password', validators=[DataRequired()])
    submit = SubmitField('Enviar ')


class TodoForm(FlaskForm):
    description = StringField('Descripción', validators=[DataRequired()])
    submit = SubmitField('Crear')


class DeleteToDoForm(FlaskForm):
    submit = SubmitField("Borrar")


class UpdateToDoForm(FlaskForm):
    submit = SubmitField("Actualizar")