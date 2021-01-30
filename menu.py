# Create menu
from ursina.prefabs.dropdown_menu import DropdownMenuButton, DropdownMenu


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