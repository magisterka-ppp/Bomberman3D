from ursina import *
from constants import WORLD_SCALE, BUFF_CHANCE


class Explosion(Entity):
    def __init__(self, parent, owner, gameController, position=(0, 0, 0)):
        super().__init__(
            parent=parent,
            position=[x * WORLD_SCALE/4.025 for x in position],
            scale=WORLD_SCALE/4.025,
            model='sphere',
            collider='box',
            texture='l0',
            color=color.white,
        )
        self.gameController = gameController
        if parent is None and owner is None:
            return
        if gameController.player.intersects(self).hit and not gameController.panel.hardRestart:
            gameController.snd_gameLose.play()
            gameController.panel.showRestart()
        for enemy in gameController.enemy_table:
            if enemy.intersects(self).hit:
                if owner is enemy:
                    owner.stunned = True
                    invoke(owner.after_stun, delay=1)
                else:
                    destroy(enemy)
                    gameController.enemy_table.remove(enemy)
                    if len(gameController.enemy_table) == 0 and not gameController.panel.hardRestart:
                        gameController.snd_gameWin.play()
                        gameController.panel.showWin()
        for buff in gameController.buff_table:
            if buff.intersects(self).hit:
                gameController.buff_table.remove(buff)
                destroy(buff)
        invoke(self.explode, delay=.5)

    def explode(self):
        destroy(self.parent)


class Bomb(Entity):
    def __init__(self, owner, gameController, position=(0, 0, 0)):
        position[1] += (WORLD_SCALE - 1.2)
        super().__init__(
            parent=scene,
            position=position,
            model='bomb',
            collider='box',
            scale=WORLD_SCALE*2,
            texture='tnt',
            color=color.white,
            highlight_color=color.olive,
        )
        self.prev_texture = self.texture
        self.gameController = gameController
        invoke(self.explode, owner, delay=2)

    def explode(self, owner):
        if owner is not None and self is not None:
            self.gameController.snd_explode.play()
            owner.bombs_placed -= 1
            Explosion(self, owner, self.gameController)
            # on default allow propagation in all directions
            x_for = True
            x_bac = True
            z_for = True
            z_bac = True
            # propagation area depend on user explode_range
            for i in range(1, owner.explode_range):
                # for each direction check if current propagation range make a collide...
                # ...if it does destroy hit wall and turn of propagation in analyzed direction
                if x_for:
                    Explosion(self, owner, self.gameController, (i, 0, 0))
                    for wall in self.gameController.walls:
                        if wall.intersects(self).hit:
                            buffChance = random.randrange(1, 100)
                            if buffChance <= BUFF_CHANCE:
                                self.gameController.setBuff(wall.position)
                            destroy(wall)
                            x_for = False
                if x_bac:
                    Explosion(self, owner, self.gameController, (-i, 0, 0))
                    for wall in self.gameController.walls:
                        if wall.intersects(self).hit:
                            buffChance = random.randrange(1, 100)
                            if buffChance <= BUFF_CHANCE:
                                self.gameController.setBuff(wall.position)
                            destroy(wall)
                            x_bac = False
                if z_for:
                    Explosion(self, owner, self.gameController, (0, 0, i))
                    for wall in self.gameController.walls:
                        if wall.intersects(self).hit:
                            buffChance = random.randrange(1, 100)
                            if buffChance <= BUFF_CHANCE:
                                self.gameController.setBuff(wall.position)
                            destroy(wall)
                            z_for = False
                if z_bac:
                    Explosion(self, owner, self.gameController, (0, 0, -i))
                    for wall in self.gameController.walls:
                        if wall.intersects(self).hit:
                            buffChance = random.randrange(1, 100)
                            if buffChance <= BUFF_CHANCE:
                                self.gameController.setBuff(wall.position)
                            destroy(wall)
                            z_bac = False
