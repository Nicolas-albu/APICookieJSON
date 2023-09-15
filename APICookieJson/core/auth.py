from typing import List, TypedDict

from .cache import Cache


class AuthenticationError(Exception):
    """Custom exception for authentication errors."""

    def __init__(self, *args):
        super().__init__(*args)


class _User(TypedDict):
    """Typed dictionary representing a user."""

    username: str
    password: str


class _Session(TypedDict):
    """Typed dictionary representing an authentication session."""

    token: str
    user: _User


class _Authentication:
    """Authentication class for managing users and sessions."""

    def __init__(self, cache: Cache):
        """
        Initializes the Authentication instance.

        Args:
            cache (Cache): The cache instance to retrieve user data.
        """

        self.__users: List[_User] = cache.content  # type: ignore
        self.__sessions: List[_Session] = []

    def is_token_active(self, token: str) -> None | _User:
        """
        Checks if a token is active and returns the associated user if found.

        Args:
            token (str): The authentication token to check.

        Returns:
            None | _User: Returns None if the token is not found, or the
                associated user if found.
        """

        for _session in self.__sessions:
            if token == _session.get("token"):
                return _session["user"]

    def is_user(self, username: str, password: str) -> bool:
        """
        Checks if a user with the given username and password exists.

        Args:
            username (str): The username to check.
            password (str): The password to check.

        Returns:
            bool: True if a user with the provided credentials exists,
                False otherwise.
        """

        for _user in self.__users:
            if (username, password) == tuple(_user.values()):
                return True

        return False

    def set_session(self, token: str, username: str, password: str):
        """
        Creates and stores an authentication session for a user.

        Args:
            token (str): The authentication token for the session.
            username (str): The username of the authenticated user.
            password (str): The password of the authenticated user.
        """

        self.__sessions.append(
            {
                "token": token,
                "user": {"username": username, "password": password},
            }
        )
