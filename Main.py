import cv2
import sys
def run_recognition():
    video_capture = cv2.VideoCapture(0)

    if not video_capture.isOpened():
        sys.exit('Cannot open video stream or file')

    while True:
        ret, frame = video_capture.read()

        rgb_frame = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)

        cv2.imshow('Face Recognition', frame)

        if cv2.waitKey(1) == ord('q'):
            break

    video_capture.release()
    cv2.destroyAllWindows()

run_recognition()
