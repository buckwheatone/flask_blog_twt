from website import login_manager
from website.models import User
from flask import flash
from flask_login import current_user
from flask_wtf import FlaskForm
from flask_wtf.file import FileField, FileAllowed
# from wtforms.widgets.core import CheckboxInput
from wtforms import BooleanField, PasswordField, StringField, SubmitField, ValidationError
from wtforms.validators import DataRequired, Email, EqualTo, length

@login_manager.user_loader 
def load_user(user_id):
    return User.query.get(int(user_id))

class LoginForm(FlaskForm):
    email = StringField('Email', validators=[DataRequired(), Email()])
    password = PasswordField('Password', validators=[
                             DataRequired(),
                             length(min=8, max=200, message="Reminder: password must be at least 8 characters."), 
                             ])
    remember = BooleanField("Remember me")
    submit = SubmitField("Log in") 

class RegistrationForm(FlaskForm):
    email = StringField('Email', validators=[DataRequired(), Email()])
    username = StringField('Username', validators=[DataRequired(), length(min=3, max=20, message="Username must be at least 3 characters")])
    password = PasswordField('Password', validators=[DataRequired(), length(min=8, max=200, message="Password must be at least 8 characters")]) 
    submit = SubmitField("Sign Up") 

    def validate_username(self, username):
        user = User.query.filter_by(username=username.data).first()
        if user:
            print(user)
            raise ValidationError("Username already taken.")

    def validate_email(self, email):
        email = User.query.filter_by(email=email.data).first()
        if email:
            raise ValidationError("Email already in use.")

class UpdateProfilePic(FlaskForm):
    profile_pic = FileField('Update Profile Pic', validators=[FileAllowed(['jpg', 'jpeg', 'png'])])
    submit = SubmitField("Update")

class RequestResetForm(FlaskForm):
    email = StringField('Email', validators=[DataRequired(), Email()])
    submit = SubmitField("Request password reset") 

    def validate_email(self, email):
        user = User.query.filter_by(email=email.data).first()
        if user is None:
            flash("No account found.  Please register", category='danger')
            raise ValidationError("No account found.  Please register.")

class ResetPasswordForm(FlaskForm):
    password = PasswordField('Password', validators=[DataRequired()])
    confirm_password = PasswordField('Confirm Password', validators=[DataRequired(), EqualTo('password')])
    submit = SubmitField('Reset password') 

class UpdateEmailForm(FlaskForm):
    email = StringField('Email', validators=[DataRequired(), Email()])
    submit = SubmitField("Update email") 

    def validate_email(self, email):
        user = User.query.filter_by(email=email.data).first()
        if email.data == current_user.email or user:
            flash("Email already in use.", category='danger')
            raise ValidationError("Email already in use.")
        
class UpdateUsernameForm(FlaskForm):
    username = StringField('Username', validators=[DataRequired(), length(min=3, max=20, message="Username must be at least 3 characters")])
    submit = SubmitField("Update username") 

    def validate_username(self, username):
        user = User.query.filter_by(username=username.data).first()
        if username.data == current_user.username or user:
            flash("Username already in use.", category='danger') 
            raise ValidationError("Username already in use.")

    # TODO: consider adding ASCII letters only validation