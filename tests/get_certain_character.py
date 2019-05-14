from library.API_commands import APICommands


class TestSuiteGetAllCharacters:

    def setup_class(self):
        print("\ntest suite setup ")
        commands = APICommands()
        character_dict = APICommands.generate_character(commands, character_name="Vasya")
        result, status_code = commands.get_certain_character("Vasya")
        if str(result['result']) == "No such name":
            commands.add_character(character_dict)
        else:
            commands.delete_character("Vasya")
            commands.add_character(character_dict)

    def teardown_class(self):
        print("\ntest suite teardown")
        commands = APICommands()
        result, status_code = commands.get_certain_character("Vasya")
        if str(result['result']) != "No such name":
            commands.delete_character("Vasya")

    def test_get_certain_character(self):
        print("\nget character that exists by valid user")
        commands = APICommands()
        result, status_code = commands.get_certain_character("Vasya")
        assert str(status_code) == "200"
        commands.check_character(result['result'][0])

    def test_get_character_by_invalid_password(self):
        print("\nget character that exists by INVALID password for user")
        commands = APICommands()
        error, status_code = commands.get_certain_character("Vasya", "some_login", "some_password")
        assert str(status_code) == "401" and str(error['error']) == "You have to login with proper credentials"

    def test_get_nonexistent_character(self):
        print("\nget character that doesn't exist by valid user")
        commands = APICommands()
        result, status_code = commands.get_certain_character("nonexistent_user")
        assert str(status_code) == "200" and str(result['result']) == "No such name"
