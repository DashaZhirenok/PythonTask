from library.API_commands import APICommands


class TestSuiteGetAllCharacters:

    def setup_class(cls):
        print("\nsetup in class")
        # commands = APICommands()
        # error, status_code = commands.get_certain_character("nonexistent_user", "some_login", "some_password")
        # if str(status_code) == "401" and str(error['error']) == "You have to login with proper credentials"

    def teardown_class(cls):
        print("\nteardown in class")

    def test_get_certain_character_by_valid_user(self):
        commands = APICommands()
        result, status_code = commands.get_certain_character("Absorbing Man")
        print(result['result'])
        commands.check_character(result)
        assert str(status_code) == "200"

    def test_get_character_by_invalid_user(self):
        commands = APICommands()
        error, status_code = commands.get_certain_character("Absorbing Man", "some_login", "some_password")
        assert str(status_code) == "401" and str(error['error']) == "You have to login with proper credentials"

    def test_get_nonexistent_character(self):
        commands = APICommands()
        result, status_code = commands.get_certain_character("nonexistent_user")
        assert str(status_code) == "200" and str(result['result']) == "No such name"

