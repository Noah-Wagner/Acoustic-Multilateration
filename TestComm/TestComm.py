import serial
import sys

def serial_ports():

    if sys.platform.startswith('win'):
        ports = ['COM%s' % (i + 1) for i in range(256)]
    else:
        raise EnvironmentError('Unsupported platform')

    result = []
    for port in ports:
        try:
            s = serial.Serial(port)
            result.append(s.name)
            s.close()
            # result.append(port)
        except (OSError, serial.SerialException):
            pass
    return result


if __name__ == '__main__':
    print("Available ports:")
    available_ports = serial_ports()
    print(available_ports)
    serial_selection = input("Select port (0 indexed): ")
    s = serial.Serial(available_ports[int(serial_selection)], 9600)
    print("Selected " + s.name)

    while True:
        try:
            print(s.read().decode("UTF-8"))
        except KeyboardInterrupt:
            break

    s.close()
