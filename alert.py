from tkinter import Tk, messagebox
from os import environ
environ["PYGAME_HIDE_SUPPORT_PROMPT"] = "hide"
from pygame import mixer

def alert(message):
    root = Tk()
    root.withdraw()
    mixer.init()
    mixer.music.load("beep.wav")
    mixer.music.play(-1)
    messagebox.showwarning("Alarm", message)