from flask import Blueprint, render_template, request

from ..controllers import home_controller, login_controller
from ..core import _Authentication, password_cryptography

routes = Blueprint('routes', __name__)

_auth = _Authentication()


@routes.route('/')
def root():
    return render_template('index.html')


@routes.route('/login', methods=['POST'])
def login():
    _pass = password_cryptography(request.form['password'])

    form = {'name': request.form['name'], 'password': _pass}

    return login_controller(auth=_auth, form=form)


@routes.route("/home")
def home():
    return home_controller(auth=_auth, cookies=request.cookies)
