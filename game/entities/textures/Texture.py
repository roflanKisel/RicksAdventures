import cocos
import cocos.collision_model as cm


class Texture(cocos.sprite.Sprite):
    def __init__(self, image, position):
        super(Texture, self).__init__(image, position)
        self.cshape = cm.AARectShape(
            self.position,
            self.width // 2,
            self.height // 2
        )
