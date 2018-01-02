import pyaudio
from array import array
import videoPlaying
import uartHandler

CHUNK = 1024
FORMAT = pyaudio.paInt16
CHANNELS = 2
RATE = 44100
RECORD_SECONDS = 10

def detect_threshold(threshold):
    """
    this func will keep record surrounding voice until it hit the threeshold on blocking mode
    :param threshold: the maximum amplitude of stream read can go
    :return:
    """
    p = pyaudio.PyAudio()

    stream = p.open(format=FORMAT,
                    channels=CHANNELS,
                    rate=RATE,
                    input=True,
                    frames_per_buffer=CHUNK)

    print("* recording")

    while 1:
        data = stream.read(CHUNK)
        snd_data = array('h', data)
        if snd_data[0] > threshold:
            break
    stream.stop_stream()
    stream.close()
    p.terminate()
    return

flag = False
if __name__ == '__main__':
    threshold = input("enter the recording threshold\n")
    port = input("enter the port\n")
    flag = uartHandler.sendSignal(port)
    while flag is False:
        port = input("can't open {}, please try again\n".format(port))
        flag = uartHandler.sendSignal(port)
    print("Sent signals to arduino\n")

    file_name = input("enter the file name to play\n")
    detect_threshold(threshold=int(threshold))
    print("maximum amount of threshold {} reached, {} will be played".format(threshold, file_name))
    videoPlaying.play_video(file_name=file_name)