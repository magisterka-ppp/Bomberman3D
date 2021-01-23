from ursina import *

from constants import WORLD_SCALE

distance_y = -0.2
distance_x = 2.1


class Explosion(Entity):
    def explode(self):
        destroy(self.parent)

    def __init__(self, parent, owner, scene, scale=1, position=(0, 0, 0)):
        super().__init__(
            parent=parent,
            position=[x * scale for x in position],
            scale=scale,
            model='sphere',
            collider='box',
            texture='l0',
            color=color.white,
        )
        for wall in scene.walls:
            if wall.intersects(self).hit:
                destroy(wall)
        if scene.player.intersects(self).hit:
            application.quit()
        for enemy in scene.enemy_table:
            if enemy.intersects(self).hit and owner is not enemy:
                destroy(enemy)
        invoke(self.explode, delay=.5)


class Bomb(Entity):
    def explode(self, owner, scene):
        self.snd_explode.play()
        Explosion(self, owner, scene, .9)
        for i in range(4):
            Explosion(self, owner, scene, .5 / (i + 1), (i * distance_x + 1, distance_y * i, 0))
            Explosion(self, owner, scene, .5 / (i + 1), (-i * distance_x - 1, distance_y * i, 0))
            Explosion(self, owner, scene, .5 / (i + 1), (0, distance_y * i, i * distance_x + 1))
            Explosion(self, owner, scene, .5 / (i + 1), (0, distance_y * i, -i * distance_x - 1))

    def __init__(self, owner, scene, position=(0, 0, 0)):
        position[1] += (WORLD_SCALE - 1.2)
        super().__init__(
            parent=scene,
            position=position,
            model='bomb',
            collider='box',
            scale=3 * WORLD_SCALE,
            texture='tnt',
            color=color.white,
            highlight_color=color.olive,
        )
        self.prev_texture = self.texture
        self.snd_explode = Audio('./snd/Explosion4.wav', pitch=1, loop=False, autoplay=False)
        invoke(self.explode, owner, scene, delay=2)
