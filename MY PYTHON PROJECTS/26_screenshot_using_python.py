import pyautogui
from tkinter import *

def take_screenshot():
    add_data = entry.get()
    path = add_data + "\\test12.png"
    screenshot = pyautogui.screenshot()
    screenshot.save(path)

win = Tk()
win.title('Screenshot Taker')
win.geometry('700x300')
win.config(bg = 'yellow')
win.resizable(False, False)
entry = Entry(win, font = ('Times New Roman', 30))
entry.place(x =20, height = 70, width = 660, y = 50)
button = Button(win, text = 'Done', font = ('Times New Roman', 50), command=take_screenshot)
button.place(x = 250, y = 140, height = 100, width = 200)



win.mainloop()