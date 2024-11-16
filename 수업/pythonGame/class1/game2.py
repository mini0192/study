# 이동 거리를 랜덤으로 받기

import random

pl_pos = 1
com_pos = 1

def board():
    print("*" * (pl_pos - 1) + "P" + "*" * (30 - pl_pos))
    print("*" * (com_pos - 1) + "C" + "*" * (30 - com_pos))

while True:
    board()
    input("")
    pl_pos += random.randint(1, 6)
    com_pos += random.randint(1, 6)