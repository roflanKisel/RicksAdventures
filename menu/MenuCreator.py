from menu.MainMenu import MainMenu
from menu.items.TextMenuItem import TextMenuItem


class MenuCreator:
    @staticmethod
    def create_main_menu():
        main_menu = MainMenu()
        items = MenuCreator.__create_main_menu_items()
        main_menu.create_menu(items)
        return main_menu

    @staticmethod
    def create_level_menu():
        level_menu = MainMenu()
        items = MenuCreator.__create_level_menu_items()
        level_menu.create_menu(items)
        return level_menu

    @staticmethod
    def __create_main_menu_items():
        text_list = ["New game", "Exit"]
        callback_func_list = [MenuCreator.on_game_start(),
                              MenuCreator.on_exit()]
        items = MenuCreator.__create_text_items(text_list, callback_func_list)
        return items

    @staticmethod
    def __create_level_menu_items():
        text_list = ["Level 1", "Level 2"]
        callback_func_list = [MenuCreator.on_level_1(),
                              MenuCreator.on_level_2()]
        items = MenuCreator.__create_text_items(text_list, callback_func_list)
        return items

    @staticmethod
    def __create_text_items(text_list, callback_func_list):
        length = len(text_list)
        i = 0
        item_list = []
        while i < length:
            item_list.append(TextMenuItem(text_list[i], callback_func_list[i]))
            i += 1
        return item_list

    @staticmethod
    def on_game_start():
        print("Game start")

    @staticmethod
    def on_exit():
        print("Exit")

    @staticmethod
    def on_level_1():
        print("Level 1")

    @staticmethod
    def on_level_2():
        print("Level 2")
