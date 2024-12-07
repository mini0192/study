# 도착 여부 확인

import random

pl_pos = 1
com_pos = 1

def board():
    print("*" * (pl_pos - 1) + "P" + "*" * (30 - pl_pos) + "GOAL")
    print("*" * (com_pos - 1) + "C" + "*" * (30 - com_pos) + "GOAL")

count = int(input("입력: "))
print("주사위 게임 시작")
for i in range(count):
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

if pl_pos > com_pos:
    print("당신이 승리했습니다")
elif com_pos > pl_pos:
    print("컴퓨터가 승리했습니다")
else:
    print("무승부 입니다.")