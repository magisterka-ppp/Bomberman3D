# Create menu
from ursina import Button, color, Cursor, camera, mouse, application
from ursina.prefabs.dropdown_menu import WindowPanel, EditorCamera


class InterfacePanel(WindowPanel):
    def __init__(self, gameController):
        super().__init__(

            title='Game Over',
            popup = True,
            content=(
                Button(text='Restart', color=color.azure, on_click=self.restart),
                Button(text='Exit', color=color.azure, on_click=application.quit),
            ),
        )
        self.gameController = gameController
        self.ec = EditorCamera(rotation_smoothing=2, enabled=False, rotation=(30,30,0))
        self.ec.enabled = False
        self.cur = Cursor()
        self.cur.disable()
        self.hide()

    def input(self, key):
        if key == 'r':
            self.restart()
        if key == 'escape':
            self.switchMenu()

    def restart(self):
        self.gameController.restartGame()
        self.switchMenu()

    def switchMenu(self):
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