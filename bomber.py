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
        self.x_speed = 0.1
        self.z_speed  = 0.05
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
        self.world_rotation = +180
        ray = raycast(self.world_position, self.left, ignore=(self,))

        if ray.distance <= 2.1:
            print("yeeeeeeeeeeettttttt")
            print(self.world_rotation)
            self.world_rotation=+180


        self.position += self.right*time.dt

