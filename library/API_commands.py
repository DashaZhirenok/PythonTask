# -*- coding: utf-8 -*-
import requests


class APICommands:
    LOGIN = "dashazhirenok@yandex.ru"
    PASSWORD = "hgJH768Cv23"

    def __init__(self):
        self.base_url = "http://rest.test.ivi.ru"

    def get_all_characters(self, login=LOGIN, password=PASSWORD):
        """
        get information about all characters
        :param login: login for authorization
        :param password: password for authorization
        :return: response(json), status_code
        """
        response = requests.get(url=self.base_url + "/characters", auth=(login, password))
        return response.json(), response.status_code

    def get_certain_character(self, character_name,  login=LOGIN, password=PASSWORD):
        """
        get information about certain character by name
        :param character_name: name of character(string)
        :param login: login for authorization
        :param password: password for authorization
        :return: response(json), status_code
        """
        response = requests.get(url=self.base_url + "/character/" + character_name, auth=(login, password))
        return response.json(), response.status_code

    def create_character(self, character, login=LOGIN, password=PASSWORD):
        """
        create information about character
        POST / character
        """

    def update_character(self, character_name, login=LOGIN, password=PASSWORD):
        """
        update information about character by name
        PUT / character / {name}
        """

    def delete_character(self, character_name, login=LOGIN, password=PASSWORD):
        """
        delete information about certain character by name
        :param character_name: name of character(string)
        :param login: login for authorization
        :param password: password for authorization
        :return: response(json), status_code
        """
        response = requests.delete(url=self.base_url + "/character/" + character_name, auth=(login, password))
        return response.json(), response.status_code

    def check_character(self, character):
        # todo
        if character:
            assert True
        pass


# commands = APICommands()
# commands.get_all_characters()
# commands.get_certain_character("Absorbing Man")
# commands.delete_character("3-D Man")
