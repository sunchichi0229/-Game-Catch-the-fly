from tkinter import *
from tkinter import messagebox
import random

next_move = None

def clicked():
    window.after_cancel(next_move)
    messagebox.showinfo("Mission Success", "Click成功！おめでとう")
    window.quit()

def btn_move():
    global next_move
    new_x = random.randint(50, 450)
    new_y = random.randint(50, 450)
    delay = random.randint(300, 600)
    next_move = window.after(delay, btn_move)

window = Tk()
window.title("ハリをつかめ！")
window.geometry("500x500")
window.resizable(False, False)

img = PhotoImage(file="fly.jpg")
button = Button(window, image=img,command=clicked)
button.place(x=250, y=250)

btn_move()








window.mainloop()