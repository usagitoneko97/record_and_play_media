import numpy as np
from cv2 import VideoCapture
from cv2 import cvtColor
from cv2 import imshow
from cv2 import waitKey
from cv2 import destroyAllWindows
# import cv2


def play_video(file_name):

    cap = VideoCapture(file_name)

    while cap.isOpened():
        ret, frame = cap.read()

        if ret == True:
            imshow('frame',frame)
            if waitKey(1) & 0xFF == ord('q'):
                break
        else:
            break

    cap.release()
    destroyAllWindows()
