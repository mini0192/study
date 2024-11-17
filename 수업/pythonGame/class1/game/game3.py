# 도착 여부 확인

import random

pl_pos = 1
com_pos = 1

def board():
    print("*" * (pl_pos - 1) + "P" + "*" * (30 - pl_pos) + "GOAL")
    print("*" * (com_pos - 1) + "C" + "*" * (30 - com_pos) + "GOAL")

print("주사위 게임 시작")
while True:
    board()
    input("")
    pl_pos += random.randint(1, 6)
    com_pos += random.randint(1, 6)

    if pl_pos >= 30:
        pl_pos = 30
        print("당신이 승리했습니다")
        break

    if com_pos >= 30:
        com_pos = 30
        print("컴퓨터가 승리했습니다")
        break