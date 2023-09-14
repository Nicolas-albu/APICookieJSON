import secrets
import string
from pathlib import Path

import bcrypt
import toml

from .. import SIZE_TOKEN


def password_cryptography(_password: str) -> str:
    with open(Path.cwd() / '.secrets.toml', 'r', encoding='utf-8') as file:
        _pass = toml.load(file).get('SECRET_KEY', '')

    return str(bcrypt.hashpw(_password.encode('utf-8'), _pass))


def key_cryptography(key: str) -> str:
    chars = string.ascii_letters + string.digits + string.punctuation

    return ''.join(secrets.choice(chars) for _ in range(SIZE_TOKEN)) + str(
        bcrypt.hashpw(key.encode('utf-8'), bcrypt.gensalt())
    )
