from cocos.sprite import Sprite
import cocos.collision_model as cm


class Enemy(Sprite):
    def __init__(self, image, position):
        super(Enemy, self).__init__(image, position)
        self.cshape = cm.AARectShape(
            self.position,
            self.width // 2,
            self.height // 2
        )
