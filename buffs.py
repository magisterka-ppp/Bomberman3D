from ursina import *
from constants import WORLD_SCALE

class Buff(Entity):
    def __init__(self, gameController, position=(0, 0, 0)):
        type = random.randrange(1, 100)
        if type <= 50:
            buff_texture = 'buff_bomb_amount'
            self.bombs_amount = 1
            self.explode_range = 0
            self.snd_buff_get = Audio('./snd/buff_amount.wav', pitch=1, loop=False, autoplay=False)
        else:
            buff_texture = 'buff_enlarge_range'
            self.bombs_amount = 0
            self.explode_range = 1
            self.snd_buff_get = Audio('./snd/buff_range.wav', pitch=1, loop=False, autoplay=False)
        super().__init__(
            parent=scene,
            position=position,
            model='bomb',
            collider='box',
            scale=WORLD_SCALE,
            texture=buff_texture,
            color=color.white,
            highlight_color=color.olive,
        )
        self.gameController = gameController

    def update(self):
        # interaction with player
        if self.gameController.player.intersects(self).hit:
            self.snd_buff_get.play()
            self.gameController.player.bombs_amount += self.bombs_amount
            self.gameController.player.explode_range += self.explode_range
            self.gameController.buff_table.remove(self)
            destroy(self)

        # doesn't work, why? (this part is currently process in 'bomber.py')
        # for enemy in self.gameController.enemy_table:
        #     if enemy.intersects(self).hit:
        #         self.snd_buff_get.play()
        #         enemy.bombs_amount += self.bombs_amount
        #         enemy.explode_range += self.explode_range
        #         self.gameController.buff_table.remove(self)
        #         destroy(self)