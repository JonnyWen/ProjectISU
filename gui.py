import tkinter
from tkinter import *
from tkinter import messagebox as mess
from tkinter import ttk
import cv2
import face_recognition
import os
import sys
import numpy as np
from attendance import AttendanceMgr, getAllAttendance, getAllStudents, removeAttendance
from registration import register, removeRegisteredStudent

#clearbutton
def clear():
    inputStudentNum.delete(0, 'end')
    inputStudentName.delete(0, 'end')

def registration():

    Id = (inputStudentNum.get())
    name = (inputStudentName.get())
    msg = register(Id,name)
    message.configure(text=msg)

def takeAttendance():
    att = AttendanceMgr()
    att.takeAttendance()

def showAttendance():
    print('show attendance')
    # clear table first
    for k in tb.get_children():
        tb.delete(k)
    # Display each row
    for att in getAllAttendance():
        tb.insert('', 'end', text=att.student_num, values=(att.name, att.date, att.time))

def showAbsence():
    print('Show absence')
    # collect id of all attendees
    attendee_ids = [att.student_num for att in getAllAttendance()]
    print(attendee_ids)
    for k in tb.get_children():
        tb.delete(k)
    for student in getAllStudents():
        if student.student_num not in attendee_ids:
            tb.insert('', 'end', text=student.student_num, values=(student.name, 'absense', 'absense'))

def clearAttendance():
    print('clear attendance')
    removeAttendance()

def clearRegistration():
    print('Clear Registration')
    # Remove all image files
    for root, dirs, files in os.walk('images'):
        for file in files:
            os.remove(os.path.join(root, file))
    removeRegisteredStudent()

#AskforQUIT
def on_closing():
    if mess.askyesno("Quit", "You are exiting window.Do you want to quit?"):
        window.destroy()

#contact
def contact():
    mess._show(title="Contact Me",message="If you need any help with this application contact me at 349358598@gapps.yrdsb.ca")

# Display application window
window = tkinter.Tk()
window.title(" Student Attendance System")
window.geometry("1280x720")
window.resizable(True,True)
window.configure(background='#051650')

# Title in Application Window
title = tkinter.Label(window, text="FaceAttendance",
                         fg="white", bg="#051650", width=60, height=1, font=('Inter', 30, ' normal '))
title.place(x=10, y=10, relwidth=1)

# Registration frame
regFrame = tkinter.Frame(window, bg='#ADD8E6')
regFrame.place(relx=0.05, rely=0.1, relwidth=0.40, relheight=0.80)

# header of Registration frame
regFrameHeader = tkinter.Label(regFrame, text="Register New Student", fg="#051650", bg="white", font=('Inter', 17, ' bold '))
regFrameHeader.place(x=0, y=0, relwidth=1)

# Label of student number
lbStudentNum = tkinter.Label(regFrame, text="Student Number", width=20, height=1, fg="black", bg="#ADD8E6", font=('Inter', 15, ' bold ') )
lbStudentNum.place(x=10, y=55)

# Input box of Student number
inputStudentNum = tkinter.Entry(regFrame,width=32 ,fg="black",bg="#e1f2f2",highlightcolor="#00aeff",highlightthickness=3,font=('Inter', 15, ' bold '))
inputStudentNum.place(x=45, y=88, relwidth=0.75)

# Label of student name
lbStudentName = tkinter.Label(regFrame, text="Student Name", width=20,fg="black",bg="#ADD8E6",font=('Inter', 15, ' bold '))
lbStudentName.place(x=0, y=140)

# Input box of student name
inputStudentName = tkinter.Entry(regFrame, width=32, fg="black", bg="#e1f2f2", highlightcolor="#00aeff", highlightthickness=3, font=('Inter', 15, ' bold ')  )
inputStudentName.place(x=45, y=173,relwidth=0.75)

# Clear buttons
clearButton = tkinter.Button(regFrame, text="Clear", command=clear, fg="black", bg="green", width=11, activebackground = "green", font=('Inter', 12, ' bold '))
clearButton.place(x=45, y=230, relwidth=0.29)

# Take Picture buttons
takePicButton = tkinter.Button(regFrame, text="Register", command=registration, fg="black", bg="#051650", width=34, height=1, activebackground="grey", font=('Inter', 16, ' bold '))
takePicButton.place(x=30, y=350, relwidth=0.50)

