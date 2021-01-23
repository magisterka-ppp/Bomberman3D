
from ursina import *

from myFirstPersonController import MyFirstPersonController

app = Ursina()
world_size_x = 10
world_size_z = 10
current_map = [
    [1, 1, 1, 1, 1, 1, 1, 1, 1, 1],
    [1, 0, 0, 0, 0, 0, 0, 0, 0, 1],
    [1, 0, 0, 0, 0, 0, 0, 0, 0, 1],
    [1, 0, 0, 0, 1, 0, 0, 0, 0, 1],
    [1, 0, 0, 0, 0, 0, 0, 0, 0, 1],
    [1, 0, 0, 0, 0, 0, 0, 0, 0, 1],
    [1, 0, 0, 0, 0, 0, 0, 0, 0, 1],
    [1, 0, 0, 0, 0, 0, 0, 0, 0, 1],
    [1, 0, 0, 0, 0, 0, 0, 0, 0, 1],
    [1, 1, 1, 1, 1, 1, 1, 1, 1, 1]
]
Texture.default_filtering = None

player = MyFirstPersonController()
p = Entity()
window.fps_counter.enabled = True
window.exit_button.visible = False


class Skybox(Entity):
    def __init__(self):
        super().__init__(
            model='sphere',
            texture='skybox',
            scale=150,
            double_sided=True)


class Ground(Button):
    def __init__(self, position=(0, 0, 0)):
        super().__init__(
            parent=p,
            position=position,
            model='cube',
            scale_y=1,
            texture='dirt',
            color=color.white,
            highlight_color=color.olive,
        )
    def input(self, key):
        if self.hovered:
            if key == 'left mouse down':
                pass
                # Voxel(position=self.position + mouse.normal)

            if key == 'right mouse down':
                pass
                # destroy(self)


class Wall(Button):
    def __init__(self, position=(0, 0, 0)):
        super().__init__(
            parent=p,
            position=position,
            model='cube',
            scale_y=5,
            texture='stone',
            color=color.white,
        )


for z in range(world_size_z):
    for x in range(world_size_x):
        Ground(position=(x, 0, z))
        if current_map[z][x] == 1:
            Wall(position=(x, 1, z))

skybox = Skybox()

app.run()