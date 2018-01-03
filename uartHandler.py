import serial
import time
BAUD_RATE = 9600

def open_port(port):
    try:
        ser = serial.Serial(port, baudrate=BAUD_RATE, parity=serial.PARITY_NONE,
                            stopbits=serial.STOPBITS_ONE, bytesize=serial.EIGHTBITS)
        time.sleep(2)
        return ser
    except serial.SerialException:
        return False


def sendSignal(ser):
    try:
        ser.write(b'g')
        ser.close()
    except serial.SerialException:
        return False
