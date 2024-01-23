import face_recognition
import cv2
import sys
import numpy as np
from db import getAllStudents, Attendance, insertAttendance, queryAllAttendance, deleteAllAttendance
from datetime import datetime

class AttendanceMgr:
    face_locations = []
    face_encodings = []
    face_names = []
    known_face_encodings = []
    known_face_names = []
    known_face_ids = []
    process_current_frame = True

    def __init__(self):
        self.encode_face()

    # Load student data from database and process image files
    def encode_face(self):
        for student in getAllStudents():
            face_image = face_recognition.load_image_file(f'images/{student.imageName}')
            face_encoding = face_recognition.face_encodings(face_image)[0]

            self.known_face_encodings.append(face_encoding)
            self.known_face_names.append(student.name)
            self.known_face_ids.append(student.student_num)

    def takeAttendance(self):
        # Capture video images
        video_capture = cv2.VideoCapture(0)

        if not video_capture.isOpened():
            sys.exit('Could not open video stream or file')

        while True:
            # Capturing frame
            ret, frame = video_capture.read()

            if self.process_current_frame:
                # reduce the size of frame to make the processing faster
                small_frame = cv2.resize(frame, (0, 0), fx=0.25, fy=0.25)
                # Converts frame to RGB colors
                rgb_small_frame = cv2.cvtColor(small_frame, cv2.COLOR_BGR2RGB)

                # find all faces in the current frame
                self.face_locations = face_recognition.face_locations(rgb_small_frame)
                # Encodes all faces
                self.face_encodings = face_recognition.face_encodings(rgb_small_frame, self.face_locations)

                self.face_names = []
                for face_encoding in self.face_encodings:
                    matches = face_recognition.compare_faces(self.known_face_encodings, face_encoding)
                    name = 'Unknown'

                    # Calculates distance of know faces from current face encoding on camera
                    face_distances = face_recognition.face_distance(self.known_face_encodings, face_encoding)

                    # Find the best match using the closest distance
                    if len(face_distances) > 0:
                        best_match_index = np.argmin(face_distances)

                    # Saving match to attendance table (present student)
                    if len(face_distances) > 0 and matches[best_match_index]:
                        name = self.known_face_names[best_match_index]
                        id = self.known_face_ids[best_match_index]

                        # Save the student to attendance if the face is recognized successfully
                        if name != 'Unknown':
                            self.markAttendance(id, name)

                    self.face_names.append(f'{name}')

            self.process_current_frame = not self.process_current_frame

            # Display names around the faces
            for (top, right, bottom, left), name in zip(self.face_locations, self.face_names):
                top *= 4
                right *= 4
                bottom *= 4
                left *= 4

                cv2.rectangle(frame, (left, top), (right, bottom), (0, 0, 255))
                cv2.rectangle(frame, (left, bottom - 35), (right, bottom), (0, 0, 255), -1)
                cv2.putText(frame, name, (left + 6, bottom - 6), cv2.FONT_HERSHEY_DUPLEX, 0.8, (255, 255, 255), 1)

            cv2.imshow('Taking attendance... press q when it is done', frame)

            if cv2.waitKey(1) == ord('q'):
                break

        video_capture.release()
        cv2.destroyAllWindows()

    def markAttendance(self, id, name):
        print(f'adding new attendance for {id}, {name}')
        tString = datetime.now().strftime('%H:%M:%S')
        dString = datetime.now().strftime('%d/%m/%Y')
        attendance = Attendance(student_num=id, name=name, date=dString, time=tString)
        insertAttendance(attendance)

def getAllAttendance():
    return queryAllAttendance()

def removeAttendance():
    deleteAllAttendance()

