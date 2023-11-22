from flask_wtf import FlaskForm
from flask_wtf.file import file_allowed, FileField
from flask_login import current_user
from wtforms import StringField, PasswordField, SubmitField, BooleanField, TextAreaField
from wtforms.validators import DataRequired, Length, Email, EqualTo, ValidationError
from app.models import User

class RegistrationForm(FlaskForm):
     username = StringField('Username', validators=[DataRequired(), Length(min=2, max=30)])
     email = StringField('Email',  validators=[DataRequired(), Email()])
     password = PasswordField('Password', validators=[DataRequired()])
     confirm_password = PasswordField('confirm password', validators=[DataRequired(), EqualTo('password')])
     submit = SubmitField('Sign up')

     def validate_username(self, username):
          user = User.query.filter_by(username=username.data).first()
          if user:
               raise ValidationError('That username already exist... Please choose another username')
          

     def validate_email(self, email):
          user = User.query.filter_by(email=email.data).first()
          if user:
               raise ValidationError('This email already exist... Please use another email')
     

class LoginForm(FlaskForm):
     email = StringField('Email', validators=[DataRequired(), Email()])
     password = PasswordField('Password', validators=[DataRequired()])
     remember = BooleanField('Remember Me')
     submit = SubmitField('Login')


class UpdateAccountForm(FlaskForm):
     username = StringField('Username', validators=[DataRequired(), Length(min=2, max=30)])
     email = StringField('Email',  validators=[DataRequired(), Email()])     
     picture = FileField('Update Profile Picture', validators=[file_allowed(['jpg', 'png', 'jpeg', 'gif'])])
     submit = SubmitField('Update')

     def validate_username(self, username):
          if username.data != current_user.username:
               user = User.query.filter_by(username=username.data).first()
               if user:
                    raise ValidationError('That username already exist... Please choose another username')
          

     def validate_email(self, email):
          if email.data != current_user.email:
               user = User.query.filter_by(email=email.data).first()
               if user:
                    raise ValidationError('This email already exist... Please use another email')
               
     def validate_password(self, password):
          if password.data != current_user.password:
               user = User.query.filter_by(password=password.data).first()
               if user:
                    raise ValidationError('This password already exist... Please use another email')               
     
      
class PostForm(FlaskForm):
     title = StringField('Title', validators=[DataRequired()])
     content = TextAreaField('Content', validators=[DataRequired()])
     submit = SubmitField('Post')