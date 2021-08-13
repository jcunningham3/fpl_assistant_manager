from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, IntegerField, TextAreaField
from wtforms.validators import InputRequired

class UserForm(FlaskForm):
    email = StringField("Username", validators=[InputRequired()])
    password = PasswordField("Password", validators=[InputRequired()])
    team_id = IntegerField("Team Id", validators=[InputRequired()])


class LoginForm(FlaskForm):
    email = StringField("Email", validators=[InputRequired()])
    password = PasswordField("Password", validators=[InputRequired()])


class ChatForm(FlaskForm):
    text = StringField("Chat", validators = [InputRequired()])
