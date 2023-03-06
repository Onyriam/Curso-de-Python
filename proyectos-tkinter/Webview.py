import tkinterweb
from tkinter import *

root = Tk()

frame = tkinterweb.HtmlFrame(root)
frame.load_website("https://google.com")
frame.pack()

root.mainloop()
