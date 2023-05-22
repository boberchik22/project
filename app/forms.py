from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, BooleanField, SubmitField, IntegerField
from wtforms.validators import DataRequired, Email, EqualTo

class RegistrationForm(FlaskForm):
    username= StringField('Username',validators =[DataRequired()])
    password = PasswordField('Password', validators=[DataRequired()])
    password1 = PasswordField('Repeat Password', validators=[DataRequired(),EqualTo('password')])
    email=StringField('Email', validators=[Email()])
    remember= BooleanField('Remember?')
    submit=SubmitField('Enter')
class CarForm(FlaskForm):
    brand=StringField('Carbrand', validators =[DataRequired()])
    year =IntegerField('Year',validators =[DataRequired()])
    numbers=IntegerField('Numbers',validators =[DataRequired()])
    accident=StringField('Accident',validators =[DataRequired()])
class Register(FlaskForm):
    password=PasswordField('password',validators =[DataRequired()])
    name=StringField('name',validators =[DataRequired()])
    remember = BooleanField('Remember?')
    submit = SubmitField('Enter')