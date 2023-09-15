import json
from pathlib import Path
from typing import Dict


class Cache:
    """A class for managing cache data stored in a JSON file."""

    __path_cache = Path.cwd() / "cache.json"

    __slots__ = ['__content']

    def __init__(self):
        """
        Initializes the Cache instance and loads data from the cache file.
        """

        self.__content = None

        with open(self.__path_cache, 'r', encoding='utf-8') as file:
            self.__content = json.load(file)

        self.__content = self.__content['users']

    @property
    def content(self):
        """
        Property to access the cached content.

        Returns:
            dict: The cached content as a dictionary.
        """

        return self.__content

    def add_session(self, session: Dict[str, str]):
        """
        Adds a session to the cache and updates the cache file.

        Args:
            session (dict): The session data to add to the cache.
        """
        if self.__content:
            with open(self.__path_cache, "w", encoding="utf-8") as file:
                json.dump(session, file)
