import cv2
import face_recognition
from db import insertStudent, Student, deleteAllStudents


def register(Id, name):

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
                # Add student record to database
                student = Student(student_num = Id, name = name, imageName = img_name)
                insertStudent(student)
                break

            if cv2.waitKey(1) == ord('q'):
                break

        cam.release()
        cv2.destroyAllWindows()
        message = name + ' registered successfully.'
       # message.configure(text=res)
        return message
    else:
        if not name.isalpha():
            message = "Enter Correct name"
           # message.configure(text=res)
            return message

def removeRegisteredStudent():
    deleteAllStudents()