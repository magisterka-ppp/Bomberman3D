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
            rotation=(0,0,0)
        )
        self.x_speed = 0.1
        self.z_speed  = 0.05
        invoke(self.putBomb, delay=10)

    def putBomb(self):
        if self.is_empty():
            return
        Bomb(self, scene, position=self.position)
        invoke(self.putBomb, delay=10)


    def update(self):
        ray = raycast(self.world_position, self.forward, ignore=(self,))

        if ray.distance <= 2.1:
            print(self.world_rotation)
            self.rotation_y+=90*random.randrange(-1,1)


        self.position += self.forward*time.dt*0.5

