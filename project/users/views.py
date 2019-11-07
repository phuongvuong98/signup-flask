from flask import flash, redirect, render_template, request, \
    url_for, Blueprint, Response, json
from flask.ext.login import login_user, \
    login_required, logout_user

from .forms import LoginForm, RegisterForm
from project import db
from project.models import User, bcrypt
from functools import wraps


users_blueprint = Blueprint(
    'users', __name__,
    template_folder='templates'
)

def to_json(func):
    @wraps(func)
    def wrapper(*args, **kwargs):
        get_fun = func(*args, **kwargs)
        return json.dumps(get_fun)

    return wrapper


@users_blueprint.route('/logout')
@login_required
def logout():
    logout_user()
    flash('You were logged out.')
    return redirect(url_for('home.welcome'))


@users_blueprint.route(
    '/register', methods=['GET', 'POST'])
def register():
    form = RegisterForm()
    if form.validate_on_submit():
        user_exist_fb = User.query.filter_by(email=form.email.data).first()
        if user_exist_fb == None:
            user = User(
                email=form.email.data,
                password=form.password.data,
                email_fb="",
                email_tw="",
                id_fb="",
                id_tw="")
            db.session.add(user)
            db.session.commit()
            flash('You sign up successful.')
            return redirect("/register")
        else: flash('You sign up fail.')
    return render_template('register.html', form=form)

@users_blueprint.route('/api/fb/register', methods=['POST'])
@to_json
def registerApiFb():
    id_fb = request.json['id_fb']
    email_fb = request.json['email_fb']
    user_exist_fb = User.query.filter_by(id_fb=id_fb).first()
    if user_exist_fb == None:
        user = User(
        email=email_fb,
        password="",
        email_fb=email_fb,
        email_tw="",
        id_fb=id_fb,
        id_tw="")
        db.session.add(user)
        # login_user(user.id)
        db.session.commit()
        return True
    return False
