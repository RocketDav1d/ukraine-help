import email
import imp
import secrets
import os
from flask import Blueprint, render_template, redirect, url_for, flash, request
from app.forms import LogInForm, RegisterForm, PostForm, UpdateAccountForm
from app.nav_bar.models import User, Cookie
from app.extenstions.database import db
from werkzeug.security import generate_password_hash, check_password_hash
from flask_login import login_user, login_required, logout_user, current_user
from app.extenstions.login_manager import login_manager
from PIL import Image
from app import app




blueprint = Blueprint("nav_bar", __name__)



# with app.app_context():
#     login_manager = LoginManager()
#     login_manager.init_app(app)
#     login_manager.login_view = "login"

@login_manager.user_loader
def load_user(user_id):
    return User.query.get(int(user_id))



@blueprint.route("/")
def index():
    return render_template("index.html", title="index")


@blueprint.route("/signup", methods=['GET', 'POST'])
def register():
    form = RegisterForm()

    if form.validate_on_submit():
        hashed_password = generate_password_hash(form.password.data, method="sha256")
        # flash(f"Account created for {form.username.data}", "success")
        user = User(name=form.username.data, email=form.email.data, password=hashed_password)
        db.session.add(user)
        db.session.commit()

        return "<h1>New User has been created</h1>"

    return render_template('signup.html', form=form, title="register") 


@blueprint.route("/login", methods=["GET", "POST"])
def login():
    form = LogInForm()
    if form.validate_on_submit():
        user = User.query.filter_by(name=form.username.data).first()
        if user:
            if check_password_hash(user.password, form.password.data):
                login_user(user, remember=form.remember.data)
                # flash(f"Hey {form.username.data}. You logged in successfully", "success")
                return redirect(url_for("nav_bar.dashboard"))
        return "<h1>Invalid username or password</h1>"
    
    return render_template("login.html", form=form, title="login")


@blueprint.route("/dashboard")
@login_required
def dashboard():
    return render_template("dashboard.html", title="dashboard")

@blueprint.route("/logout")
@login_required
def logout():
    logout_user()
    return redirect(url_for("nav_bar.index"))



def save_picture(form_picture):
    random_hex = secrets.token_hex(8)
    _, f_ext = os.path.splitext(form_picture.filename)
    picture_fn = random_hex + f_ext
    picture_path = os.path.join(app.instace_path, 'static/profile_pics', picture_fn)
    form_picture.save(picture_path)
    # output_size = (125, 125)
    # i = Image.open(form_picture)
    # i.thumbnail(output_size)
    # i.save(picture_path)
    return picture_fn

#convert image into base64 string

@blueprint.route("")

@blueprint.route("/account", methods=['GET', 'POST'])
@login_required
def account():
    form = UpdateAccountForm()
    if form.validate_on_submit():
        if form.picture.data:
            picture_file = save_picture(form.picture.data)
            current_user.image_file = picture_file
        current_user.name = form.username.data
        current_user.email = form.email.data
        print()
        db.session.commit()
        flash('Your account has been updated!')
        return redirect(url_for('account'))
    elif request.method == 'GET':
        form.username.data = current_user.name
        form.email.data = current_user.email
    image_file = url_for('static', filename='profile_pics/' + current_user.image_file)
    return render_template('account.html', title='Account',
                           image_file=image_file, form=form)





@blueprint.route("/chat")
def defchat():
    return render_template("chat.html", title="chat")


@blueprint.route("/housing")
def defhousing():
    return render_template("housing.html", title="housing")


@blueprint.route("/supplies")
def defsupplies():
    return render_template("supplies.html", title="supplies")


# def save_picture(form_picture):
#     random_hex = secrets.token_hex(8)
#     _, f_ext = os.path.splitext(form_picture.filename)
#     picture_fn = random_hex + f_ext
#     picture_path = os.path.join(app.root_path, 'static/profile_pics', picture_fn)

#     output_size = (125, 125)
#     i = Image.open(form_picture)
#     i.thumbnail(output_size)
#     i.save(picture_path)

#     return picture_fn


# @blueprint.route("/account")
# def account():
#     form = UpdateAccountForm()
#     if form.validate_on_submit():
#         if form.picture.data:
#             picture_file = save_picture(form.picture.data)
#             current_user.image_file = picture_file
#         current_user.username = form.username.data
#         current_user.email = form.email.data
#         db.session.commit()
#         flash('Your account has been updated!', 'success')
#         return redirect(url_for('account'))
#     elif request.method == 'GET':
#         form.username.data = current_user.username
#         form.email.data = current_user.email
#     image_file = url_for('static', filename='profile_pics/' + current_user.image_file)
#     return render_template('account.html', title='Account',
#                            image_file=image_file, form=form)







@blueprint.route("/post/new", methods=["GET", "POST"])
@login_required
def new_post():
    form = PostForm()
    if form.validate_on_submit():
        flash("Your post has been created", "success")
        return redirect(url_for("nav_bar.defhousing"))
    return render_template("create_post.html", title="New Post", form=form)

