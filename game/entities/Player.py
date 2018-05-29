from cocos.sprite import Sprite
import cocos.collision_model as cm


class Player(Sprite):
    def __init__(self, image, position, velocity, speed):
        super(Player, self).__init__(image, position)
        self.__velocity = velocity
        self.__speed = speed
        self.cshape = cm.AARectShape(
            self.position,
            self.width // 2,
            self.height // 2
        )

    def get_velocity(self):
        return self.__velocity

    def get_speed(self):
        return self.__speed
