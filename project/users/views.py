#################
#### imports ####
#################

from flask import flash, redirect, render_template, request, \
    url_for, Blueprint, Response, json  # pragma: no cover
from flask.ext.login import login_user, \
    login_required, logout_user  # pragma: no cover

from .forms import LoginForm, RegisterForm  # pragma: no cover
from project import db  # pragma: no cover
from project.models import User, bcrypt  # pragma: no cover

################
#### config ####
################

users_blueprint = Blueprint(
    'users', __name__,
    template_folder='templates'
)  # pragma: no cover


################
#### routes ####
################

@users_blueprint.route('/login', methods=['GET', 'POST'])  # pragma: no cover
def login():
    error = None
    form = LoginForm(request.form)
    if request.method == 'POST':
        if form.validate_on_submit():
            user = User.query.filter_by(name=request.form['username']).first()
            if user is not None and bcrypt.check_password_hash(
                    user.password, request.form['password']
            ):
                login_user(user)
                flash('You were logged in. Go Crazy.')
                return redirect(url_for('home.home'))

            else:
                error = 'Invalid username or password.'
    return render_template('login.html', form=form, error=error)


@users_blueprint.route('/logout')  # pragma: no cover
@login_required  # pragma: no cover
def logout():
    logout_user()
    flash('You were logged out.')
    return redirect(url_for('home.welcome'))


@users_blueprint.route(
    '/register/', methods=['GET', 'POST'])  # pragma: no cover
def register():
    form = RegisterForm()
    if form.validate_on_submit():
        print(form.email.data + " " + form.password.data)
        user = User(
            email=form.email.data,
            password=form.password.data,
            emailfb="",
            email_tw="",
            idfb="",
            idtw="")
        try:
            db.session.add(user)
            db.session.commit()
        except Exception as ex:
            return Response(json.dumps({"error": str(ex)}), 500)
        login_user(user)
        return redirect("/welcome")
    return render_template('register.html', form=form)

@users_blueprint.route(
    '/api/fb/register/', methods=['POST'])  # pragma: no cover
def registerApiFb():
    """Register a new user.

        Validates that the username is not already taken. Hashes the
        password for security.
        """

    email_fb = bytes(request.get_json().get("email_fb", ""), "utf-8")
    id_fb = bytes(request.get_json().get("id_fb", ""), "utf-8")
    password = bytes(request.get_json().get("password", ""), "utf-8")

    print("{}".format(email_fb) + " " + "{}".format(id_fb) + "{}".format(password))

    user = User(
        email=email_fb,
        password=password,
        email_fb=email_fb,
        email_tw="",
        id_fb=id_fb,
        id_tw="")
    db.session.add(user)
    db.session.commit()

    # if form.validate_on_submit():
    #     print(form.email.data + " " + form.password.data)
    #     user = User(
    #         email=form.email.data,
    #         password=form.password.data,
    #         emailfb="",
    #         email_tw="",
    #         idfb="",
    #         idtw="")
    #     try:
    #         db.session.add(user)
    #         db.session.commit()
    #     except Exception as ex:
    #         return Response(json.dumps({"error": str(ex)}), 500)
    #     login_user(user)
    return redirect("/welcome")
    # return render_template('register.html', form=form)
