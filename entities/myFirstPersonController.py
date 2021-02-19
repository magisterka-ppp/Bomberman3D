from ursina.prefabs.first_person_controller import FirstPersonController
from constants import WORLD_SCALE


class MyFirstPersonController(FirstPersonController):

    def __init__(self):
        super().__init__()
        self.jump_duration = 0
        self.collider = 'box'
        self.position = (1 * WORLD_SCALE, 1 * WORLD_SCALE, 1 * WORLD_SCALE)
        self.bombs_amount = 1
        self.bombs_placed = 0
        self.explode_range = 2
        self.scale = WORLD_SCALE
