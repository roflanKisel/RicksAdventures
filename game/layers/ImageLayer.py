import cocos


class ImageLayer(cocos.layer.Layer):
    is_event_handler = True

    def __init__(self, path):
        super(ImageLayer, self).__init__()

        self.sprite = cocos.sprite.Sprite(path)
        self.sprite.position = 600, 400

        self.add(self.sprite)
