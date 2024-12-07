# 이동 거리를 하드코딩

pl_pos = 1
com_pos = 1

def board():
    print("*" * (pl_pos - 1) + "P" + "*" * (30 - pl_pos))
    print("*" * (com_pos - 1) + "C" + "*" * (30 - com_pos))

while True:
    board()
    input("")
    pl_pos += 1
    com_pos += 2