from ursina.prefabs.first_person_controller import FirstPersonController

from constants import WORLD_SCALE


class MyFirstPersonController(FirstPersonController):

    def __init__(self):
        super().__init__()
        self.jump_duration = 0
        self.position = (1*WORLD_SCALE, 1*WORLD_SCALE, 1*WORLD_SCALE)


    def input(self, key):
        super().input(key)