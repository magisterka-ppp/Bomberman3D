from ursina import *
from bomb import Bomb
from buffs import Buff
from constants import WORLD_SCALE


class Bomber(Entity):
    def __init__(self, gameController, position=(0, 0, 0), texture_color=None):
        enemy_texture_colors = ["red", "green", "blue", "purple", "orange", "white", "black"]
        if texture_color is None:
            texture_color = random.choice(enemy_texture_colors)
        super().__init__(
            parent = scene,
            position = position,
            model = 'enemy',
            scale = WORLD_SCALE/4,
            collider = 'box',
            texture = texture_color,
            color = color.white,
            rotation = (0, 0, 0),
            bombs_amount = 1,
            bombs_placed = 0,
            explode_range = 2,
            mem_position = [0, 0, 0],
        )
        self.gameController = gameController

    def putBomb(self):
        if self.is_empty():
            return
        # avoid enemy to stuck in bomb
        if abs(self.mem_position[0] - self.position.x) < 0.8\
                and abs(self.mem_position[1] - self.position.y) < 0.8 \
                and abs(self.mem_position[2] - self.position.z) < 0.8:
            return
        if self.bombs_placed < self.bombs_amount:
            Bomb(self, self.gameController, position=self.mem_position)
            self.bombs_placed += 1

    def update(self):
        for buff in self.gameController.buff_table:
            if buff.intersects(self).hit:
                self.bombs_amount += buff.bombs_amount
                self.explode_range += buff.explode_range
                self.gameController.buff_table.remove(buff)
                destroy(buff)
                self.position += self.back * time.dt * 4
                return

        ray = raycast(self.world_position, self.back, ignore=(self, Buff))

        if ray.distance <= WORLD_SCALE/2:
            self.rotation_y += 90 + 180 * random.randrange(0, 2)
            self.mem_position = [self.position.x, self.position.y - 1, self.position.z]
            invoke(self.putBomb, delay=0.5)
            return
        self.position += self.back * time.dt * 4
