import numpy


class MultiSystem:
    SOUND_SPEED = 340.29
    _sensor_coords = []
    _arrival_times = []

    def __init__(self, tup):
        self._sensor_coords = tup
        self._arrival_times = [None] * len(tup)

    def addTime(self, time, sensor_id):
        self._arrival_times[sensor_id] = time

    def perform_multilateration(self):
        self.__perform_multilateration_linear()

    def __perform_multilateration_linear(self):

        # # Rescaling
        # dist = [0] * len(self._sensor_coords)
        # dist[0] = (self._sensor_coords[0][0] ** 2 + self._sensor_coords[0][1] ** 2
        #                                       + self._sensor_coords[0][2] ** 2) ** 0.5
        # for i in range(1, len(self._sensor_coords)):
        #     dist[i] = ((self._sensor_coords[i][0] - self._sensor_coords[0][0]) ** 2
        #                + (self._sensor_coords[i][1] - self._sensor_coords[0][1]) ** 2
        #                + (self._sensor_coords[i][2] - self._sensor_coords[0][2]) ** 2) ** 0.5
        # # Rescaling

        temp_time = self._arrival_times[0]
        for i in range(0, len(self._sensor_coords)):
            self._arrival_times[i] -= temp_time


        b = []
        # b = [0] * (len(self._arrival_times) - 2)
        a = []

        A = [0] * (len(self._arrival_times) - 2)
        B = [0] * (len(self._arrival_times) - 2)
        C = [0] * (len(self._arrival_times) - 2)
        D = [0] * (len(self._arrival_times) - 2)

        t_1 = self.SOUND_SPEED * (self._arrival_times[1] - self._arrival_times[0])
        for i in range(2, len(self._arrival_times)):
            t_m = self.SOUND_SPEED * (self._arrival_times[i] - self._arrival_times[0])

            A[i - 2] = 2*((self._sensor_coords[i][0] / t_m) - (self._sensor_coords[1][0] / t_1))

            B[i - 2] = 2*((self._sensor_coords[i][1] / t_m) - (self._sensor_coords[1][1] / t_1))

            C[i - 2] = 2*((self._sensor_coords[i][2] / t_m) - (self._sensor_coords[1][2] / t_1))

            D[i - 2] = t_m - t_1 - \
                ((self._sensor_coords[i][0] ** 2 + self._sensor_coords[i][1] ** 2 + self._sensor_coords[i][2] ** 2) / t_m) + \
                ((self._sensor_coords[1][0] ** 2 + self._sensor_coords[1][1] ** 2 + self._sensor_coords[1][2] ** 2) / t_1)

            a.append([A[i-2], B[i-2], C[i-2]])
            b.append(-D[i-2])
        # a = numpy.array(a)
        # print (a)
        # print(b)
        # x = numpy.linalg.solve(a,b)
        x = numpy.linalg.lstsq(a, b)
        print(x)


        #
        # class ArrivalCoord:
        #


def perform_test():
    b = [0, 4, -3]
    a = []
    a.append([1, 1, 1])
    a.append([2, 1, -1])
    a.append([-1.5, -1, 1])
    # a = ((1, 1, 1), (2, 1, -1), (-1.5, -1, 1))
    x = numpy.linalg.lstsq(a, b)
    # print(x)
    #
    # b =(-6, 8)
    # a = ((1, -1), (1, 1))
    # print numpy.linalg.lstsq(a, b)
    #
    #


    source = (1, 2, 6)
    places = []
    places.append((0, 0, 0))
    places.append((-2.1, 3.1, 10.0))
    places.append(( -1, -3.1, 4.5))
    places.append((3, -5, -6))
    places.append((5, 3, 2))
    numpy.transpose(places)
    # places = ((2.0, 3.0, 0.0), (-2.1, 3.1, 0.0), (-1, -3.1, 0.0), (3, -5, 0), (2, 3, 2))
    multiSystem1 = MultiSystem(places)
    i = 0
    for thing in places:
        multiSystem1.addTime((((thing[0] - source[0]) ** 2 + (thing[1] - source[1]) ** 2 + (thing[2] - source[2]) ** 2) ** 0.5) / 340.29, i)
        i += 1

    multiSystem1.perform_multilateration()

    multiSystem = MultiSystem(((2.0, 3.0, 0.0), (-2.1, 3.1, 0.0), (-1, -3.1, 0.0), (3, -5, 0), (2, 3, 2)))
    multiSystem.addTime(0.0072, 0)
    multiSystem.addTime(0.0114, 1)
    multiSystem.addTime(0.0137, 2)
    multiSystem.addTime(0.0188, 3)
    multiSystem.addTime(0.0088, 4)

    # multiSystem.perform_multilateration()

# Main

perform_test()

# End main
