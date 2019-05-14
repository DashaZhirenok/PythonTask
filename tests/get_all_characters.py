from library.API_commands import APICommands


class TestSuiteGetAllCharacters:

    def setup(self):
        print("basic setup into class")

    def teardown(self):
        print("basic teardown into class")

    def test_get_all_characters_by_valid_user(self):
        commands = APICommands()
        all_characters, status_code = commands.get_all_characters()
        assert str(status_code) == "200"

    def test_get_all_characters_by_invalid_user(self):
        commands = APICommands()
        error, status_code = commands.get_all_characters("some_login", "some_password")
        assert str(status_code) == "401" and str(error['error']) == "You have to login with proper credentials"

