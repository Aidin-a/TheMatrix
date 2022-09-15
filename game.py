import tkinter
import tkinter.font
import tkinter.ttk as ttk
import lib


def login():
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
    x = (screen_width / 2) - (300 / 2)
    y = (screen_height / 2) - (235 / 2)
    Login.geometry('%dx%d+%d+%d' % (300, 235, x, y))

    def loginCheck():
        uname = UName.get()
        passw = PAssw.get()
        if uname == "1" and passw == "1":
            lib.showGameWindow(Login)
        else:
            lblUName.configure(foreground="#ff0000")
            lblPAssw.configure(foreground="#ff0000")

    ttk.Label(master=Login, font=tkinter.font.Font(font="Roboto 25"), padding=15, text="The Matrix").pack()
    UName = ttk.Entry(master=UNameFrame, font=font, width=250)  # UName
    PAssw = ttk.Entry(master=PAsswFrame, show="*", font=font, width=250)  # PAssw
    ttk.Button(master=LoginFrame, text="Login", width=20, padding=2.5, command=loginCheck).pack()  # SUbmt
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


def start(geometries):
    gameWindow = tkinter.Tk()
    gameWindow.title("The Matrix")
    photo = tkinter.PhotoImage(file='./Icons/Logo.png')
    # gameWindow.wm_iconphoto(True, photo)
    screen_width = gameWindow.winfo_screenwidth()
    screen_height = gameWindow.winfo_screenheight()
    x = (screen_width / 2) - (int(geometries[0]) / 2)
    y = (screen_height / 2) - (int(geometries[1]) / 2)
    gameWindow.geometry('%dx%d+%d+%d' % (int(geometries[0]), int(geometries[1]), x, y))
    gameWindow.resizable(False, False)
