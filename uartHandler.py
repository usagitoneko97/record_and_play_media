import serial
import time
BAUD_RATE = 9600

def open_port(port):
    try:
        ser = serial.Serial(port, baudrate=BAUD_RATE, parity=serial.PARITY_NONE,
                            stopbits=serial.STOPBITS_ONE, bytesize=serial.EIGHTBITS)
        time.sleep(2)
        return True, ser
    except serial.SerialException:
        return False


def sendSignalStart(ser):
    try:
        ser.write(b'g')

    except serial.SerialException:
        return False

def sendSignalStop(ser):
    try:
        ser.write(b's')
    except serial.SerialException:
        return False
