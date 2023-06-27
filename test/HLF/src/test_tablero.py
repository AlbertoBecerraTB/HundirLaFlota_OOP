import os, sys
sys.path.append(os.getcwd())
from HLF.utils import config
from HLF.src.tablero import Tablero

def test_init_size():
    size = 5
    tablero_1 = Tablero()
    tablero_2 = Tablero(size)

    cond_1 = tablero_1.BOARD_SIZE == config.BOARD_SIZE
    cond_2 = tablero_2.BOARD_SIZE == size
    assert cond_1&cond_2