#################
#### imports ####
#################

from flask import render_template, Blueprint, \
    request, flash, redirect, url_for   # pragma: no cover
from flask.ext.login import login_required, current_user   # pragma: no cover

from .forms import MessageForm   # pragma: no cover
from project import db   # pragma: no cover

################
#### config ####
################

home_blueprint = Blueprint(
    'home', __name__,
    template_folder='templates'
)   # pragma: no cover


################
#### routes ####
################

# use decorators to link the function to a url
@home_blueprint.route('/', methods=['GET', 'POST'])   # pragma: no cover
@login_required   # pragma: no cover
def home():
    error = None
    return render_template('welcome.html')


@home_blueprint.route('/welcome')   # pragma: no cover
def welcome():
    return render_template('welcome.html')  # render a template
