data = 3

def functionA():
    global data
    data = 5
    print(data)

functionA()
print(data)