# Clear Registration buttons
clearRegistrationButton = tkinter.Button(regFrame, text="Clear all registration", command=clearRegistration, fg="black", bg="#051650", width=34, height=1, activebackground="grey", font=('Inter', 16, ' bold '))
clearRegistrationButton.place(x=30, y=400, relwidth=0.50)

### End of registratipon frame

# Attendance panel
attFrame = tkinter.Frame(window, bg="#ADD8E6")
attFrame.place(relx=0.56, rely=0.1, relwidth=0.40, relheight=0.80)

# header of Registration frame
attFrameHeader = tkinter.Label(attFrame, text="Mark Attendance", fg="#051650", bg="white", font=('Inter', 17, ' bold '))
attFrameHeader.place(x=0, y=0, relwidth=1)

# Taking attendance button
takeAttendanceButton = tkinter.Button(attFrame, text="Take Attendance", command=takeAttendance, fg="black", bg="#00aeff", height=1, activebackground = "white" ,font=('Inter', 16, ' bold '))
takeAttendanceButton.place(x=30,y=60,relwidth=0.40)

# Taking attendance button
takeAttendanceButton = tkinter.Button(attFrame, text="Clear Attendance", command=clearAttendance, fg="black", bg="#00aeff", height=1, activebackground = "white" ,font=('Inter', 16, ' bold '))
takeAttendanceButton.place(x=280,y=60,relwidth=0.40)

# Showing attendance button
showAttendanceButton = tkinter.Button(attFrame, text="Show Attendance", command=showAttendance, fg="black", bg="#00aeff", height=1, activebackground = "white" ,font=('Inter', 16, ' bold '))
showAttendanceButton.place(x=30,y=480,relwidth=0.40)

# Show absence button
showAbsenceButton = tkinter.Button(attFrame, text="Show Absence", command=showAbsence, fg="black", bg="#00aeff", height=1, activebackground = "white" ,font=('Inter', 16, ' bold '))
showAbsenceButton.place(x=280,y=480,relwidth=0.40)

# Exit button for exiting application
exitButton = tkinter.Button(attFrame, text="Exit", command=window.destroy, fg="black", bg="#13059c", width=35, height=1, activebackground = "white", font=('Inter', 20, ' bold '))
exitButton.place(x=30, y=520,relwidth=0.89)

# message
message = tkinter.Label(regFrame, text="" ,bg="#ADD8E6" ,fg="green" ,width=39,height=1, activebackground = "yellow" ,font=('Inter', 16, ' bold '))
message.place(x=7, y=500)

# Attendance table title
attendanceTitle = tkinter.Label(attFrame, text="Attendance Table",width=20,fg="#051650",bg="#ADD8E6",height=1,font=('Inter', 17, ' bold '))
attendanceTitle.place(x=140, y=115)

# attendance table
style = ttk.Style()
style.configure("mystyle.Treeview", highlightthickness=0, bd=0, font=('Inter', 15)) # Modify the font of the body
style.configure("mystyle.Treeview.Heading",font=('Inter', 13,'bold')) # Modify the font of the headings
style.layout("mystyle.Treeview", [('mystyle.Treeview.treearea', {'sticky': 'nswe'})]) # Remove the borders
tb = ttk.Treeview(attFrame, height =15,columns = ('name','date','time'),style="mystyle.Treeview")
tb.column('#0',width=82)
tb.column('name',width=130)
tb.column('date',width=133)
tb.column('time',width=133)
tb.grid(row=2,column=0,padx=(15,0),pady=(150,0),columnspan=4)
tb.heading('#0',text ='ID')
tb.heading('name',text ='Name')
tb.heading('date',text ='Date')
tb.heading('time',text ='Time')

# scroll bar
scroll=ttk.Scrollbar(attFrame,orient='vertical',command=tb.yview)
scroll.grid(row=2,column=4,padx=(0,100),pady=(150,0),sticky='ns')
tb.configure(yscrollcommand=scroll.set)

#Menubar
menubar=Menu(window)
help=Menu(menubar,tearoff=0)
help.add_command(label="Contact Us",command=contact)
help.add_separator()
help.add_command(label="Exit",command=on_closing)
menubar.add_cascade(label="Help",menu=help)

#Show Menubar on window
window.config(menu=menubar)

window.protocol("WM_DELETE_WINDOW", on_closing)
window.mainloop()

