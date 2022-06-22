from pynput.mouse import Button, Controller
import keyboard
import time
import tkinter
import pyperclip
from PIL import Image, ImageGrab


from tkinter import *

root = Tk()
root.geometry("500x500")
root.title("Mouse Utils")
root.config(bg="#ae8fff")


HelpText = Label(root, text="You can click on the eg. cords to copy them.\nPress C for mouse coordinates.\nPress V for RGB color.")
HelpText.configure( foreground="#f3f2f2", pady="10", padx="20", bg="#171515")


Cords = Label(root, text="Cords")
Cords.configure(background="#9472ed", foreground="#e3d9ff", borderwidth=4, relief="raised", pady="10", padx="20")
Color = Label(root, text="Color")
Color.configure(background="#9472ed", foreground="#e3d9ff", borderwidth=4, relief="raised", pady="10", padx="20")



valCall_Cords = ""
valCall_Color = ""

#######################
def callbackCords(arg1):
    if valCall_Cords == "":
        return
    pyperclip.copy(arg1)
def callbackColor(arg1):
    if valCall_Color == "":
        return
    pyperclip.copy(arg1)
#######################

def getMouseCoords():
    mouse = Controller()
    return  str(mouse.position);

def Events(event):
    if event.keysym == 'c':
        Cords.config(text = "Cords: " + getMouseCoords())
        global valCall_Cords
        valCall_Cords = getMouseCoords()
        print(getMouseCoords())
    if event.keysym == 'v':
        mouse = Controller()
        pos = mouse.position
        px = ImageGrab.grab().load()
        color = px[list(pos)[0], list(pos)[1]]
        Color.config(text="Color: " + str(color))
        global valCall_Color
        valCall_Color = str(color)
        print(color)



HelpText.pack()
Cords.pack(padx=20, pady=20)
Color.pack(padx=20, pady=20)
Cords.bind("<Button-1>", lambda e: callbackCords(valCall_Cords))
Color.bind("<Button-1>", lambda e: callbackColor(valCall_Color))



root.bind("<KeyRelease>", Events)

root.mainloop()






