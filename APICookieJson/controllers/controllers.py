from typing import Dict

from flask import flash, make_response, redirect, render_template

from .. import _TOKEN_SPECIAL
from ..core import _Authentication, _User, key_cryptography


def login_controller(auth: _Authentication, form: Dict[str, str]):
    if not 'name' in form or 'password' in form:
        flash('Requer nome de usuário e senha.', 'error')
        return redirect('/')

    if auth.is_user(
        form.get('name', ''),
        form.get('password', ''),
    ):
        __token = key_cryptography(form.get('password', ''))
        auth.set_session(
            __token,
            form.get('name', ''),
            form.get('password', ''),
        )

        # response = make_response(redirect('/home'))
        response = 
        response.set_cookie(_TOKEN_SPECIAL, __token)

        return response


def home_controller(auth: _Authentication, cookies: Dict):
    if _TOKEN_SPECIAL in cookies:
        session = auth.is_token_active(_TOKEN_SPECIAL)

        if isinstance(session, _User):
            return render_template("home.html", user=session.get('name'))

    flash('Credenciais inválidas', 'error')
    return redirect('/login')
