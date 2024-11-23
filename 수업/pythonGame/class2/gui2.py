# 버튼 이벤트
import tkinter
import random

count = 0
data = random.randint(1, 100)
print(data)

minRank = 100

def clickEvent():
    global count
    global data
    global minRank

    inputData = entry.get()

    if(inputData):
        num = int(inputData)
        if(data == num):
            data = random.randint(1, 100)
            print(data)
            if(count < minRank):
                minRank = count
                rankLabel["text"] = "TOP RANK: {}".format(minRank)
            count = 0
            statusLabel["text"] = "YOU WIN"
        elif(data > num):
            statusLabel["text"] = "UP"
        elif(data < num):
            statusLabel["text"] = "DOWN"
        count += 1
        countLabel["text"] = count
root = tkinter.Tk()

root.title("First Program")
root.geometry("800x600")

titleLabel = tkinter.Label(root, text="UP & DOWN GAME", font=("System", 16))
titleLabel.pack()

countLabel = tkinter.Label(root, text="0", font=("System", 16))
countLabel.pack()

statusLabel = tkinter.Label(root, text="", font=("System", 16))
statusLabel.pack()

entry = tkinter.Entry(root)
entry.pack()

button = tkinter.Button(root, text="Button", font=("System", 16), command=clickEvent)
button.pack()

rankLabel = tkinter.Label(root, text="TOP RANK:", font=("System", 16))
rankLabel.pack()

root.mainloop()