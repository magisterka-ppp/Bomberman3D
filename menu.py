# Create menu
from ursina import Button, color, Cursor, camera, mouse, application
from ursina.prefabs.dropdown_menu import DropdownMenuButton, DropdownMenu, WindowPanel, EditorCamera


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
    def __init__(self, gameController):
        super().__init__(

            title='Menu',
            popup = True,
            content=(
                Button(text='Restart', color=color.azure, on_click=self.restart),
                Button(text='Exit', color=color.azure, on_click=application.quit),
            ),
        )
        self.hardRestart = False
        self.gameController = gameController
        self.ec = EditorCamera(rotation_smoothing=2, enabled=False, rotation=(30,30,0))
        self.ec.enabled = False
        self.cur = Cursor()
        self.cur.disable()
        self.hide()

    def restart(self):
        self.hardRestart = False
        self.hide()
        camera.orthographic = False
        self.ec.enabled = False
        mouse.locked = True
        mouse.visible = False
        self.cur.disable()
        self.gameController.restartGame()

    def input(self, key):
        if key == 'r' and not self.hardRestart:
            self.restart()
        if key == 'escape' and not self.hardRestart:
            self.text = 'Menu'
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

    def showRestart(self):
        self.hardRestart = True
        print('restart')
        self.text = 'Game Over'
        camera.orthographic = True
        self.show()
        self.ec.enabled = True
        mouse.locked = False
        mouse.visible = False
        self.cur.enable()
