from library.API_commands import APICommands


class TestSuiteDelCharacter:

    def setup(self):
        print("\ntest case setup ")
        commands = APICommands()
        # add character if not exists
        result, status_code = commands.get_certain_character("Vasya")
        if str(result['result']) == "No such name":
            character_dict = APICommands.generate_character(commands, character_name="Vasya")
            commands.add_character(character_dict)

    def teardown(self):
        print("\ntest case teardown")
        commands = APICommands()
        result, status_code = commands.get_certain_character("Vasya")
        # delete character if exists after test suite
        if str(result['result']) != "No such name":
            commands.delete_character("Vasya")

    def test_case_del_character(self):
        print("\ndelete character that exists")
        commands = APICommands()
        result, status_code = commands.delete_character("Vasya")
        assert str(status_code) == "200" and "is deleted" in str(result["result"])

    def test_case_del_character_by_invalid_user(self):
        print("\ndelete character that exists by INVALID user")
        commands = APICommands()
        error, status_code = commands.delete_character("Vasya", "some_login", "some_password")
        assert str(status_code) == "401" and str(error['error']) == "You have to login with proper credentials"

    def test_case_del_nonexistent_character(self):
        print("\ndelete nonexistent character")
        commands = APICommands()
        result, status_code = commands.delete_character("Vasya")
        assert str(status_code) == "200" and "is deleted" in str(result["result"])
        result, status_code = commands.delete_character("Vasya")
        assert str(status_code) == "200" and str(result["result"][0]) == "No such name"

