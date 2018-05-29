import cocos
import game.entities.Player
import game.entities.enemies.Enemy
import game.scenes.Level

from cocos.actions import MoveBy
from cocos.actions import Repeat
from cocos.actions import Reverse
from game.controller.Game import Game
from game.entities.enemies.Enemy import Enemy
from game.entities.portals.Portal import Portal
from game.entities.textures.Texture import Texture
from game.layers.ImageLayer import ImageLayer
from game.services.WallCreator import WallCreator


class Level2:
    @staticmethod
    def get_game_scene():
        # creating object of Level class and add diff things to this
        player = game.entities.Player.Player("resources/img/roflan.png", (100, 100), (0, 0), 150)
        boss = game.entities.enemies.Enemy.Enemy("resources/img/haste.png", (1100, 600))
        level = game.scenes.Level.Level()

        horizontal_walls = (
            ([62, 696], 18),
            ([62, 20], 18),
            ([62, 450], 6),
            ([62, 180], 16)
        )

        vertical_walls = (
            ([20, 32], 14),
            ([1180, 32], 14),
            ([220, 225], 9),
            ([420, 225], 9)
        )

        horizontal_spines = (
            ([560, 290], 10),
            ([470, 400], 10),
            ([560, 510], 10)
        )

        vertical_spines = (
            ([250, 70], 2),
            ([480, 70], 2),
            ([710, 70], 2),
            ([940, 70], 2)
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

        level.add_portal(Portal("resources/img/portal_h.png", [180, 20], (360, 620)))
        level.add_portal(Portal("resources/img/portal_v.png", [220, 520], (310, 120)))

        level.add_portal(Portal("resources/img/portal_h.png", [410, 20], (150, 620)))
        level.add_portal(Portal("resources/img/portal_v.png", [20, 520], (540, 120)))

        level.add_portal(Portal("resources/img/portal_h.png", [640, 20], (90, 370)))
        level.add_portal(Portal("resources/img/portal_v.png", [220, 250], (770, 120)))

        level.add_portal(Portal("resources/img/portal_h.png", [870, 20], (280, 370)))
        level.add_portal(Portal("resources/img/portal_v.png", [420, 250], (1000, 120)))

        bitcoins = ((430, 120), (660, 120), (890, 120), (70, 650), (370, 500),
                    (70, 235), (485, 290), (1115, 400), (485, 510))
        for pos in bitcoins:
            bitcoin = Texture("resources/img/bitcoin.png", pos)
            level.add_bitcoin(bitcoin)

        enemy1 = Enemy("resources/img/buld.png", (370, 650))
        enemy1_moves = Repeat(MoveBy((-100, 0), 1) +
                              MoveBy((0, -150), 1.2) +
                              MoveBy((100, 0), 1) +
                              MoveBy((0, 150), 1.2))
        enemy1.do(enemy1_moves)
        level.add_enemy(enemy1)

        enemy2 = Enemy("resources/img/buld.png", (170, 500))
        enemy2_moves = Repeat(MoveBy((0, 150), 1.2) +
                              MoveBy((-100, -150), 1.5) +
                              MoveBy((0, 150), 1.2) +
                              MoveBy((100, -150), 1.5))
        enemy2.do(enemy2_moves)
        level.add_enemy(enemy2)

        enemy3 = Enemy("resources/img/buld.png", (170, 400))
        enemy3_moves = Repeat(MoveBy((0, -170), 1.25) + Reverse(MoveBy((0, -170), 1.25)))
        enemy3.do(enemy3_moves)
        level.add_enemy(enemy3)

        enemy4 = Enemy("resources/img/buld.png", (170, 250))
        enemy4_moves = Repeat(MoveBy((-100, 0), 1) + Reverse(MoveBy((-100, 0), 1)))
        enemy4.do(enemy4_moves)
        level.add_enemy(enemy4)

        enemy5 = Enemy("resources/img/buld.png", (270, 230))
        enemy5_moves = Repeat(MoveBy((100, 0), 1) +
                              MoveBy((0, 170), 1.25) +
                              MoveBy((-100, -170), 1.4))
        enemy5.do(enemy5_moves)
        level.add_enemy(enemy5)

        enemy6 = Enemy("resources/img/roflan2.png", (580, 650))
        enemy6_moves = Repeat(MoveBy((0, -410), 1.3) + Reverse(MoveBy((0, -410), 1.3)))
        enemy6.do(enemy6_moves)
        level.add_enemy(enemy6)

        enemy7 = Enemy("resources/img/roflan2.png", (750, 650))
        enemy7_moves = Repeat(MoveBy((0, -410), 1.1) + Reverse(MoveBy((0, -410), 1.1)))
        enemy7.do(enemy7_moves)
        level.add_enemy(enemy7)

        enemy8 = Enemy("resources/img/roflan2.png", (920, 650))
        enemy8_moves = Repeat(MoveBy((0, -410), 1) + Reverse(MoveBy((0, -410), 1)))
        enemy8.do(enemy8_moves)
        level.add_enemy(enemy8)

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

