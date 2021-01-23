from ursina import *

from bomb import Bomb
from constants import WORLD_SCALE


class Bomber(Entity):
    def __init__(self, scene , position=(0, 0, 0)):
        super().__init__(
            parent=scene,
            position=position,
            model='bombero',
            scale= 2 * WORLD_SCALE,
            collider ='box',
            texture='bomber',
            color=color.white,
            xz = -1,
            direction = 1,
        )

        invoke(self.putBomb, delay=10)
        invoke(self.changeDirection, delay=5)

    def putBomb(self):
        if self.is_empty():
            return
        Bomb(self, scene, position=self.position)
        invoke(self.putBomb, delay=10)

    def changeDirection(self):
        self.xz *= -1
        self.direction *= -1

    def update(self):
        ray = raycast(self.world_position, self.back, ignore=(self,))

        if ray.distance <= 2.1:
            self.changeDirection()

        if self.xz == 1:
            self.position += (self.direction * time.dt * WORLD_SCALE,0,0)
        else:
            self.position += (0, 0, self.direction * time.dt * WORLD_SCALE)