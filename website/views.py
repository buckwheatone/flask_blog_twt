import os
import secrets
from flask import current_app, Blueprint, render_template, request, flash, redirect, url_for, jsonify
from flask_login import login_required, current_user, logout_user
from sqlalchemy import select, or_
from .models import Post, User, Comment, Like
from .forms import (LoginForm, RegistrationForm, 
                    UpdateEmailForm, UpdateProfilePic, 
                    RequestResetForm, ResetPasswordForm, UpdateUsernameForm)
from .utils import save_picture
from . import db
from PIL import Image

views = Blueprint("views", __name__)


@views.route("/home")
@login_required 
def home():
    page = request.args.get('page', 1, type=int)

    # query to filter only active user IDs
    is_active_ids = db.session.query(User.id).filter_by(active=1)

    posts = Post.query\
                .filter(Post.author.in_(is_active_ids))\
                .order_by(Post.date_created.desc())\
                .paginate(page=page, per_page=10) 

    # list of active user IDs for use in posts_div view
    comment_id_list = [id for tup in is_active_ids.all() for id in tup]

    return render_template("home.html", user=current_user, posts=posts, id_list=comment_id_list)

@views.route("/profile", methods=['GET', 'POST'])
@login_required
def profile():
    # Email, username, password, profile pic forms 
    update_em_form = UpdateEmailForm()
    update_un_form = UpdateUsernameForm()
    update_pp_form = UpdateProfilePic() 


    if update_pp_form.validate_on_submit():
        if update_pp_form.profile_pic.data:
            picture_file = save_picture(update_pp_form.profile_pic.data) 
            current_user.image_file = picture_file 
        db.session.commit()

        return redirect(url_for('views.profile'))
    image_file = url_for('static', filename='profile_pics/' + current_user.image_file) 
    return render_template("profile.html", image_file=image_file, 
                            update_em_form=update_em_form,
                            update_pp_form=update_pp_form,
                            update_un_form=update_un_form) 


@views.route("/create-post", methods=['GET', 'POST'])
@login_required
def create_post():
    if request.method == "POST":
        text = request.form.get('text')

        if not text:
            flash('Post cannot be empty', category='error')
        else:
            post = Post(text=text, author=current_user.id)
            db.session.add(post)
            db.session.commit()
            flash('Post created!', category='success')
            return redirect(url_for('views.home'))

    return render_template('create_post.html', user=current_user)


@views.route("/delete-post/<id>", methods=['POST'])
@login_required
def delete_post(id):
    post = Post.query.filter_by(id=id).first()

    if not post:
        flash("Post does not exist.", category='error')
    elif current_user.id != post.author:
        flash('You do not have permission to delete this post.', \
              category='error')
    else:
        db.session.delete(post)
        db.session.commit()
        flash('Post deleted.', category='success')

    return redirect(url_for('views.home'))


@views.route("/posts/<string:username>")
@login_required
def posts(username):
    user = User.query.filter_by(username=username, active=True).first()

    if not user:
        flash('No user with that username exists.', category='error')
        return redirect(url_for('views.home'))

    page = request.args.get('page', 1, type=int)
    posts = Post.query.filter_by(author=user.id)\
                .order_by(Post.date_created.desc())\
                .paginate(page=page, per_page=10)
    is_active_ids = db.session.query(User.id).filter_by(active=1)
    comment_id_list = [id for tup in is_active_ids.all() for id in tup]

    return render_template("posts.html", \
            user=current_user, posts=posts, username=username, id_list=comment_id_list)

@views.route("/create-comment/<post_id>", methods=['POST'])
@login_required
def create_comment(post_id):
    text = request.form.get('text')

    if not text:
        flash('Comment cannot be empty.', category='error')
    else:
        post = Post.query.filter_by(id=post_id)
        if post:
            comment = Comment(
                text=text, author=current_user.id, post_id=post_id)
            db.session.add(comment)
            db.session.commit()
        else:
            flash('Post does not exist.', category='error')

    return redirect(url_for('views.home'))


@views.route("/delete-comment/<comment_id>")
@login_required
def delete_comment(comment_id):
    comment = Comment.query.filter_by(id=comment_id).first()
    if not comment:
        flash('Comment does not exist.', category='error')
    elif current_user.id != comment.author and current_user.id != comment.post.author:
        flash('You do not have permission to delete this comment.', \
              category='error')
    else:
        db.session.delete(comment)
        db.session.commit()
    return redirect(url_for('views.home'))

@views.route("/delete-account", methods=['POST', 'GET'])
def delete_account():
    current_user.active = 0
    current_user.email = current_user.email + '_deleted'
    db.session.commit()
    logout_user()
    flash("Your account has been deleted.", category='info')
    return redirect(url_for('auth.landing'))


@views.route("/like-post/<post_id>", methods=['POST'])
@login_required
def like(post_id):
    post = Post.query.filter_by(id=post_id).first()
    like = Like.query.filter_by(
        author=current_user.id, post_id=post_id).first()
    if not post:
        return jsonify({'error': 'Post does not exist.'}, 400)
    elif like:
        db.session.delete(like)
        db.session.commit()
    else:
        like = Like(author=current_user.id, post_id=post_id)
        db.session.add(like)
        db.session.commit()

    return jsonify({"likes": len(post.likes), "liked": current_user.id in map(lambda x: x.author, post.likes)})

@views.route("/update-email", methods=['POST']) 
@login_required 
def update_email():
    update_em_form = UpdateEmailForm() 
    if update_em_form.validate_on_submit():
        user = User.query.get(current_user.id) 
        user.email = update_em_form.email.data 
        db.session.add(user)
        db.session.commit()
        flash("Email updated successfully", category='success')  
    return redirect(url_for('views.profile'))    

@views.route("/update-username", methods=['POST']) 
@login_required 
def update_username():
    update_un_form = UpdateUsernameForm() 
    if update_un_form.validate_on_submit():
        user = User.query.get(current_user.id) 
        user.username = update_un_form.username.data 
        db.session.add(user)
        db.session.commit()
        flash("Username updated successfully", category='success')  
    return redirect(url_for('views.profile'))