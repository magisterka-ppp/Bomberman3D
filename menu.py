# Create menu
from ursina import Button, color, Cursor, camera, mouse
from ursina.prefabs.dropdown_menu import DropdownMenuButton, DropdownMenu, WindowPanel, EditorCamera, Entity


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
            popup = True,
            content=(
                Button(text='Exit', color=color.azure),
                Button(text='Restart', color=color.azure),
            ),
        )
        self.ec = EditorCamera(rotation_smoothing=2, enabled=False, rotation=(30,30,0))
        self.ec.enabled = False
        self.cur = Cursor()
        self.cur.disable()
        self.hide()

    def input(self, key):
        if key == 'tab':
            if self.is_hidden():
                camera.orthographic = True
                self.show()
                self.ec.enabled = True
                mouse.locked = False
                mouse.visible = False
                self.cur.enable()
            else:
                self.hide()
                camera.orthographic = False
                self.ec.enabled = False
                mouse.locked = True
                mouse.visible = False
                self.cur.disable()