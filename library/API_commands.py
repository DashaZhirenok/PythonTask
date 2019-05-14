# -*- coding: utf-8 -*-
import requests
import json


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

    def add_character(self, character_dict, login=LOGIN, password=PASSWORD):
        """
        add information about character

        :param character_dict: dict with character. for example:
        {"name": "Hawkeye", "universe": "Marvel Universe",
           "education": "High school (unfinished)", "weight": 104,
           "height": 1.90, "identity": "Publicly known",
           "other_aliases": "None"}
        :param login: login for authorization
        :param password: password for authorization
        :return: response(json), status_code
        """
        headers = {"Content-type": "application/json", "Content-Encoding": "utf-8"}
        response = requests.post(url=self.base_url + "/character", auth=(login, password), headers=headers,
                                 data=json.dumps(character_dict))
        return response.json(), response.status_code

    def update_character(self, character_name, character_dict, login=LOGIN, password=PASSWORD):
        """
        update information about character by name
        :param character_name: name of character(string)
        :param character_dict: dict with character. for example:
        {"name": "Hawkeye", "universe": "Marvel Universe",
           "education": "High school (unfinished)", "weight": 104,
           "height": 1.90, "identity": "Publicly known",
           "other_aliases": "None"}
        :param login: login for authorization
        :param password: password for authorization
        :return: response(json), status_code
        """
        headers = {"Content-type": "application/json", "Content-Encoding": "utf-8"}
        response = requests.put(url=self.base_url + "/character/" + character_name, auth=(login, password), headers=headers,
                                 data=json.dumps(character_dict))
        return response.json(), response.status_code

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

    # helpful functions
    def check_character(self, character_dict):
        keys = ["name", "universe", "education", "weight", "height", "identity", "other_aliases"]
        # todo check that in keys valid values
        for cur_key in keys:
            assert cur_key in character_dict
        pass

    def generate_character(self, character_name="Hawkeye", character_universe="Marvel Universe",
                       character_education="High school (unfinished)", character_weight=104,
                       character_height=1.90, character_identity="Publicly known", character_other_aliases="None"):
        """
        generate character by params
        :return: character_dict
        """
        character_dict = {}
        character_dict.update({"name": character_name, "universe": character_universe, "education": character_education,
                              "weight": character_weight, "height": character_height, "identity": character_identity,
                               "other_aliases": character_other_aliases})
        return character_dict

    def add_some_characters(self, character_name="Vasya", number_of_characters=1):
        commands = APICommands()
        i = 0
        while i < number_of_characters:
            result, status_code = commands.get_certain_character(character_name + str(i))
            if str(result['result']) == "No such name":
                character_dict = APICommands.generate_character(commands, character_name=character_name + str(i))
                commands.add_character(character_dict)
                result, status_code = commands.get_certain_character(character_name + str(i))
                commands.check_character(result['result'][0])
            i += 1

    def del_some_characters(self, character_name="Vasya", number_of_characters=1):
        commands = APICommands()
        i = 0
        while i < number_of_characters:
            result, status_code = commands.get_certain_character(character_name + str(i))
            if str(result['result']) != "No such name":
                commands.delete_character(character_name + str(i))
            i += 1
