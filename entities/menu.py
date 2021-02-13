# Create menu
from ursina import Button, color, Cursor, camera, mouse, application
from ursina.prefabs.dropdown_menu import WindowPanel, EditorCamera


class InterfacePanel(WindowPanel):
    def __init__(self, gameController):
        super().__init__(
            title='Menu',
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

    def showWin(self):
        self.hardRestart = True
        print('win')
        self.text = 'You won!'
        camera.orthographic = True
        self.show()
        self.ec.enabled = True
        mouse.locked = False
        mouse.visible = False
        self.cur.enable()
