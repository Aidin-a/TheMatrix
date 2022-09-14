import tkinter
import tkinter.font
import tkinter.ttk as ttk
from tkinter.constants import *

import lib


def start():
    Login = tkinter.Tk()
    Login.title("The Matrix")
    photo = tkinter.PhotoImage(file='./Icons/Logo.png')
    Login.wm_iconphoto(True, photo)
    LoginFrame = tkinter.Frame(padx=5, pady=5)
    UNameFrame = tkinter.Frame(padx=5, pady=5)
    PAsswFrame = tkinter.Frame(padx=5, pady=5)
    font = tkinter.font.Font(font="Roboto 10")
    screen_width = Login.winfo_screenwidth()
    screen_height = Login.winfo_screenheight()

    # calculate position x and y coordinates
    x = (screen_width/2) - (300/2)
    y = (screen_height/2) - (235/2)
    Login.geometry('%dx%d+%d+%d' % (300, 235, x, y))

    def login():
        uname = UName.get()
        passw = PAssw.get()
        if uname == "Administrator" and passw == "85208520":
            lib.startGame()
        else:
            lblUName.configure(foreground="#ff0000")
            lblPAssw.configure(foreground="#ff0000")

    ttk.Label(master=Login, font=tkinter.font.Font(font="Roboto 25"), padding=15, text="The Matrix").pack()
    UName = ttk.Entry(master=UNameFrame, font=font, width=250)  # UName
    PAssw = ttk.Entry(master=PAsswFrame, show="*", font=font, width=250)  # PAssw
    ttk.Button(master=LoginFrame, text="Login", width=20, padding=2.5, command=login).pack()  # SUbmt
    lblUName = ttk.Label(master=Login, font=font, padding=1, text="Enter Username:")
    lblUName.pack()
    UName.pack()
    UNameFrame.pack()
    lblPAssw = ttk.Label(master=Login, font=font, padding=1, text="Enter Password:")
    lblPAssw.pack()
    PAssw.pack()
    PAsswFrame.pack()
    LoginFrame.pack()
    Login.resizable(False, False)
    tkinter.mainloop()
