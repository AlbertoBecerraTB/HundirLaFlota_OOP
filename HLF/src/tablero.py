import os, sys
sys.path.append(os.getcwd())
from HLF.utils import config

class Tablero:
    BOARD_SIZE = config.BOARD_SIZE

    def __init__(self, size=None):
        if size is not None:
            self.BOARD_SIZE = size


if __name__ == "__main__":
    
    tablero_player = Tablero()
    print(tablero_player)