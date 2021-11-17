import numpy
from time import sleep
from alert import alert
from warnings import filterwarnings
from pyautogui import screenshot
from pytesseract import pytesseract
import cv2

pytesseract.tesseract_cmd = "Tesseract-OCR\\tesseract.exe"
filterwarnings("ignore")

indicator = input("indicator: ")  # "Student password:"
interval = int(input("interval: "))

while not indicator in pytesseract.image_to_string(
    cv2.threshold(
        numpy.asarray(screenshot().convert("L")).astype(numpy.uint8),
        0,
        255,
        cv2.THRESH_OTSU,
    )[1]
):
    sleep(interval)
alert()
