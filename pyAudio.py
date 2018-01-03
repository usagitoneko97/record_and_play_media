import pyaudio
from array import array
import videoPlaying
import uartHandler

CHUNK = 1024
FORMAT = pyaudio.paInt16
CHANNELS = 2
RATE = 44100
RECORD_SECONDS = 10



def open_stream():
    p = pyaudio.PyAudio()

    stream = p.open(format=FORMAT,
                    channels=CHANNELS,
                    rate=RATE,
                    input=True,
                    frames_per_buffer=CHUNK)

    return stream, p

def detect_threshold(threshold, stream):
    """
    this func will check the ambient volume level
    :param threshold: the maximum amplitude of stream read can go
    :return:
        True : threshold had reached
        False: threshold had not reached
    """

    average = 0

    # for _ in range(3):
    #     data = stream.read(CHUNK)
    #     snd_data = array('h', data)
    #     average += snd_data[0]
    #
    # average = average / 3
    # print("average :{}".format(average))

    data = stream.read(CHUNK)
    snd_data = array('h', data)

    if snd_data[0] > threshold:
        return True
    return False

def close_stream(stream, p):
    stream.stop_stream()
    stream.close()
    p.terminate()


def detect_threshold_blocking(threshold):
    """
    this func will check the ambient volume level in blocking mode
    :param threshold: the maximum amplitude of stream read can go
    :return:
        True : threshold had reached
        False: threshold had not reached
    """
    stream, p = open_stream()
    while 1:
        data = stream.read(CHUNK)
        snd_data = array('h', data)
        if snd_data[0] > threshold:
            break

    close_stream(stream, p)