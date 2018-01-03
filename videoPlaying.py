import cv2
import pyAudio
import threading



flag = 0
NO_OF_RETRIES = 4
retries_num = 0
timerFlag = 0

def play_frame(file_name, threshold, stream, p):
    global timerFlag
    retries_num = 0
    global timerFlag
    cap = cv2.VideoCapture(file_name)
    timer = threading.Timer(0.2, threshold_frame, args=(threshold, stream))
    timer.start()
    while cap.isOpened():
        ret, frame = cap.read()

        cv2.imshow('frame', frame)
        if cv2.waitKey(25) & 0xFF == ord('q'):
            break

        if flag == 1:
            break
        if timerFlag == 1:
            timerFlag = 0
            timer = threading.Timer(0.2, threshold_frame, args=(threshold, stream))
            timer.start()

    timer.cancel()
    pyAudio.close_stream(stream, p)
    cap.release()
    cv2.destroyAllWindows()

def threshold_frame(threshold, stream):
    global flag
    global retries_num
    global timerFlag
    timerFlag = 1
    if (pyAudio.detect_threshold(threshold, stream) == False):
        retries_num = retries_num + 1
    else:
        # reset the retires_num
        retries_num = 0

    if retries_num > 6:
        flag = 1