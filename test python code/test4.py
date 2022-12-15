# importing required packages
import tkinter
from PIL import ImageTk, Image
import os

# creating main window
root = tkinter.Tk()

# loading the image

# reading the image
def test() :
    img = ImageTk.PhotoImage(Image.open("test.png"))
    panel = tkinter.Label(root, image = img)
    panel.pack(side = "bottom", fill = "both", expand = "yes")

test()

# setting the application


# running the application
root.mainloop()
