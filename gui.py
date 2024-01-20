import tkinter
import cv2
import face_recognition
import os
import sys
import numpy as np
from attendance import AttendanceMgr

def clear():
    print('clear')

def takePic():
    Id = (inputStudentNum.get())
    name = (inputStudentName.get())
    if ((name.isalpha()) or (' ' in name)):

        cam = cv2.VideoCapture(0)
        ret, img = cam.read()
        gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

        while True:
            ret, frame = cam.read()
            if not ret:
                print("failed to grab frame")
                break

            small_frame = cv2.resize(frame, (0, 0), fx=0.25, fy=0.25)
            rgb_small_frame = cv2.cvtColor(small_frame, cv2.COLOR_BGR2RGB)
            face_locations = face_recognition.face_locations(rgb_small_frame)

            for top, right, bottom, left in face_locations:
                top *= 4
                right *= 4
                bottom *= 4
                left *= 4

                cv2.rectangle(frame, (left, top), (right, bottom), (0, 255, 0))

            cv2.imshow("Position your face in the middle of camera and press space...", frame)

            k = cv2.waitKey(1)
            if k % 256 == 32:
                # SPACE pressed
                img_name = "{}.{}.png".format(Id, name)
                cv2.imwrite('images/' + img_name, frame)
                print("{} written!".format(img_name))
                break

            if cv2.waitKey(1) == ord('q'):
                break

        cam.release()
        cv2.destroyAllWindows()
        res = name + ' registered successfully.'
        message.configure(text=res)
    else:
        if not name.isalpha():
            res = "Enter Correct name"
            message.configure(text=res)


def takeAttendance():
    att = AttendanceMgr()
    att.takeAttendance()


# Display application window
window = tkinter.Tk()
window.title(" Student Attendance System")
window.geometry("1280x720")
window.resizable(True,True)
window.configure(background='#051650')

# Title in Application Window
title = tkinter.Label(window, text="Smart Student Attendance System",
                         fg="white", bg="#051650", width=60, height=1, font=('Helvetica', 30, ' normal '))
title.place(x=10, y=10, relwidth=1)

# Registration frame
regFrame = tkinter.Frame(window, bg='#ADD8E6')
regFrame.place(relx=0.05, rely=0.1, relwidth=0.40, relheight=0.80)

# header of Registration frame
regFrameHeader = tkinter.Label(regFrame, text="Register New Student", fg="#051650", bg="white", font=('Helvetica', 17, ' bold '))
regFrameHeader.place(x=0, y=0, relwidth=1)

# Label of student number
lbStudentNum = tkinter.Label(regFrame, text="Student Number", width=20, height=1, fg="black", bg="#ADD8E6", font=('Helvetica', 15, ' bold ') )
lbStudentNum.place(x=10, y=55)

# Input box of Student number
inputStudentNum = tkinter.Entry(regFrame,width=32 ,fg="black",bg="#e1f2f2",highlightcolor="#00aeff",highlightthickness=3,font=('Helvetica', 15, ' bold '))
inputStudentNum.place(x=45, y=88, relwidth=0.75)

# Label of student name
lbStudentName = tkinter.Label(regFrame, text="Student Name", width=20,fg="black",bg="#ADD8E6",font=('Helvetica', 15, ' bold '))
lbStudentName.place(x=0, y=140)

# Input box of student name
inputStudentName = tkinter.Entry(regFrame, width=32, fg="black", bg="#e1f2f2", highlightcolor="#00aeff", highlightthickness=3, font=('Helvetica', 15, ' bold ')  )
inputStudentName.place(x=45, y=173,relwidth=0.75)

# Clear buttons
clearButton = tkinter.Button(regFrame, text="Clear", command=clear, fg="black", bg="green", width=11, activebackground = "green", font=('Helvetica', 12, ' bold '))
clearButton.place(x=45, y=230, relwidth=0.29)

# Take Picture buttons
takePicButton = tkinter.Button(regFrame, text="Take Pictures", command=takePic, fg="black", bg="#051650", width=34, height=1, activebackground="grey", font=('Helvetica', 16, ' bold '))
takePicButton.place(x=30, y=350, relwidth=0.50)

### End of registratipon frame

# Attendance panel
attFrame = tkinter.Frame(window, bg="#ADD8E6")
attFrame.place(relx=0.56, rely=0.1, relwidth=0.40, relheight=0.80)

# header of Registration frame
attFrameHeader = tkinter.Label(attFrame, text="Mark Attendance", fg="#051650", bg="white", font=('Helvetica', 17, ' bold '))
attFrameHeader.place(x=0, y=0, relwidth=1)

# Taking attendance button
takeAttendanceButton = tkinter.Button(attFrame, text="Take Attendance", command=takeAttendance, fg="black", bg="#00aeff", height=1, activebackground = "white" ,font=('Helvetica', 16, ' bold '))
takeAttendanceButton.place(x=30,y=60,relwidth=0.89)

# Exit button for exiting application
exitButton = tkinter.Button(attFrame, text="Exit", command=window.destroy, fg="black", bg="#13059c", width=35, height=1, activebackground = "white", font=('Helvetica', 20, ' bold '))
exitButton.place(x=30, y=450,relwidth=0.89)

# message
message = tkinter.Label(regFrame, text="" ,bg="#ADD8E6" ,fg="green"  ,width=39,height=1, activebackground = "yellow" ,font=('times', 16, ' bold '))
message.place(x=7, y=500)

window.mainloop()

