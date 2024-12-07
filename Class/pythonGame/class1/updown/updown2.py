import random

user = dict()

while True:
    count = 0
    data = random.randint(1, 100)
    print(data)
    while True:
        count += 1
        get = int(input("입력: "))
        if data == get:
            break
        if data < get:
            print("DOWN")
            continue
        if data > get:
            print("UP")
            continue

    print("이겼음")
    user[input("이름: ")] = count
    sortUser = sorted(user.items(), key=lambda x: x[1])
    print(sortUser)