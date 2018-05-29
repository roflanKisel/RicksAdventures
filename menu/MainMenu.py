from __future__ import division, print_function, unicode_literals
import cocos


class MainMenu(cocos.menu.Menu):
    def __init__(self):
        super(MainMenu, self).__init__()

    # ban mouse moves
    def on_mouse_release(self, x, y, buttons, modifiers):
        pass

    def on_mouse_motion(self, x, y, dx, dy):
        pass

    @staticmethod
    def on_quit():
        cocos.director.director.terminate_app = True
