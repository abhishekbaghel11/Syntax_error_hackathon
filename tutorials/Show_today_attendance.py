# Importing important libraries

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
root.title("Today's Attendance")
root.geometry('400x600')
root.configure(bg = '#67c443')

main_frame = Frame(root)
main_frame.pack(fill = BOTH,expand=1)

Can = Canvas(main_frame)
Can.pack(side = LEFT,fill = BOTH,expand=1)

scroll_bar = Scrollbar(main_frame, orient=VERTICAL, command= Can.yview)
scroll_bar.pack(side = RIGHT, fill = Y)

Can.configure(yscrollcommand=scroll_bar.set)
Can.bind('<Configure>', lambda e:  Can.configure(scrollregion= Can.bbox("all")))

supp_frame = Frame(Can)

Can.create_window((0,0),window=supp_frame, anchor="nw") 

# Establishing connection with the database
connection = mysql.connector.connect(host='localhost',
                                     database='my_new_database',
                                     user='root',
                                     password='Abhishek@123iitr')

cursor = connection.cursor()

# selecting only today's attendance
sql_select_Query = '''select * from attend where date = %s'''
now = datetime.now()
dtString = now.strftime("%d/%m/%Y")
d=(dtString,)
cursor.execute(sql_select_Query,d)

font_style_custom = font.Font(family='Comic Sans MS',size = 15,weight='bold')

a_main = Label(supp_frame, text="Name-Date",font=font_style_custom)
a_main.pack()
attendees = cursor.fetchall()
for i in attendees:
    a = Label(supp_frame, text=f"{i[0]}-{i[1]}",font=font_style_custom)
    a.pack()

root.resizable(False,True)
connection.commit()
root.mainloop()