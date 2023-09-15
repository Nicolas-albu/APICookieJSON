import secrets
import string
from pathlib import Path

import bcrypt
import toml

from .. import SIZE_TOKEN

CHARS = (
    string.ascii_letters
    + string.digits
    + string.punctuation.translate(str.maketrans('', '', r""" ' " \\ """))
)


def password_cryptography(_password: str) -> str:
    """
    Cryptographically hash a password using bcrypt.

    Args:
        _password (str): The password to be hashed.

    Returns:
        str: The hashed password.
    """

    with open(Path.cwd() / '.secrets.toml', 'r', encoding='utf-8') as file:
        _pass = toml.load(file).get('SECRET_KEY', '').encode('utf-8')

    return bcrypt.hashpw(_password.encode('utf-8'), _pass).decode('utf-8')


def key_cryptography(key: str) -> str:
    """
    Cryptographically hash a key and generate a token.

    Args:
        key (str): The key to be hashed and used to generate a token.

    Returns:
        str: The generated token.
    """

    key = bcrypt.hashpw(key.encode('utf-8'), bcrypt.gensalt()).decode()

    return ''.join(secrets.choice(CHARS) for _ in range(SIZE_TOKEN)) + key
