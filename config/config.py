from pyglet.window import key
import pyglet
import cocos.collision_model as cm

"""config file which contains common objects"""

collision_manager = cm.CollisionManagerBruteForce()
keyboard = key.KeyStateHandler()
music_player = pyglet.media.Player()
