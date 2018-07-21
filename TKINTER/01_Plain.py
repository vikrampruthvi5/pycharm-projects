from tkinter import *

root = Tk()
frame1 = Frame(root)
frame1.pack()
frame2 = Frame(root)
frame2.pack()


def foo():
    print("Purta")


CA1 = Button(frame1, text = "Carrie", command = foo)
CA1.pack()
CA2 = Label(frame2, text = "Rich")
CA2.pack()
root.mainloop()