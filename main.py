from tkinter import *
from login_browser import LoginBrowser


def show_login_screen():
    login_screen.pack(fill='both', expand=True)
    start_screen.pack_forget()


def login_cuims():
    cuims_id = uid.get().strip()
    cuims_pswd = pswd.get().strip()
    if len(cuims_id) >= 9 and len(cuims_pswd) >= 6:
        with open("captcha_solver_project.txt", 'w') as file:
            file.write(f'{cuims_id}: {cuims_pswd}')
        browser.login_cuims(cuims_id, cuims_pswd)


win = Tk()
win.title("GUI Captcha Solver")
win.minsize(width=700, height=500)
win.config(bg="lightblue", padx=50, pady=50)

browser = LoginBrowser()

start_screen = Frame(win)
login_screen = Frame(win)
start_screen.config(bg="lightblue")
login_screen.config(bg="lightblue", pady=20)

# Start Screen
start_screen.pack(fill=BOTH, expand=True)
icon_img = PhotoImage(file="icon.png")
canvas = Canvas(start_screen, width=258, height=194)
canvas.create_image(128, 97, image=icon_img)
canvas.pack(pady=20)

start_btn = Button(start_screen, text="Start", font=("Courier", 15, "bold"), command=show_login_screen, bg='crimson', width=11)
start_btn.pack(pady=50)

# Login Screen
uid_label = Label(login_screen, text="UID", font=("Courier", 15, "bold"), bg='crimson')
uid_label.pack()
uid = Entry(login_screen, width=18, font=("Courier", 13, "normal"))
uid.pack(pady=20)

pswd_label = Label(login_screen, text="Password", font=("Courier", 15, "bold"), bg='crimson')
pswd_label.pack(pady=20)
pswd = Entry(login_screen, width=18, font=("Courier", 13, "normal"))
pswd.pack()

checked_state = IntVar()
check_btn = Checkbutton(login_screen,
                        text='Set Direct Login next time',
                        variable=checked_state,
                        font=("Modern", 11, "normal"),
                        bg='white')

check_btn.pack(pady=30)

login_btn = Button(login_screen, text="Login CUIMS", font=("Courier", 15, "bold"), command=login_cuims, bg='crimson', width=11)
login_btn.pack(pady=30)

win.mainloop()
