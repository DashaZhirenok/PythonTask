from library.API_commands import APICommands


class TestSuiteAddCharacter:

    def setup(self):
        print("\ntest case setup ")
        # del 1 character if exists
        commands = APICommands()
        commands.del_some_characters("Vasya", 1)

    def teardown(self):
        print("\ntest case teardown")
        # delete 1 character if exists after test case
        commands = APICommands()
        commands.del_some_characters("Vasya", 1)

    def test_add_character(self):
        print("\nadd valid character")
        commands = APICommands()
        character_dict = APICommands.generate_character(commands, character_name="Vasya0")
        result, status_code = commands.add_character(character_dict)
        assert str(status_code) == "200"
        commands.check_character(result['result'])

    def test_add_already_exist_character(self):
        print("\nadd character that already exists")
        commands = APICommands()
        character_dict = APICommands.generate_character(commands, character_name="Vasya0")
        commands.add_character(character_dict)
        result, status_code = commands.add_character(character_dict)
        assert str(status_code) == "200" and str((result['result'])) == "Vasya0 is already exists"

    def test_add_character_by_invalid_user(self):
        print("\nadd valid character by INVALID user")
        commands = APICommands()
        character_dict = APICommands.generate_character(commands, character_name="Vasya0")
        error, status_code = commands.add_character(character_dict, "some_login", "some_password")
        assert str(status_code) == "401" and str(error['error']) == "You have to login with proper credentials"
