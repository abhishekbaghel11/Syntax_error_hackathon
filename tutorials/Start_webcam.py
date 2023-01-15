# To close the webcam--> press button 'q' and then the cross button

# importing the important libraries

from tkinter import *
from PIL import Image, ImageTk
import tkinter.font as font

import pandas as pd
import mysql.connector

import cv2
import requests
import imutils
import numpy as np
import face_recognition as fr
import os
from datetime import datetime

root = Tk()
root.title("Attendance")
root.geometry('300x300')

bg_img = ImageTk.PhotoImage(file='E:\\Syntax Error\\test_img\\grass_an.png')

frame=Frame(root, width=300, height=300)
frame.grid(row=0, column=0, sticky="NW")

l = Label(frame,image=bg_img)
l.pack()

# Calling the attendance register program using the button
def clicked1():
    exec(open("E:\\Syntax Error\\tutorials\\attendance_register.py").read())

# Button to call another program 
btn = Button(root, text="Start the Webcam", fg = 'black', command = clicked1, anchor = CENTER)
btn.place(relx = 0.5,rely = 0.5 , anchor = CENTER)

root.resizable(False,False)
root.mainloop()