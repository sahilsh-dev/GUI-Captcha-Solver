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
login_screen.config(bg="lightblue", pady=50)

# Start Screen
start_screen.pack(fill=BOTH, expand=True)
icon_img = PhotoImage(file="icon.png")
canvas = Canvas(start_screen, width=258, height=194)
canvas.create_image(128, 97, image=icon_img)
canvas.pack(pady=20)

start_btn = Button(start_screen, text="Start", font=("Courier", 15, "bold"), command=login, bg='white', width=11)
start_btn.pack(pady=50)

# Login Screen
uid_label = Label(login_screen, text="UID :", font=("Courier", 15, "normal"), bg='white')
uid_label.pack()
uid = Entry(login_screen, width=18, font=("Courier", 13, "normal"))
uid.pack(pady=20)

pswd_label = Label(login_screen, text="Password :", font=("Courier", 15, "normal"), bg='white')
pswd_label.pack(pady=20)
pswd = Entry(login_screen, width=18, font=("Courier", 13, "normal"))
pswd.place(rely=0.5)
pswd.pack()


win.mainloop()
