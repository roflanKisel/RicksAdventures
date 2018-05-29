import math
import time
import cocos
import cocos.text
import pyglet
import game.layers.ImageLayer
import menu.MenuCreator

from cocos.scenes.transitions import SplitColsTransition
from config.config import collision_manager
from game.controller.ActionController import ActionController
from game.services.CollisionService import CollisionService
from game.services.GameService import GameService
from config.config import music_player


class Game(cocos.layer.Layer):
    is_event_handler = True

    def __init__(self, level, player, boss):
        super(Game, self).__init__()
        collision_manager.clear()
        self.__score = 0
        self.__start_time = time.time()

        self.player = player
        self.boss = boss

        # init batch nodes
        self.walls = cocos.batch.BatchNode()
        self.spines = cocos.batch.BatchNode()
        self.enemies = cocos.batch.BatchNode()
        self.portals = cocos.batch.BatchNode()
        self.textures = cocos.batch.BatchNode()
        self.bitcoins = cocos.batch.BatchNode()

        # getting objects from level obj
        self.all_walls = level.get_all_walls()
        self.all_spines = level.get_all_spines()
        self.all_enemies = level.get_all_enemies()
        self.all_portals = level.get_all_portals()
        self.all_textures = level.get_all_textures()
        self.all_bitcoins = level.get_all_bitcoins()

        Game.__init_batch_walls(((self.walls, self.all_walls), (self.spines, self.all_spines)))
        Game.__init_batch_entities(((self.enemies, self.all_enemies), (self.portals,self.all_portals),
                                    (self.textures, self.all_textures), (self.bitcoins, self.all_bitcoins)))

        self.__add_layers(((self.boss, 1), (self.player, 2), (self.walls, 1), (self.spines, 1),
                           (self.enemies, 2), (self.portals, 2), (self.textures, 1), (self.bitcoins, 1)))

        collision_manager.add(self.player)
        collision_manager.add(self.boss)
        self.player.do(ActionController())

        self.schedule(self.update)

    @staticmethod
    def __init_batch_walls(walls):
        for wall in walls:
            CollisionService.wall_init_batch_node(collision_manager, wall[0], wall[1])

    @staticmethod
    def __init_batch_entities(entities):
        for entity in entities:
            CollisionService.entity_init_batch_node(collision_manager, entity[0], entity[1])

    def __add_layers(self, layers):
        for layer in layers:
            self.add(layer[0], z=layer[1])

    def update(self, dt):
        self.player.cshape.center = self.player.position

        # updating enemy cshapes
        for enemy in self.all_enemies:
            enemy.cshape.center = enemy.position

        collisions = collision_manager.objs_colliding(self.player)

        # updating and checking collisions
        boss_in_collisions = self.boss in collisions
        enemy_in_collisions = GameService.collision_handler(self.all_enemies, collisions)
        spine_in_collisions = GameService.is_batch_in_collisions(self.all_spines, collisions)
        portal_in_collisions = GameService.collision_handler(self.all_portals, collisions)
        bitcoin_in_collisions = GameService.collision_handler(self.all_bitcoins, collisions)

        if boss_in_collisions:
            Game.switch_to_menu('WIN', self.__score, time.time() - self.__start_time)
        elif enemy_in_collisions or spine_in_collisions:
            Game.switch_to_menu('LOSE', self.__score, time.time() - self.__start_time)
        elif portal_in_collisions:
            portal = portal_in_collisions
            self.player.position = portal.get_next_position()
        elif bitcoin_in_collisions:
            bitcoin_in_collisions.image = pyglet.resource.image('resources/img/null.png')
            self.all_bitcoins.remove(bitcoin_in_collisions)
            self.__score += 1

    @staticmethod
    def on_quit():
        music_player.delete()
        cocos.director.director.terminate_app = True

    @staticmethod
    def switch_to_menu(result, score, delta_time):
        if result == "LOSE":
            label1 = cocos.text.Label(text=result, font_size=50, position=(520, 480), color=(255, 7, 7, 255))
        elif result == "WIN":
            label1 = cocos.text.Label(text=result, font_size=50, position=(540, 480), color=(7, 255, 7, 255))
        else:
            label1 = cocos.text.Label(text="MAIN MENU", font_size=50, position=(540, 480), color=(255, 255, 255, 255))
        label2 = cocos.text.Label(text="SCORE: " + str(score) + " btc", font_size=30, position=(449, 150))
        label3 = cocos.text.Label(text="TIME: " + str(math.floor(delta_time)) + " sec",
                                  font_size=30, position=(490, 200))
        menu_layer = menu.MenuCreator.MenuCreator.create_main_menu()
        background = game.layers.ImageLayer.ImageLayer('resources/img/back.jpg')
        menu_scene = cocos.scene.Scene(background)
        menu_scene.add(label1)
        menu_scene.add(label2)
        menu_scene.add(label3)
        menu_scene.add(menu_layer)
        cocos.director.director.replace(SplitColsTransition(menu_scene))
