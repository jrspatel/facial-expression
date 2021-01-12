# opens the webcam and reads the images.

import cv2
from deepface import DeepFace
face_cascade = cv2.CascadeClassifier("haarcascade_frontalface_default.xml")

class VideoCamera(object):
    def __init__(self):
        # starting the webcam
        self.video = cv2.VideoCapture(0)

    def __del__(self):
        # closing the webcam
        self.video.release()

    def get_frame(self):
        # all our prediction -- detecting images and expression
        ret , frame = self.video.read()
        result = DeepFace.analyze(frame, actions=['emotion'])
        gray = cv2.cvtColor(frame,cv2.COLOR_BGR2GRAY)
        font = cv2.FONT_HERSHEY_SIMPLEX
        faces = face_cascade.detectMultiScale(gray,1.3,5)
        for (x,y,w,h) in faces:
            cv2.rectangle(frame,(x,y),(x+w,y+h),(0,0,255),3)
        cv2.putText(frame, result['dominant_emotion'], (50, 50), font, 3, (0, 0, 255), 2)
        ret , jpeg = cv2.imencode('.jpg',frame)

        return jpeg.tobytes()

