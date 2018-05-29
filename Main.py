from __future__ import division
from config.config import keyboard, music_player

import cocos
import menu.MenuCreator
import game.layers.ImageLayer
import pyglet


if __name__ == '__main__':
    sound = pyglet.resource.media('resources/sound/bg-music.mp3')
    music_player.queue(sound)
    music_player.play()

    cocos.director.director.init(
        width=1200,
        height=714,
        caption="Ricks Adventures",
        autoscale=False,
        resizable=False
    )

    # start menu
    background = game.layers.ImageLayer.ImageLayer('resources/img/back.jpg')
    menu_layer = menu.MenuCreator.MenuCreator.create_main_menu()
    menu_scene = cocos.scene.Scene()
    menu_scene.add(menu_layer, z=1)
    menu_scene.add(background, z=0)

    cocos.director.director.window.push_handlers(keyboard)
    cocos.director.director.run(menu_scene)
