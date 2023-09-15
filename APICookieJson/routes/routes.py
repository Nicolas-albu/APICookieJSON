from flask import Blueprint, flash, redirect, render_template, request, url_for

from ..controllers import home_controller, login_controller
from ..core import Cache, _Authentication, password_cryptography

routes = Blueprint('routes', __name__)


_auth = _Authentication(Cache())


@routes.route('/')
def root():
    """
    Route for the root (index) page.

    Returns:
        flask.Response: A Flask response object with the rendered index.html
            template.
    """

    return render_template('index.html')


@routes.route('/login', methods=['POST'])
def login():
    """
    Route for handling user login.

    Returns:
        flask.Response: A Flask response object that may redirect to the home
            page or display an error message.
    """

    if '' in request.form.values():
        flash('Por favor, preencha todos os campos', 'error')
        return redirect(url_for('routes.root'))

    _form = request.form.to_dict()
    _form['password'] = password_cryptography(request.form['password'])

    return login_controller(auth=_auth, form=_form)


@routes.route("/home")
def home():
    """
    Route for the home page.

    Returns:
        flask.Response: A Flask response object that may display the home page
            or an error message.
    """
    return home_controller(auth=_auth, cookies=request.cookies)
