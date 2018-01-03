import uartHandler
import pyAudio
import videoPlaying

flag = False
flagAudio = False
if __name__ == '__main__':
    threshold = input("enter the recording threshold\n")
    # port = input("enter the port\n")
    # flag = uartHandler.open_port(port)
    # while flag is False:
    #     port = input("can't open {}, please try again\n".format(port))
    #     flag = uartHandler.sendSignal(port)

    file_name = input("enter the file name to play\n")
    # waiting for the first time blowing
    stream, p = pyAudio.open_stream()
    flagAudio = pyAudio.detect_threshold(stream=stream, threshold=int(threshold))
    while flagAudio is False:
        flagAudio = pyAudio.detect_threshold(stream=stream, threshold=int(threshold))

    print("maximum amount of threshold {} reached, {} will be played".format(threshold, file_name))
    videoPlaying.play_frame(file_name=file_name, threshold=int(threshold), stream=stream, p=p)