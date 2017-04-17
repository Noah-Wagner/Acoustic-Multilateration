import requests
import serial
import sys

# times = [] * 5
times = [-1, -1, -1, -1, -1]
time_out_flag = True
# count = [0]

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

    sensor_id = int(message[6]) - 1

    if times[sensor_id] == -1:
        times[sensor_id] = float(message[7:len(message)])*10**(-6)

    print("Sensor " + str(sensor_id + 1) + ": " + str(times[sensor_id]))

    count = 0
    for thing in times:
        if thing > -1:
            count += 1

    if count >= 5:
        url = "http://senior-design-project-155422.appspot.com/getsourceloc/?arrivaltimes="
        for i in range(0, 4):
            url += str(times[i])
            url += ", "
        url += str(times[4])
        print(url)
        x= requests.get(url)
        print(x.content)


if __name__ == '__main__':

    # parser("Node: 1 547991e-6")
    # parser("Node: 2 554019e-6")
    # parser("Node: 3 556358e-6")
    # parser("Node: 4 563371e-6")
    # parser("Node: 5 569160e-6")

    print("Available ports:")
    available_ports = serial_ports()
    print(available_ports)
    serial_selection = input("Select port (0 indexed): ")
    s = serial.Serial(available_ports[int(serial_selection)], 9600)
    print("Selected " + s.name)

    while True:
        try:
            stringlol = s.readline().decode("UTF-8")

            if stringlol[0] != "H":
                print(stringlol)
                stringlol = stringlol[0:len(stringlol) - len("\r\n")]
                # print(stringlol)

                parser(stringlol)
        except KeyboardInterrupt:
            break

    s.close()