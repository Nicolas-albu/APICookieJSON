from flask import Blueprint, render_template, request

from .. import _TOKEN_SPECIAL
from ..core import Authentication

routes = Blueprint('routes', __name__)


@routes.route('/')
def root():
    return "ola"


@routes.route("/home")
def home():
    _auth = Authentication()

    if _TOKEN_SPECIAL in request.cookies and (
        session := _auth.is_token_in_session(_TOKEN_SPECIAL)
    ):
        user, *_ = session  # type: ignore
        return render_template("home.html", user=user)

    return render_template('error.html')
