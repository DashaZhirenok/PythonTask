from library.API_commands import APICommands


class TestSuiteUpdateCharacter:

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

    def test_update_character(self):
        print("\nupdate exists character")
        commands = APICommands()
        character_dict = APICommands.generate_character(commands, character_name="Vasya0")
        result, status_code = commands.update_character("Vasya0", character_dict)
        # status_code == 500 at 2:20 o'clock 15.05.2019. (system not available or bug ?)
        assert str(status_code) == "200"
        commands.check_character(result['result'])

    def test_update_nonexistent_character(self):
        # Does this command create character if not exist? i think so
        print("\nupdate nonexistent character")
        commands = APICommands()
        character_dict = APICommands.generate_character(commands, character_name="nonexis")
        result, status_code = commands.update_character("nonexis", character_dict)
        assert str(status_code) == "200"
        commands.check_character(result['result'])
