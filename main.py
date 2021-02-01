from ursina import *

from blocks import Ground, Wall, HardWall
from bomber import Bomber
from buffs import Buff
from constants import WORLD_SCALE
from menu import InterfacePanel
from myFirstPersonController import MyFirstPersonController
from skybox import Skybox


class GameController:
    def __init__(self):
        self.snd_gameWin = Audio('./snd/game_win.wav', pitch=1, loop=False, autoplay=False)
        self.snd_gameLose = Audio('./snd/game_lose.wav', pitch=1, loop=False, autoplay=False)
        self.snd_putBomb = Audio('./snd/Pickup_Coin4.wav', pitch=1, loop=False, autoplay=False)
        self.snd_explode = Audio('./snd/Explosion4.wav', pitch=1, loop=False, autoplay=False)

    def loadMap(self):
        # example (spawn in up left corner)
        map_quarter = [
            [2, 2, 2, 2, 2, 2, 2, 2, 2, 2],
            [2, 0, 0, 1, 1, 1, 0, 0, 1, 1],
            [2, 0, 1, 0, 0, 1, 0, 1, 1, 0],
            [2, 1, 0, 1, 0, 0, 0, 0, 1, 0],
            [2, 1, 0, 0, 1, 0, 0, 0, 1, 0],
            [2, 1, 1, 0, 0, 1, 1, 1, 1, 1],
            [2, 0, 0, 0, 0, 1, 1, 1, 1, 1],
            [2, 0, 1, 0, 0, 1, 1, 0, 0, 0],
            [2, 1, 1, 1, 1, 1, 1, 0, 1, 0],
            [2, 1, 0, 0, 0, 1, 1, 0, 0, 1],
        ]
        x = len(map_quarter)
        z = len(map_quarter[0])
        self.current_map = [[0] * x * 2 for _ in range(z * 2)]
        for i in range(x):
            for j in range(z):
                self.current_map[i][j] = map_quarter[i][j]
                self.current_map[2*x-1-i][j] = map_quarter[i][j]
                self.current_map[i][2*z-1-j] = map_quarter[i][j]
                self.current_map[2*x-1-i][2*z-1-j] = map_quarter[i][j]
        self.world_size_x = x*2
        self.world_size_z = z*2

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
        print('generate walls')
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
        self.walls.clear()
        for wall in self.ground:
            destroy(wall)
        self.ground.clear()
        for wall in self.hardWall:
            destroy(wall)
        self.hardWall.clear()
        self.loadBlocks()

    def loadEnemy(self):
        self.enemy_table = [
            Bomber(self, (1 * WORLD_SCALE, 1 * WORLD_SCALE, (self.world_size_x - 2) * WORLD_SCALE)),
            Bomber(self, ((self.world_size_x - 2) * WORLD_SCALE, 1 * WORLD_SCALE, 1 * WORLD_SCALE)),
            Bomber(self, ((self.world_size_x - 2) * WORLD_SCALE, 1 * WORLD_SCALE, (self.world_size_x - 2) * WORLD_SCALE))
        ]

    def reloadEnemy(self):
        for enemy in self.enemy_table:
            destroy(enemy)
        self.enemy_table.clear()
        self.loadEnemy()

    def loadBuff(self):
        self.buff_table = []

    def reloadBuff(self):
        for buff in self.buff_table:
            destroy(buff)
        self.buff_table.clear()
        self.loadBuff()

    def setBuff(self, position):
        self.buff_table.append(Buff(self, position))

    def startGame(self):
        self.loadMap()
        self.loadMenu()
        self.loadBlocks()
        self.loadPlayer()
        self.loadEnemy()
        self.loadBuff()
        self.app = app
        Skybox()

    def restartGame(self):
        self.loadMap()
        self.reloadBlocks()
        self.reloadPlayer()
        self.reloadEnemy()
        self.reloadBuff()

if __name__ == '__main__':
    app = Ursina()
    Texture.default_filtering = None
    window.fps_counter.enabled = True
    window.exit_button.visible = False

    gameController = GameController()
    gameController.startGame()
    NoclipMode(speed=10, require_key='shift')
    app.run()
