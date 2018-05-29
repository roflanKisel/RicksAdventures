import cocos
import cocos.collision_model as cm


class Barrier(cocos.sprite.Sprite):
    def __init__(self, image, position, is_damaging):
        super(Barrier, self).__init__(image, position)
        self.is_damaging = is_damaging
        self.cshape = cm.AARectShape(
            self.position,
            self.width // 2,
            self.height // 2
        )
