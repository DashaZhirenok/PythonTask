from library.API_commands import APICommands


class TestSuiteAddCharacter:

    def setup(self):
        print("\ntest case setup ")
        commands = APICommands()
        # delete character if exists, else add character
        result, status_code = commands.get_certain_character("Vasya")
        if str(result['result']) != "No such name":
            commands.delete_character("Vasya")

    def teardown(self):
        print("\ntest case teardown")
        commands = APICommands()
        result, status_code = commands.get_certain_character("Vasya")
        # delete character if exists after test suite
        if str(result['result']) != "No such name":
            commands.delete_character("Vasya")

    def test_add_character(self):
        print("\nadd valid character")
        commands = APICommands()
        character_dict = APICommands.generate_character(commands, character_name="Vasya")
        result, status_code = commands.add_character(character_dict)
        assert str(status_code) == "200"
        commands.check_character(result['result'])

    def test_add_already_exist_character(self):
        print("\nadd character that already exists")
        commands = APICommands()
        character_dict = APICommands.generate_character(commands, character_name="Vasya")
        commands.add_character(character_dict)
        result, status_code = commands.add_character(character_dict)
        assert str(status_code) == "200" and str((result['result'])) == "Vasya is already exists"

    def test_add_character_by_invalid_user(self):
        print("\nadd valid character by INVALID user")
        commands = APICommands()
        character_dict = APICommands.generate_character(commands, character_name="Vasya")
        error, status_code = commands.add_character(character_dict, "some_login", "some_password")
        assert str(status_code) == "401" and str(error['error']) == "You have to login with proper credentials"
