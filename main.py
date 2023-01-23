from tkinter import *
from login_browser import LoginBrowser


def direct_login():
    with open("captcha_solver_project.txt") as file:
        data = file.readline().strip()
        if data:
            text = data.split(':')
            cuims_id = text[0].split()
            cuims_pswd = text[1].split()
            browser.login_cuims(cuims_id, cuims_pswd)


def show_login_screen():
    login_screen.pack(fill='both', expand=True)
    start_screen.pack_forget()


def login_cuims():
    cuims_id = uid.get().strip()
    cuims_pswd = pswd.get().strip()
    if len(cuims_id) >= 8 and len(cuims_pswd) >= 6:
        if checked_state.get() == 1:
            with open("captcha_solver_project.txt", 'w') as file:
                file.write(f'{cuims_id} : {cuims_pswd}')
                print("Saved")
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

start_btn = Button(start_screen, text="Start", font=("Courier", 15, "bold"),
                   command=show_login_screen, bg='crimson', width=11)
start_btn.place(x=130, y=280)
direct_login_btn = Button(start_screen, text="Direct Login", font=("Courier", 15, "bold"),
                          command=direct_login, bg='crimson', width=11)
direct_login_btn.place(x=330, y=280)

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

check_btn.pack(pady=40)

login_btn = Button(login_screen, text="Login CUIMS", font=("Courier", 15, "bold"),
                   command=login_cuims, bg='crimson', width=11)
login_btn.pack(pady=30)

win.mainloop()
