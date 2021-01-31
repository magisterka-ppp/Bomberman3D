from ursina import *
from bomb import Bomb
from buffs import Buff
import array
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
        )
        self.gameController = gameController
        self.bombs_amount = 1
        self.bombs_placed = 0
        self.explode_range = 2
        self.mem_position = [0, 0, 0]
        self.wait = False
        self.stunned = False

    def after_time(self):
        self.wait = False

    def after_stun(self):
        self.stunned = False

    def putBomb(self):
        if self.is_empty():
            return
        # avoid enemy to stuck in bomb
        if abs(self.mem_position[0] - self.position.x) < 0.8 and abs(self.mem_position[2] - self.position.z) < 0.8:
            return
        if self.bombs_placed < self.bombs_amount and not self.wait:
            Bomb(self, self.gameController, position=self.mem_position)
            self.bombs_placed += 1
            self.wait = True
            invoke(self.after_time, delay=1)

    def update(self):
        if not self.stunned:
            # Why (doing the same part of work) code in 'buffs.py' doesn't work?
            for buff in self.gameController.buff_table:
                if buff.intersects(self).hit:
                    buff.snd_buff_get.play()
                    self.bombs_amount += buff.bombs_amount
                    self.explode_range += buff.explode_range
                    self.gameController.buff_table.remove(buff)
                    destroy(buff)

            ray_bomb = raycast(self.world_position, self.back,
                               ignore=([self] + self.gameController.buff_table + self.gameController.walls + self.gameController.hardWall + self.gameController.enemy_table),
                               distance=0.5 + WORLD_SCALE / 2)
            ray_enemy = raycast(self.world_position, self.back,
                               ignore=([self] + self.gameController.buff_table + self.gameController.walls + self.gameController.hardWall),
                               distance=WORLD_SCALE / 2)
            ray_wall = raycast(self.world_position, self.back,
                               ignore=([self] + self.gameController.buff_table + self.gameController.enemy_table),
                               distance=WORLD_SCALE/2)
            # enemy detect bomb
            if ray_bomb.hit:
                action = random.randrange(0, 1)
                if action == 1:
                    self.mem_position = [self.position.x, self.position.y - 1, self.position.z]
                    invoke(self.putBomb, delay=0.5)
                self.rotation_y += 90 + 90 * random.randrange(0, 2)

            # enemy detect opponent
            if ray_enemy.hit:
                action = random.randrange(0, 10)
                if action <= 7:
                    self.mem_position = [self.position.x, self.position.y - 1, self.position.z]
                    invoke(self.putBomb, delay=0.5)
                self.rotation_y += 90 + 90 * random.randrange(0, 2)

            # enemy detect wall
            if ray_wall.hit:
                action = random.randrange(1, 4)
                if action == 1:
                    self.rotation_y += 90 + 90 * random.randrange(0, 2)
                elif action == 2:
                    self.mem_position = [self.position.x, self.position.y - 1, self.position.z]
                    invoke(self.putBomb, delay=0.5)
                elif action == 3:
                    self.mem_position = [self.position.x, self.position.y - 1, self.position.z]
                    self.rotation_y += 90 + 90 * random.randrange(0, 2)
                    invoke(self.putBomb, delay=0.5)
                    return
                elif action == 4:
                    return

            self.position += self.back * time.dt * 4
