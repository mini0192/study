import random

data = random.randint(1, 100)
print(data)
while True:
    get = int(input("입력: "))
    if data == get:
        break
    if data < get:
        print("DOWN")
        continue
    if data > get:
        print("UP")
        continue