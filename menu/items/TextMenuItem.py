import cocos
import menu.MenuCreator
import game.layers.ImageLayer
from cocos.scenes.transitions import FadeTRTransition, SplitColsTransition
from config.config import music_player
from game.levels.Level1 import Level1
from game.levels.Level2 import Level2


class TextMenuItem(cocos.menu.MenuItem):
    def __init__(self, label, callback_func, *args, **kwargs):
        super(TextMenuItem, self).__init__(label, callback_func, *args, **kwargs)

    def on_activated(self):
        if self.label == 'New game':
            background = game.layers.ImageLayer.ImageLayer('resources/img/back.jpg')
            level_scene = cocos.scene.Scene(background)
            level_scene.add(menu.MenuCreator.MenuCreator.create_level_menu())
            cocos.director.director.replace(SplitColsTransition(level_scene))
        elif self.label == 'Exit':
            music_player.delete()
            cocos.director.director.terminate_app = True
        elif self.label == 'Level 1':
            game_scene = Level1.get_game_scene()
            cocos.director.director.replace(FadeTRTransition(game_scene))
        elif self.label == 'Level 2':
            game_scene = Level2.get_game_scene()
            cocos.director.director.replace(FadeTRTransition(game_scene))
