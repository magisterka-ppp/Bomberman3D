from ursina import *

from bomb import Bomb
from constants import WORLD_SCALE


class Ground(Button):
    def __init__(self, scene, position=(0, 0, 0)):
        super().__init__(
            parent=scene,
            position=position,
            model='cube',
            scale=WORLD_SCALE,
            scale_y=1 * WORLD_SCALE,
            texture='dirt',
            color=color.white,
            highlight_color=color.olive,
        )
        self.scene = scene

    def input(self, key):
        if key == 'escape':
            exit()

        if self.hovered:
            position = self.position - self.scene.player.position
            if abs(position.x) < 20 and abs(position.z) < 20:
                if key == 'left mouse down':
                    if self.scene.player.bombs_placed < self.scene.player.bombs_amount:
                        Bomb(self.scene.player, self.scene, position=self.position + mouse.normal)
                        self.scene.player.bombs_placed += 1
                        from main import snd_putBomb
                        snd_putBomb.play()


class Wall(Button):
    def __init__(self, scene, position=(0, 0, 0)):
        super().__init__(
            parent=scene,
            position=position,
            model='cube',
            scale=WORLD_SCALE,
            scale_y=5 * WORLD_SCALE,
            texture='stone',
            color=color.white,
        )


class HardWall(Button):
    def __init__(self, scene, position=(0, 0, 0)):
        super().__init__(
            parent=scene,
            position=position,
            model='cube',
            scale=WORLD_SCALE,
            scale_y=7 * WORLD_SCALE,
            texture='wood',
            color=color.white,
        )
