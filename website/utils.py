import os
import secrets 
from website import mail
from flask import current_app, url_for
from flask_mail import Message
from PIL import Image 


def save_picture(form_picture):
    random_hex = secrets.token_hex(8)
    _, f_ext = os.path.splitext(form_picture.filename)
    picture_fn = random_hex + f_ext
    picture_path = os.path.join(current_app.root_path, 'static/profile_pics', picture_fn)
    profile_pic_size = (125, 125)
    i = Image.open(form_picture)
    i.thumbnail(profile_pic_size)
    i.save(picture_path)
    #TODO: Consider writing clean-up actions to remove old photos

    return picture_fn

def send_reset_email(user):
    token = user.get_reset_token()
    
    msg = Message('Password reset for SpaceR', sender=os.getenv("MAIL_DEFAULT_SENDER"),
                    recipients=[user.email])
    # _external=True is for full links vs. relative links we use in the app
    msg.body = f"""
To reset your password for SpaceR, visit the following link:
{url_for('users.reset_token', token=token, _external=True)}

If you did not request a password reset, please ignore this email.
    """
    mail.send(msg)
