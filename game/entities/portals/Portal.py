import cocos
import cocos.collision_model as cm


class Portal(cocos.sprite.Sprite):
    def __init__(self, image, position, next_position):
        super(Portal, self).__init__(image, position)
        self.__next_position = next_position
        self.cshape = cm.AARectShape(
            self.position,
            self.width // 2,
            self.height // 2
        )

    def get_next_position(self):
        return self.__next_position
