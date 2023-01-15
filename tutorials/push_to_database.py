# Importing the important libraries

import pandas as pd
import mysql.connector

# reading csv file
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

    name_index = list(range(0,len(nameList)))

# establishing connection with the database
connection = mysql.connector.connect(host='localhost',
                                     database='my_new_database',
                                     user='root',
                                     password='Abhishek@123iitr')
cursor = connection.cursor()

cursor.execute('''DROP TABLE attend''')

cursor.execute('''
		CREATE TABLE attend (
			name text,
			date text
			)
               ''')

# adding entries into the database
for index in name_index:
    if(index != 0):
        abc = 'INSERT INTO attend (name, date) VALUES (%s,%s)'
        mytup = (nameList[index],dateList[index])
        cursor.execute(abc,mytup)

connection.commit()