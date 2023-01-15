# importing the important libraries

import cv2
import requests
import imutils
import numpy as np
import face_recognition as fr
import os
from datetime import datetime

# Connecting to webcam student_names--> 
# REDMI_NOTE_9
# url = "https://192.168.103.213:8080/video"

# SAMSUNG S20
url = "https://192.168.103.218:8080/video"


path = 'attendance_img'
images = []
student_names = []
# passing the images as list in the mylist
mylist = os.listdir(path)

for imgN in mylist:
    # adding the images to 'images' list
    curImg = cv2.imread(f'{path}/{imgN}')
    images.append(curImg)
    # taking only the name from the image files
    student_names.append(os.path.splitext(imgN)[0])

# Function to find the encodings of the already available images
def findEncodings(images):
    encodelist = []
    for img in images:
        img = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)
        encode = fr.face_encodings(img)[0]
        encodelist.append(encode)
    return encodelist

# Attendance marking function
def markAttendance(name,d):
    with open('E:\Syntax Error\Attendance.csv','r+') as f:
        myDataList = f.readlines()
        nameList = []
        dateList = []
        # a created to prevent to clear the last letter of date_string
        a = 0
        for line in myDataList:
            a += 1  
            entry = line.split(',')
            nameList.append(entry[0])
            # last entry should not be altered
            if a != len(myDataList):
                # to clear the last letter of the string
                entry[1] = entry[1].rstrip(entry[1][-1])
            # date appended in the list 
            dateList.append(entry[1])
            
        # conditions so that the name does not get added multiple times 
        if (name not in nameList):
            f.writelines(f'\n{name},{d}')
        elif((name in nameList)):
            final_index = max(index for index, item in enumerate(nameList) if item == name)
            if((d != dateList[final_index]) ):
                f.writelines(f'\n{name},{d}')
            
known_encodings = findEncodings(images)
print("Encoding Complete")

# Initialiazing webcam
cap = cv2.VideoCapture(url)

while True:
    success, img = cap.read()
    img_small = cv2.resize(img, (0, 0), None, 0.25,0.25)
    img_small = cv2.cvtColor(img_small, cv2.COLOR_BGR2RGB)
    faces_in_cur_frame = fr.face_locations(img_small)
    encodes_of_cur_frame = fr.face_encodings(img_small,faces_in_cur_frame)

    # comparing the encodings and finding the best match 
    for encodeFace,faceLoc in zip(encodes_of_cur_frame,faces_in_cur_frame):
        match_compare = fr.compare_faces(known_encodings,encodeFace)
        face_error = fr.face_distance(known_encodings,encodeFace)
        # taking the minimum argument
        matchIndex = np.argmin(face_error)

        if match_compare[matchIndex]:
            # turning the name into uppercases
            name = student_names[matchIndex].upper()
            y1,x2,y2,x1 = faceLoc
            y1,x2,y2,x1 = y1*4,x2*4,y2*4,x1*4
            # making rectangle around the detected faces
            cv2.rectangle(img,(x1,y1),(x2,y2),(128, 159, 255),2)
            cv2.putText(img,name,(x1+6,y2+30),cv2.FONT_HERSHEY_COMPLEX,1,(45, 179, 0),2)
            now = datetime.now()
            dtString = now.strftime("%d/%m/%Y")
            markAttendance(name,dtString)

    if img is not None:
        cv2.imshow("Frame:--> press 'q' to exit",img)
    q = cv2.waitKey(2)
    # press q to exit the program
    if q == ord("q"):
        break

    exec(open("E:\\Syntax Error\\tutorials\\push_to_database.py").read())