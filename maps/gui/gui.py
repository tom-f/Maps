from main_window import MainWindow
from Tkinter import Tk

class Gui(object):
    def __init__(self):
        root = Tk()
        root.geometry("250x150+300+300")
        app = MainWindow(root)
        root.mainloop()

