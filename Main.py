import cv2
import sys
import face_recognition
def run_recognition():
    video_capture = cv2.VideoCapture(0)

    if not video_capture.isOpened():
        sys.exit('Cannot open video stream or file')

    while True:
        ret, frame = video_capture.read()
        small_frame = cv2.resize(frame, (0, 0), fx=0.25, fy=0.25)

        rgb_small_frame = cv2.cvtColor(small_frame, cv2.COLOR_BGR2RGB)

        face_locations = []

        face_locations = face_recognition.face_locations(rgb_small_frame)

        for (top, right, bottom, left) in face_locations:
            top *= 4
            right *= 4
            bottom *= 4
            left *= 4
            cv2.rectangle(frame, (left, top), (right, bottom), (0, 255, 0))

        cv2.imshow('Face Recognition', frame)

        if cv2.waitKey(1) == ord('q'):
            break

    video_capture.release()
    cv2.destroyAllWindows()

run_recognition()
