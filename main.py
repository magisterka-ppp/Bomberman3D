from ursina import *

from blocks import Ground, Wall, HardWall
from bomber import Bomber
from constants import WORLD_SCALE
from menu import InterfacePanel
from myFirstPersonController import MyFirstPersonController
from skybox import Skybox

snd_putBomb = Audio('./snd/Pickup_Coin4.wav', pitch=1, loop=False, autoplay=False)
snd_explode = Audio('./snd/Explosion4.wav', pitch=1, loop=False, autoplay=False)


class GameController:
    def loadMap(self):
        self.current_map = [
            [2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2],
            [2, 0, 1, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 2],
            [2, 0, 1, 0, 1, 0, 1, 1, 0, 1, 1, 1, 1, 1, 1, 1, 0, 1, 0, 2],
            [2, 0, 1, 0, 1, 0, 0, 1, 1, 1, 1, 0, 0, 0, 0, 0, 0, 1, 0, 2],
            [2, 0, 1, 0, 1, 0, 1, 1, 0, 0, 1, 0, 0, 1, 1, 1, 0, 1, 0, 2],
            [2, 0, 0, 0, 0, 0, 0, 1, 0, 0, 1, 0, 0, 1, 1, 1, 0, 1, 0, 2],
            [2, 1, 1, 1, 1, 1, 0, 1, 0, 0, 0, 0, 0, 1, 1, 1, 0, 1, 0, 2],
            [2, 0, 0, 1, 0, 1, 0, 1, 0, 1, 1, 1, 1, 1, 0, 0, 0, 0, 0, 2],
            [2, 0, 0, 0, 0, 0, 0, 0, 0, 1, 1, 1, 1, 1, 0, 1, 0, 1, 0, 2],
            [2, 1, 1, 0, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 0, 1, 0, 1, 0, 2],
            [2, 1, 1, 0, 1, 1, 1, 1, 1, 1, 1, 0, 0, 0, 0, 1, 1, 1, 0, 2],
            [2, 0, 1, 0, 1, 0, 0, 0, 0, 1, 0, 1, 0, 1, 0, 1, 1, 1, 0, 2],
            [2, 0, 1, 0, 1, 0, 1, 1, 0, 0, 0, 1, 0, 1, 0, 1, 0, 0, 0, 2],
            [2, 0, 1, 0, 1, 0, 0, 1, 1, 1, 0, 1, 0, 1, 0, 1, 1, 0, 1, 2],
            [2, 0, 1, 0, 1, 0, 1, 1, 0, 1, 0, 1, 1, 1, 0, 1, 1, 1, 1, 2],
            [2, 0, 0, 0, 0, 0, 0, 1, 0, 1, 0, 0, 0, 0, 0, 1, 0, 0, 0, 2],
            [2, 1, 1, 1, 1, 1, 0, 1, 0, 1, 1, 1, 1, 1, 0, 1, 0, 1, 0, 2],
            [2, 0, 0, 1, 0, 1, 0, 1, 0, 1, 1, 1, 1, 1, 1, 1, 1, 1, 0, 2],
            [2, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 2],
            [2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2]
        ]
        self.world_size_x = len(self.current_map[0])
        self.world_size_z = len(self.current_map)

    def loadPlayer(self):
        self.player = MyFirstPersonController()

    def reloadPlayer(self):
        destroy(self.player)
        self.loadPlayer()

    def loadMenu(self):
        self.panel = InterfacePanel(self)

    def reloadMenu(self):
        destroy(self.panel)
        self.loadMenu()

    def loadBlocks(self):
        self.walls = []
        self.ground = []
        self.hardWall = []
        for z in range(self.world_size_z):
            for x in range(self.world_size_x):
                self.ground.append(Ground(self, (x * WORLD_SCALE, 0, z * WORLD_SCALE)))
                if self.current_map[z][x] == 1:
                    self.walls.append(Wall(self, (x * WORLD_SCALE, 1 * WORLD_SCALE, z * WORLD_SCALE)))
                if self.current_map[z][x] == 2:
                    self.hardWall.append(HardWall(self, (x * WORLD_SCALE, 1 * WORLD_SCALE, z * WORLD_SCALE)))

    def reloadBlocks(self):
        for wall in self.walls:
            destroy(wall)
        for wall in self.ground:
            destroy(wall)
        for wall in self.hardWall:
            destroy(wall)
        self.loadBlocks()

    def loadEnemy(self):
        self.enemy_table = [
            Bomber(self, (1 * WORLD_SCALE, 1 * WORLD_SCALE, 1 * WORLD_SCALE)),
            Bomber(self, (18 * WORLD_SCALE, 1 * WORLD_SCALE, 18 * WORLD_SCALE)),
            Bomber(self, (1 * WORLD_SCALE, 1 * WORLD_SCALE, 18 * WORLD_SCALE))
        ]

    def reloadEnemy(self):
        for enemy in self.enemy_table:
            destroy(enemy)

    def startGame(self):
        self.loadMap()
        self.loadPlayer()
        self.loadMenu()
        self.loadBlocks()
        self.loadEnemy()
        self.app = app
        Skybox()

    def restartGame(self):
        self.loadMap()
        self.reloadPlayer()
        self.reloadMenu()
        self.reloadBlocks()
        self.reloadEnemy()




if __name__ == '__main__':
    app = Ursina()
    Texture.default_filtering = None
    window.fps_counter.enabled = True
    window.exit_button.visible = False

    gameController = GameController()
    gameController.startGame()
    gameController.restartGame()
    app.run()
