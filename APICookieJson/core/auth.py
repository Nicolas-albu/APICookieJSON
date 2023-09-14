from typing import List, TypedDict


class _User(TypedDict):
    name: str
    password: str


class _Token(TypedDict):
    token: str
    user: _User


class _Authentication:
    def __init__(self):
        self.__users: List[_User] = []
        self.__sessions: List[_Token] = []

    def is_token_active(self, token: str) -> bool | _User:
        for _session in self.__sessions:
            if token == _session.get("token"):
                return _session.get("user")

        return False

    def is_user(self, username: str, password: str) -> bool:
        for _user in self.__users:
            if (username, password) == _user.values():
                return True

        return False

    def set_session(self, token: str, username: str, password: str) -> None:
        self.__sessions.append(
            {
                "token": token,
                "user": {"name": username, "password": password},
            }
        )
