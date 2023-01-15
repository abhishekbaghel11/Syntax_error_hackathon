# Face-Recognition-Attendance-System
This is the project for the Hackathon 'Syntax Error'

Introduction to Project : 
This is a python project which will make the attendance system efficient in terms of time and proxy. Idea is to record attendance by scanning faces of students.

Description of Files and Programs :
Start_webcam.py--> This program opens up a window and by clicking on the start webcam button, webcam opens up and starts reading the faces and update the attendace in the csv file and then in the database.

attendance_register.py--> This contains the main code for the face recognition program and is called by the start webcam button in the start_webcam.py file.

push_to_database.py--> This contains the code for reading the csv file and then updating the information to the database.

Show_today_attendance.py--> This program opens up a window displaying records of today's attendance by extracting data from database.

Attendance.csv--> This contains the records of the recognised faces(present students).

attendance_img--> This folder contains the images of all the students for reference.

test_img--> This folder contains background image of the initial pop-up window.
