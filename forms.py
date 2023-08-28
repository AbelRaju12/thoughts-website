from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, SubmitField, BooleanField
from wtforms.validators import DataRequired, Length, Email, EqualTo, ValidationError

class loginform(FlaskForm):
    username = StringField('Username', validators=[DataRequired()])
    password = PasswordField('Password', validators=[DataRequired()])
    remember = BooleanField('Remember Me')
    submit = SubmitField('Login')
    
class registerform(FlaskForm):
    username = StringField('Username', validators=[DataRequired(), Length(min = 3, max = 20)])
    email = StringField('Email', validators=[DataRequired(), Length(min = 3, max = 120), Email()])
    confirm_email = StringField('Confirm Email', validators=[DataRequired(), Length(min = 3, max = 120), Email(), EqualTo('email')])
    password = PasswordField('Password', validators=[DataRequired()])
    confirm_password = PasswordField('Confirm Password', validators=[DataRequired(), EqualTo('password')])
    submit = SubmitField('Sign Up')
    
    