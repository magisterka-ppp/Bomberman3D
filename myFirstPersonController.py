from ursina.prefabs.first_person_controller import FirstPersonController


class MyFirstPersonController(FirstPersonController):

    def __init__(self):
        super().__init__()
        self.jump_duration = 0
        self.position = (1, 1, 1)


    def input(self, key):
        super().input(key)