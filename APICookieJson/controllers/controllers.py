from typing import Dict

from flask import flash, make_response, redirect, render_template, url_for

from .. import _TOKEN_SPECIAL
from ..core import _Authentication, key_cryptography


def login_controller(auth: _Authentication, form: Dict[str, str]):
    """
    Controller function for handling user login.

    Args:
        auth (_Authentication): An instance of the Authentication class.
        form (Dict[str, str]): A dictionary containing user login form data
            (username and password).

    Returns:
        flask.Response: A Flask response object.
    """

    if auth.is_user(**form):
        __token = key_cryptography(form['password'])

        auth.set_session(__token, form['username'], form['password'])

        response = make_response(redirect(url_for('routes.home')))
        response.set_cookie(_TOKEN_SPECIAL, __token)

        return response

    flash('Nome de usuário e/ou senha incorreto', 'error')
    return redirect(url_for('routes.root'))


def home_controller(auth: _Authentication, cookies: Dict[str, str]):
    """
    Controller function for handling the home page.

    Args:
        auth (_Authentication): An instance of the Authentication class.
        cookies (Dict[str, str]): A dictionary containing cookies from the
            request.

    Returns:
        flask.Response: A Flask response object.
    """

    if _TOKEN_SPECIAL in cookies:
        session = auth.is_token_active(cookies[_TOKEN_SPECIAL])

        if session:
            return render_template("home.html", user=session.get('username'))

    flash('Credenciais inválidas', 'error')
    return redirect('/login')
