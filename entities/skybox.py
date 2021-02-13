from ursina import Text, Entity


class Skybox(Entity):
    def __init__(self):
        super().__init__(
            model='sphere',
            texture='skybox',
            scale=500,
            double_sided=True)
        Text('Press W, A, S, D to control character and left mouse button to place bomb.', origin=(0, -.5), y=-.4)
