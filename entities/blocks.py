from ursina import *

from entities.bomb import Bomb
from constants import WORLD_SCALE


class Ground(Button):
    def __init__(self, gameController, position=(0, 0, 0)):
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
        self.gameController = gameController

    def input(self, key):
        player = self.gameController.player
        if self.hovered:
            position = self.position - player.position
            if abs(position.x) < 20 and abs(position.z) < 20:
                if key == 'left mouse down':
                    if player.bombs_placed < player.bombs_amount:
                        self.gameController.snd_putBomb.play()
                        Bomb(player, self.gameController, position=self.position + mouse.normal)
                        player.bombs_placed += 1


class Wall(Button):
    def __init__(self, gameController, position=(0, 0, 0)):
        super().__init__(
            parent=scene,
            position=position,
            model='cube',
            scale=WORLD_SCALE,
            scale_y=5 * WORLD_SCALE,
            texture='stone',
            color=color.white,
        )
        self.gameController = gameController


class HardWall(Button):
    def __init__(self, gameController, position=(0, 0, 0)):
        super().__init__(
            parent=scene,
            position=position,
            model='cube',
            scale=WORLD_SCALE,
            scale_y=7 * WORLD_SCALE,
            texture='wood',
            color=color.white,
        )
        self.gameController = gameController
