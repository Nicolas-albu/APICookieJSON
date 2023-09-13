from typing import List, Optional, TypedDict


class _User(TypedDict):
    name: str
    password: str


class _Token(TypedDict):
    token: str
    user: _User


class Authentication:
    def __init__(self):
        self.__users: _User = {}  # type: ignore
        self.__sessions: List[_Token] = []

    def is_token_in_session(
        self,
        token: str,
        session: Optional[_User] = None,
    ) -> bool | _User:
        for _session in self.__sessions:
            if token == _session.get("token"):
                return _session.get("user")

        return False
