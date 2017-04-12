import requests
import serial
import sys

times = [] * 5
count = [0]

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




def parser(message):
    count[0] += 1
    sensor_id = int(message[7])
    times[int(sensor_id)] = int(message[8:len(message)])

    if count[0] >= 5:
        url = "http://senior-design-project-155422.appspot.com/getsourceloc/?arrivaltimes="
        for i in range(0, 4):
            url += times[i]
            url += ", "
        url += times[4]
        requests.get(url)
    print("XD HERE XD")

if __name__ == '__main__':

    # parser("3 48791546546546841616165416165465465464651651616164164714871")

    print("Available ports:")
    available_ports = serial_ports()
    print(available_ports)
    serial_selection = input("Select port (0 indexed): ")
    s = serial.Serial(available_ports[int(serial_selection)], 9600)
    print("Selected " + s.name)

    while True:
        try:
            print(s.readline().decode("UTF-8"))
            parser(s.readLine().decode("UTF-8"))
        except KeyboardInterrupt:
            break

    s.close()
