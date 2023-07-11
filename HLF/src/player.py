import numpy as np

import os, sys
sys.path.append(os.getcwd())
from HLF.utils import config

class Player:
    WATER_SIGN = config.WATER_SIGN
    HIT_SIGN = config.HIT_SIGN
    def __init__(self, name):
        self.name = name

    def shoot(self, x, y, tablero):
        tab = tablero.tablero.copy()
        if tab[x, y] == tablero.EMPTY_SIGN:
            tab[x, y] = self.WATER_SIGN
        elif tab[x, y] == tablero.BOAT_SIGN:
            tab[x, y] = self.HIT_SIGN
        elif (tab[x, y] == self.WATER_SIGN) |\
             (tab[x, y] == self.HIT_SIGN):
            raise ValueError("Aquí ya has disparado")
        
        return tab

if __name__ == "__main__":
    from HLF.src.tablero import Tablero
    tablero = Tablero()
    player = Player("Alberto")
    print(player)