from ursina import *

from bomb import Bomb
from constants import WORLD_SCALE


class Bomber(Entity):
    def __init__(self, scene, position=(0, 0, 0)):
        super().__init__(
            parent=scene,
            position=position,
            model='enemy',
            scale= WORLD_SCALE/4,
            collider='box',
            texture='GhostlingUV',
            color=color.white,
            rotation=(0, 0, 0)
        )
        invoke(self.putBomb, delay=10)

    def putBomb(self):
        if self.is_empty():
            return
        Bomb(self, scene, position=self.position)
        invoke(self.putBomb, delay=10)

    def update(self):
        ray = raycast(self.world_position, self.back, ignore=(self,))

        if ray.distance <= 2.1:
            self.rotation_y += 90 + 180 * random.randrange(0, 2)
            return

        self.position += self.back * time.dt * 4
