import serial
BAUD_RATE = 115200
TIMEOUT = 1

def sendSignal(port):
    try:
        ser = serial.Serial(port, BAUD_RATE, timeout=TIMEOUT)
        ser.write(b'g')
        ser.close()
    except serial.SerialException:
        return False
