from ursina.prefabs.first_person_controller import FirstPersonController

from constants import WORLD_SCALE


class MyFirstPersonController(FirstPersonController):

    def __init__(self):
        super().__init__()
        self.jump_duration = 0
        self.collider = 'box'
        self.position = (0*WORLD_SCALE, 6*WORLD_SCALE, 0*WORLD_SCALE)


    def input(self, key):
        super().input(key)