from tkinter import *


def start():
    print("Click")


win = Tk()
win.title("GUI Captcha Solver")
win.minsize(width=700, height=500)
win.config(bg="lightblue", padx=50, pady=50)

icon_img = PhotoImage(file="icon.png")
canvas = Canvas(win, width=258, height=194)
canvas.create_image(128, 97, image=icon_img)
canvas.pack(pady=20)

start_btn = Button(text="Start", font=("Courier", 15, "normal"), command=start, width=11)
start_btn.pack(pady=50)


win.mainloop()
