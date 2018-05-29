import cocos
from cocos.actions import MoveBy
from cocos.actions import Repeat
from cocos.actions import Reverse
from cocos.actions.interval_actions import MoveTo

import game.entities.Player
import game.entities.enemies.Enemy
import game.scenes.Level
from game.controller.Game import Game
from game.entities.enemies.Enemy import Enemy
from game.entities.portals.Portal import Portal
from game.entities.textures.Texture import Texture
from game.layers.ImageLayer import ImageLayer
from game.services.WallCreator import WallCreator


class Level1:
    @staticmethod
    def get_game_scene():
        # creating object of Level class and add diff things to this
        player = game.entities.Player.Player("resources/img/roflan.png", (75, 80), (0, 0), 150)
        boss = game.entities.enemies.Enemy.Enemy("resources/img/bounty.png", (600, 370))
        boss.do(cocos.actions.Repeat(cocos.actions.Waves3D(
            waves=3, amplitude=40, grid=(16, 16))))
        level = game.scenes.Level.Level()

        horizontal_walls = (
            ([32, 20], 8),
            ([600, 20], 8),
            ([1169, 20], 2),
            ([32, 693], 8),
            ([594, 693], 10),
            ([140, 278], 1),
            ([320, 135], 2),
            ([329, 601], 2),
            ([264, 472], 1),
            ([480, 451], 1),
            ([480, 285], 1),
            ([1090, 285], 2),
        )

        vertical_walls = (
            ([20, 72], 8),
            ([20, 637], 2),
            ([1180, 72], 13),
            ([180, 266], 1),
            ([140, 420], 1),
            ([434, 147], 3),
            ([314, 460], 1),
            ([434, 463], 3),
            ([722, 70], 2),
            ([722, 270], 1),
            ([832, 70], 2),
            ([942, 70], 2),
            ([1052, 70], 2),
        )

        horizontal_spines = (
            ([74, 474], 3),
            ([544, 451], 6),
            ([1000, 451], 3),
            ([544, 285], 3),
            ([774, 285], 5)
        )

        vertical_spines = (
            ([180, 74], 3),
            ([315, 270], 3),
            ([434, 75], 1),
            ([496, 336], 2)

        )

        for wall in horizontal_walls:
            level.add_wall(WallCreator.create_horizontal_walls(
                "resources/img/stone_h.png",
                wall[0], wall[1]
            ))

        for wall in vertical_walls:
            level.add_wall(WallCreator.create_vertical_walls(
                "resources/img/stone_v.png",
                wall[0], wall[1]
            ))

        for spine in horizontal_spines:
            level.add_spine(WallCreator.create_horizontal_walls(
                "resources/img/prov_h.png",
                spine[0], spine[1], 'spine'
            ))

        for spine in vertical_spines:
            level.add_spine(WallCreator.create_vertical_walls(
                "resources/img/prov_v.png",
                spine[0], spine[1], 'spine'
            ))

        level.add_portal(Portal("resources/img/portal_v.png", [20, 574], (537, 75)))
        level.add_portal(Portal("resources/img/portal_h.png", [537, 20], (75, 574)))
        level.add_portal(Portal("resources/img/portal_h.png", [1105, 20], (535, 637)))
        level.add_portal(Portal("resources/img/portal_h.png", [535, 693], (1105, 70)))

        guns = ((1130, 610), (1130, 520))
        for pos in guns:
            gun = Texture("resources/img/pushka.png", pos)
            gun.do(Repeat(cocos.actions.AccelDeccel(cocos.actions.RotateBy(180, 1.25))))
            level.add_texture(gun)

        common_textures = ((1100, 400), (1100, 360), (1130, 370))
        for pos in common_textures:
            texture = Texture("resources/img/zachto.png", pos)
            level.add_texture(texture)

        bitcoins = ((300, 80), (80, 420), (480, 240), (775, 80), (885, 80),
                    (995, 80), (480, 500), (680, 565))
        for pos in bitcoins:
            bitcoin = Texture("resources/img/bitcoin.png", pos)
            level.add_bitcoin(bitcoin)

        enemy1 = Enemy("resources/img/buld.png", (75, 420))
        enemy1_moves = Repeat(MoveBy((0, -80), 0.65) +
                              MoveBy((190, 0), 1.5) +
                              Reverse(MoveBy((0, -80), 0.65) +
                                      MoveBy((190, 0), 1.5)))
        enemy1.do(enemy1_moves)
        level.add_enemy(enemy1)

        enemy2 = Enemy("resources/img/buld.png", (370, 190))
        enemy2_moves = Repeat(MoveBy((-130, 0), 0.7) +
                              MoveBy((0, -120), 0.6) +
                              MoveBy((130, 0), 0.7) +
                              Reverse(MoveBy((-130, 0), 0.7) +
                                      MoveBy((0, -120), 0.6) +
                                      MoveBy((130, 0), 0.7)))
        enemy2.do(enemy2_moves)
        level.add_enemy(enemy2)

        enemy3 = Enemy("resources/img/buld.png", (150, 535))
        enemy3_moves = Repeat(MoveBy((220, 0), 1.3) +
                              MoveBy((0, -197), 1) +
                              MoveBy((70, 0), 0.4) +
                              Reverse(MoveBy((220, 0), 1.3) +
                                      MoveBy((0, -197), 1) +
                                      MoveBy((70, 0), 0.4)))
        enemy3.do(enemy3_moves)
        level.add_enemy(enemy3)

        enemy4 = Enemy("resources/img/buld.png", (537, 230))
        enemy4_moves = Repeat(MoveBy((0, -140), 1) +
                              Reverse(MoveBy((0, -140), 1)))
        enemy4.do(enemy4_moves)
        level.add_enemy(enemy4)

        enemy5 = Enemy("resources/img/buld.png", (1130, 200))
        enemy5_moves = Repeat(MoveBy((-400, 0), 1.6) +
                              Reverse(MoveBy((-400, 0), 1.6)))
        enemy5.do(enemy5_moves)
        level.add_enemy(enemy5)

        enemy6 = Enemy("resources/img/roflan2.png", (1070, 610))
        enemy6_moves = Repeat(MoveBy((-580, 0), 2.5) +
                              MoveTo((670, 1000), 0) +
                              MoveTo((1070, 1000), 0) +
                              MoveTo((1070, 610), 0))
        enemy6.do(enemy6_moves)
        level.add_enemy(enemy6)

        enemy7 = Enemy("resources/img/roflan2.png", (1070, 520))
        enemy7_moves = Repeat(MoveBy((-580, 0), 2) +
                              MoveTo((670, 1000), 0) +
                              MoveTo((1070, 1000), 0) +
                              MoveTo((1070, 520), 0))
        enemy7.do(enemy7_moves)
        level.add_enemy(enemy7)

        game_layer = Game(level, player, boss)
        game_scene = cocos.scene.Scene()

        image_layer = ImageLayer("resources/img/back3.jpg")
        image_layer.do(cocos.actions.Repeat(cocos.actions.Waves3D(
            waves=1, amplitude=20, grid=(8, 8)) +
                                            cocos.actions.Reverse(
                                                cocos.actions.Waves3D(
                                                    waves=1, amplitude=20, grid=(8, 8))
                                            )))

        game_scene.add(image_layer)
        game_scene.add(game_layer)
        return game_scene

