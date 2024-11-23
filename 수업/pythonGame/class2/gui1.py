# # 창 띄우기 및 버튼 넣기
import tkinter

root = tkinter.Tk()

root.title("First Program")
root.geometry("800x600")

label = tkinter.Label(root, text="Label Text", font=("System", 16))
label.pack()

entry = tkinter.Entry(root)
entry.pack()

button = tkinter.Button(root, text="Button", font=("System", 16))
button.pack()
root.mainloop()