from ursina import *
from ursina import mouse
from ursina.prefabs.dropdown_menu import DropdownMenu, DropdownMenuButton

from bomb import Bomb
from bomber import Bomber
from constants import WORLD_SCALE
from myFirstPersonController import MyFirstPersonController


# Create menu
class Menu(DropdownMenu):
    def __init__(self, name):
        super().__init__(
            text=name,
            buttons=(
                DropdownMenuButton('New'),
                DropdownMenu('Options', buttons=(
                    DropdownMenuButton('Option a'),
                    DropdownMenuButton('Option b'),
                )),
                DropdownMenu('Help'),
                DropdownMenuButton('Exit'),
            ),
        )
        self.is_open = False

    def input(self, key):
        if key == 'tab':
            if self.is_open == False:
                self.open()
                self.is_open = True
            else:
                self.close()
                self.is_open = False
        if key == 'arrow_right':
            ...
    def update(self):
        ...


class InterfacePanel(WindowPanel):
    def __init__(self):
        super().__init__(
            title='Game Over',
            content=(
                Button(text='Exit', color=color.azure),
                Button(text='Restart', color=color.azure),
            ),
        )

    def input(self, key):
        if key == 'tab':
            self.disable()
        if key == 'space':
            pane = InterfacePanel()


class Skybox(Entity):
    def __init__(self):
        super().__init__(
            model='sphere',
            texture='skybox',
            scale=500,
            double_sided=True)
        Text('Press W, A, S, D to control character and left mouse button to place bomb.', origin=(0, -.5), y=-.4)


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

    def input(self, key):
        if key == 'escape':
            exit()

        if self.hovered:
            position = self.position - player.position
            if abs(position.x) < 20 and abs(position.z) < 20:
                if key == 'left mouse down':
                    if player.bombs_placed < player.bombs_amount:
                        Bomb(player, scene, position=self.position + mouse.normal)
                        player.bombs_placed += 1
                        snd_putbomb.play()


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

    # Audio files
    snd_bg = Audio('./snd/Factory.ogg', pitch=1, loop=True, autoplay=True)
    snd_putbomb = Audio('./snd/Pickup_Coin4.wav', pitch=1, loop=False, autoplay=False)
    player = MyFirstPersonController()
    panel = InterfacePanel()

    walls = []
    for z in range(world_size_z):
        for x in range(world_size_x):
            Ground(scene, (x * WORLD_SCALE, 0, z * WORLD_SCALE))
            if current_map[z][x] == 1:
                walls.append(Wall((x * WORLD_SCALE, 1 * WORLD_SCALE, z * WORLD_SCALE)))
            if current_map[z][x] == 2:
                HardWall((x * WORLD_SCALE, 1 * WORLD_SCALE, z * WORLD_SCALE))

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
