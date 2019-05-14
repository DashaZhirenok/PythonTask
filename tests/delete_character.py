from library.API_commands import APICommands


class TestSuiteDelCharacter:

    def setup(self):
        print("\ntest case setup ")
        # add character if not exists
        commands = APICommands()
        commands.add_some_characters("Vasya", 1)

    def teardown(self):
        print("\ntest case teardown")
        # delete character if exists after test case
        commands = APICommands()
        commands.del_some_characters("Vasya", 1)

    def test_case_del_character(self):
        print("\ndelete character that exists")
        commands = APICommands()
        result, status_code = commands.delete_character("Vasya0")
        assert str(status_code) == "200" and "is deleted" in str(result["result"])

    def test_case_del_character_by_invalid_user(self):
        print("\ndelete character that exists by INVALID user")
        commands = APICommands()
        error, status_code = commands.delete_character("Vasya0", "some_login", "some_password")
        assert str(status_code) == "401" and str(error['error']) == "You have to login with proper credentials"

    def test_case_del_nonexistent_character(self):
        print("\ndelete nonexistent character")
        commands = APICommands()
        result, status_code = commands.delete_character("Vasya0")
        assert str(status_code) == "200" and "is deleted" in str(result["result"])
        result, status_code = commands.delete_character("Vasya0")
        assert str(status_code) == "200" and str(result["result"][0]) == "No such name"

