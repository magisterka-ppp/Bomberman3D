from ursina import *

distance_y = -0.2

distance_x = 2.1


class Explosion(Entity):
    def explode(self, walls):
        destroy(self.parent)

    def __init__(self, parent, walls, scale=1, position=(0, 0, 0)):
        super().__init__(
            parent=parent,
            position=[x * scale for x in position],
            scale=scale,
            model='sphere',
            collider='sphere',
            texture='l0',
            color=color.white,
        )
        for wall in walls:
            if wall.intersects(self).hit:
                destroy(wall)
        invoke(self.explode, walls, delay=.5)


class Bomb(Entity):
    def explode(self, walls):
        Explosion(self, walls, .9)
        for i in range(4):
            Explosion(self, walls, .5 / (i+1), (i * distance_x + 1, distance_y * i, 0))
            Explosion(self, walls, .5 / (i+1), (-i * distance_x - 1, distance_y * i, 0))
            Explosion(self, walls, .5 / (i+1), (0, distance_y * i, i * distance_x + 1))
            Explosion(self, walls, .5 / (i+1), (0, distance_y * i, -i * distance_x - 1))

    def __init__(self, walls, position=(0, 0, 0)):
        super().__init__(
            parent=scene,
            position=position,
            model='bomb',
            scale=3,
            texture='tnt',
            color=color.white,
            highlight_color=color.olive,
        )
        invoke(self.explode, walls, delay=2)
