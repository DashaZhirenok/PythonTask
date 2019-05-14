from library.API_commands import APICommands


class TestSuiteGetAllCharacters:

    def setup(self):
        print("\ntest case setup ")
        # add 3 character if not exists
        commands = APICommands()
        commands.add_some_characters("Vasya", 3)

    def teardown(self):
        print("\ntest case teardown")
        # delete 3 character if exists after test case
        commands = APICommands()
        commands.del_some_characters("Vasya", 3)

    def test_get_all_characters(self):
        print("\nget all characters. Actions:")
        print("\n1. add 3 character")
        print("\n2. get all characters, but check 3(exist)")
        print("\n3. del 3 character")
        commands = APICommands()
        all_characters, status_code = commands.get_all_characters()
        assert str(status_code) == "200"
        # todo удалить базу и проверить, что все верные возвращаются
        # сделана проверка хотя бы 3 штуки
        all_characters = all_characters['result']
        i = 0
        for cur_character in all_characters:
            if "Vasya" in cur_character["name"]:
                commands.check_character(cur_character)
                i += 1
        assert i == 3

    def test_get_all_characters_after_deleting(self):
        print("\nget all characters. Actions:")
        print("\n1. del 3 characters if exists")
        print("\n2. get all characters, but check 3(not exist)")
        commands = APICommands()
        commands.del_some_characters("Vasya", 3)
        all_characters, status_code = commands.get_all_characters()
        assert str(status_code) == "200"
        all_characters = all_characters['result']
        i = 0
        for cur_character in all_characters:
            if cur_character["name"] == ("Vasya0" or "Vasya1" or "Vasya2"):
                i += 1

        assert i == 0

    def test_get_all_characters_by_invalid_password(self):
        print("\nget all characters by INVALID password for user")
        commands = APICommands()
        error, status_code = commands.get_all_characters("some_login", "some_password")
        assert str(status_code) == "401" and str(error['error']) == "You have to login with proper credentials"
