from ursina import *


class Explosion(Entity):
    def explode(self):
        destroy(self.parent)

    def __init__(self, parent):
        super().__init__(
            parent=parent,
            position=(0, 0, 0),
            model='sphere',
            texture='l0',
            color=color.white,
        )
        invoke(self.explode, delay=1)


class Bomb(Entity):
    def explode(self, walls):
        for wall in walls:
            if wall.intersects(self).hit:
                destroy(wall)
        Explosion(self)

    def __init__(self, walls, position=(0, 0, 0)):
        super().__init__(
            parent=scene,
            position=position,
            model='bomb',
            collider='sphere',
            scale=4,
            texture='tnt',
            color=color.white,
            highlight_color=color.olive,
        )
        invoke(self.explode, walls, delay=2)
