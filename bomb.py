from ursina import *
from constants import WORLD_SCALE


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
        # make sub-explosions same size as main one
        if str(self.parent) != "render/scene/bomb":
            self.scale *= 2
            self.position *= 2
        # avoiding of infinit recurrency
        if str(self.parent) == "render/scene/bomb":
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
                    Explosion(self, owner, gameController, (i, 0, 0))
                    for wall in gameController.walls:
                        if wall.intersects(self).hit:
                            destroy(wall)
                            x_for = False
                if x_bac:
                    Explosion(self, owner, gameController, (-i, 0, 0))
                    for wall in gameController.walls:
                        if wall.intersects(self).hit:
                            destroy(wall)
                            x_bac = False
                if z_for:
                    Explosion(self, owner, gameController, (0, 0, i))
                    for wall in gameController.walls:
                        if wall.intersects(self).hit:
                            destroy(wall)
                            z_for = False
                if z_bac:
                    Explosion(self, owner, gameController, (0, 0, -i))
                    for wall in gameController.walls:
                        if wall.intersects(self).hit:
                            destroy(wall)
                            z_bac = False
        if gameController.player.intersects(self).hit:
            application.quit()
        for enemy in gameController.enemy_table:
            if enemy.intersects(self).hit and owner is not enemy:
                destroy(enemy)
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
        invoke(self.explode, owner, gameController, delay=2)

    def explode(self, owner, gameController):
        Explosion(self, owner, gameController)
        owner.bombs_placed -= 1
        from main import snd_explode
        snd_explode.play()