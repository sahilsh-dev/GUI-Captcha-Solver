from tkinter import *


def login():
    login_screen.pack(fill='both', expand=True)
    start_screen.pack_forget()


win = Tk()
win.title("GUI Captcha Solver")
win.minsize(width=700, height=500)
win.config(bg="lightblue", padx=50, pady=50)

start_screen = Frame(win)
login_screen = Frame(win)
start_screen.config(bg="lightblue")
login_screen.config(bg="lightblue")

# Start Screen
start_screen.pack(fill=BOTH, expand=True)
icon_img = PhotoImage(file="icon.png")
canvas = Canvas(start_screen, width=258, height=194)
canvas.create_image(128, 97, image=icon_img)
canvas.pack(pady=20)

start_btn = Button(start_screen, text="Start", font=("Courier", 15, "normal"), command=login, width=11)
start_btn.pack(pady=50)

# Login Screen
uid_label = Label(login_screen, text="UID :")
uid_label.pack(pady=10)
uid = Entry(login_screen, width=20)
uid.pack()

pswd_label = Label(login_screen, text="Password :")
pswd_label.pack(pady=10)
pswd = Entry(login_screen, width=20)
pswd.pack()


win.mainloop()
