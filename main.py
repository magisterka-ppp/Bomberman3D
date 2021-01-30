from ursina import *

from blocks import Ground, Wall, HardWall
from bomber import Bomber
from constants import WORLD_SCALE
from menu import InterfacePanel
from myFirstPersonController import MyFirstPersonController
from skybox import Skybox

snd_putBomb = Audio('./snd/Pickup_Coin4.wav', pitch=1, loop=False, autoplay=False)
snd_explode = Audio('./snd/Explosion4.wav', pitch=1, loop=False, autoplay=False)


if __name__ == '__main__':

    app = Ursina()
    current_map = [
        # start
        [2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2],
        [2, 0, 1, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 2],
        [2, 0, 1, 0, 1, 0, 1, 1, 0, 1, 1, 1, 1, 1, 1, 1, 0, 1, 0, 2],
        [2, 0, 1, 0, 1, 0, 0, 1, 1, 1, 1, 0, 0, 0, 0, 0, 0, 1, 0, 2],
        [2, 0, 1, 0, 1, 0, 1, 1, 0, 0, 1, 0, 0, 1, 1, 1, 0, 1, 0, 2],
        [2, 0, 0, 0, 0, 0, 0, 1, 0, 0, 1, 0, 0, 1, 1, 1, 0, 1, 0, 2],
        [2, 1, 1, 1, 1, 1, 0, 1, 0, 0, 0, 0, 0, 1, 1, 1, 0, 1, 0, 2],
        [2, 0, 0, 1, 0, 1, 0, 1, 0, 1, 1, 1, 1, 1, 0, 0, 0, 0, 0, 2],
        [2, 0, 0, 0, 0, 0, 0, 0, 0, 1, 1, 1, 1, 1, 0, 1, 0, 1, 0, 2],
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

    player = MyFirstPersonController()
    panel = InterfacePanel()

    walls = []
    for z in range(world_size_z):
        for x in range(world_size_x):
            Ground(scene, (x * WORLD_SCALE, 0, z * WORLD_SCALE))
            if current_map[z][x] == 1:
                walls.append(Wall(scene, (x * WORLD_SCALE, 1 * WORLD_SCALE, z * WORLD_SCALE)))
            if current_map[z][x] == 2:
                HardWall(scene, (x * WORLD_SCALE, 1 * WORLD_SCALE, z * WORLD_SCALE))

    enemy_table = [
        Bomber(scene, (1 * WORLD_SCALE, 1 * WORLD_SCALE, 1 * WORLD_SCALE)),
        Bomber(scene, (18 * WORLD_SCALE, 1 * WORLD_SCALE, 18 * WORLD_SCALE)),
        Bomber(scene, (1 * WORLD_SCALE, 1 * WORLD_SCALE, 18 * WORLD_SCALE))
    ]

    scene.walls = walls
    scene.app = app
    scene.player = player
    scene.panel = panel
    scene.enemy_table = enemy_table
    skybox = Skybox()

    app.run()
