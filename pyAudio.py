import pyaudio
import sys
from array import array
import serial
import videoPlaying

CHUNK = 1024
FORMAT = pyaudio.paInt16
CHANNELS = 2
RATE = 44100
RECORD_SECONDS = 10
WAVE_OUTPUT_FILENAME = "output.wav"

def detect_threeshold(threeshold):
    """
    this func will keep record surrounding voice until it hit the threeshold on blocking mode
    :param threeshold: the maximum amplitude of stream read can go
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
        if snd_data[0] > threeshold:
            break
    stream.stop_stream()
    stream.close()
    p.terminate()
    return


if __name__ == '__main__':
    threeshold = input("enter the recording threeshold\n")
    file_name = input("enter the file name to play\n")
    detect_threeshold(threeshold=int(threeshold))
    print("maximum amount of threeshold %s reached, program will now exit" % threeshold)
    videoPlaying.play_video(file_name=file_name)