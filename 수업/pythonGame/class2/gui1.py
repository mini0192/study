import tkinter

root = tkinter.Tk()

def clickEvent():
    label["text"] = "Hello world"
    print("click")

root.title("First Program")
root.geometry("800x600")

label = tkinter.Label(root, text="Up and Down Game", font=("System", 20))
label.pack()

entry = tkinter.Entry(root)
entry.pack()

button = tkinter.Button(root, text="Button", font=("System", 16), command=clickEvent)
button.pack()

root.mainloop()