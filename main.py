from ursina import *
from ursina import mouse, curve

from bomb import Bomb
from constants import WORLD_SCALE
from myFirstPersonController import MyFirstPersonController

app = Ursina()
current_map = [
    [2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2],
    [2, 0, 1, 0, 1, 0, 0, 0, 0, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 2],
    [2, 0, 1, 0, 1, 0, 1, 1, 0, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 2],
    [2, 0, 1, 0, 1, 0, 0, 1, 1, 1, 1, 0, 0, 0, 0, 0, 0, 1, 1, 2],
    [2, 0, 1, 0, 1, 0, 1, 1, 0, 0, 1, 0, 0, 1, 1, 1, 0, 1, 1, 2],
    [2, 0, 0, 0, 0, 0, 0, 1, 0, 0, 1, 0, 0, 1, 1, 1, 0, 1, 1, 2],
    [2, 1, 1, 1, 1, 1, 0, 1, 0, 0, 0, 0, 0, 1, 1, 1, 0, 1, 1, 2],
    [2, 0, 0, 1, 0, 1, 0, 1, 0, 1, 1, 1, 1, 1, 0, 0, 0, 0, 0, 2],
    [2, 0, 0, 0, 0, 0, 0, 0, 0, 1, 1, 1, 1, 1, 0, 1, 0, 1, 0, 1],
    [2, 1, 1, 0, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 0, 1, 0, 1, 0, 2],
    [2, 1, 1, 0, 1, 1, 1, 1, 1, 1, 1, 0, 0, 0, 0, 1, 1, 1, 0, 2],
    [2, 0, 1, 0, 1, 0, 0, 0, 0, 1, 0, 1, 0, 1, 0, 1, 1, 1, 0, 2],
    [2, 0, 1, 0, 1, 0, 1, 1, 0, 0, 0, 1, 0, 1, 0, 1, 0, 0, 0, 2],
    [2, 0, 1, 0, 1, 0, 0, 1, 1, 1, 0, 1, 0, 1, 0, 1, 1, 0, 1, 2],
    [2, 0, 1, 0, 1, 0, 1, 1, 0, 1, 0, 1, 1, 1, 0, 1, 1, 1, 1, 2],
    [2, 0, 0, 0, 0, 0, 0, 1, 0, 1, 0, 0, 0, 0, 0, 1, 0, 0, 0, 2],
    [2, 1, 1, 1, 1, 1, 0, 1, 0, 1, 1, 1, 1, 1, 0, 1, 0, 1, 0, 2],
    [2, 0, 0, 1, 0, 1, 0, 1, 0, 1, 1, 1, 1, 1, 1, 1, 1, 1, 0, 2],
    [2, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 2],
    [2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2]
]

world_size_x = len(current_map[0])
world_size_z = len(current_map)
Texture.default_filtering = None

window.fps_counter.enabled = True
window.exit_button.visible = False

# Audio files
snd_bg = Audio('./snd/Factory.ogg', pitch=1, loop=True, autoplay=True)
snd_putbomb = Audio('./snd/Pickup_Coin4.wav', pitch=1, loop=False, autoplay=False)


class Skybox(Entity):
    def __init__(self):
        super().__init__(
            model='sphere',
            texture='skybox',
            scale=500,
            double_sided=True)
        snd_bg.play()


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
        self.walls = walls

    def input(self, key):
        if self.hovered:
            if key == 'left mouse down':
                Bomb(scene, position=self.position + mouse.normal)
                snd_putbomb.play()


class Bomber(Entity):
    def __init__(self, position=(0, 0, 0)):
        super().__init__(
            parent=scene,
            position=position,
            model='bomber',
            collider='box',
            scale=5 * WORLD_SCALE,
            texture='bomber',
            color=color.white,
        )

        def putBomb():
            Bomb(scene, position=self.position)
            invoke(putBomb, delay=10)

        invoke(putBomb, delay=10)


class Wall(Button):
    def __init__(self, position=(0, 0, 0)):
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
    def __init__(self, position=(0, 0, 0)):
        super().__init__(
            parent=scene,
            position=position,
            model='cube',
            scale=WORLD_SCALE,
            scale_y=7 * WORLD_SCALE,
            texture='wood',
            color=color.white,
        )


walls = []
for z in range(world_size_z):
    for x in range(world_size_x):
        Ground(scene, (x * WORLD_SCALE, 0, z * WORLD_SCALE))
        if current_map[z][x] == 1:
            walls.append(Wall((x * WORLD_SCALE, 1 * WORLD_SCALE, z * WORLD_SCALE)))
        if current_map[z][x] == 2:
            HardWall((x * WORLD_SCALE, 1 * WORLD_SCALE, z * WORLD_SCALE))

enemy_table = []
enemy_table.append(Bomber((5 * WORLD_SCALE, 1 * WORLD_SCALE, 5 * WORLD_SCALE)))

scene.walls = walls
scene.player = MyFirstPersonController()
scene.app = app
scene.enemy_table = enemy_table
skybox = Skybox()

app.run()
