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
            xz = 1,
            direction = 1,
        )
        self.grounded = False
        self.gravity = True
        self.air_time = 0

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
        invoke(self.changeDirection, delay=5)

    def update(self):
        if self.gravity:
            # # gravity
            ray = raycast(self.world_position+(0,2,0), self.down, ignore=(self,))

            if ray.distance <= 2.1:
                if not self.grounded:
                    self.land()
                self.grounded = True
                # make sure it's not a wall and that the point is not too far up
                if ray.world_normal.y > .7 and ray.world_point.y - self.world_y < .5: # walk up slope
                    self.y = ray.world_point[1]
                return
            else:
                self.grounded = False


        if self.xz == 1:
            self.position += (self.direction * time.dt * WORLD_SCALE,0,0)
        else:
            self.position += (0, 0, self.direction * time.dt * WORLD_SCALE)

         # if not on ground and not on way up in jump, fall
        self.y -= min(self.air_time, ray.distance - .05)
        self.air_time += time.dt * .25 * self.gravity

    def land(self):
         # print('land')
        self.air_time = 0
        self.grounded = True