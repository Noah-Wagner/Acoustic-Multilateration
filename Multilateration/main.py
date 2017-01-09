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
        self.perform_multilateration_linear()


    def perform_multilateration_linear(self):
        b = [0] * (len(self._arrival_times) - 2)
        a = []

        t_1 = self.SOUND_SPEED * (self._arrival_times[1] - self._arrival_times[0])
        for i in range(2, len(self._arrival_times)):
            t_m = self.SOUND_SPEED * (self._arrival_times[i] - self._arrival_times[0])

            A = ((2 * self._sensor_coords[i][0]) / t_m) - ((2 * self._sensor_coords[1][0]) / t_1)

            B = ((2 * self._sensor_coords[i][1]) / t_m) - ((2 * self._sensor_coords[1][1]) / t_1)

            C = ((2 * self._sensor_coords[i][2]) / t_m) - ((2 * self._sensor_coords[1][2]) / t_1)

            D = t_m - t_1 - \
                ((self._sensor_coords[i][0] ** 2 + self._sensor_coords[i][1] ** 2 + self._sensor_coords[i][2] ** 2)/(t_m)) + \
                ((self._sensor_coords[1][0] ** 2 + self._sensor_coords[1][1] ** 2 + self._sensor_coords[1][2] ** 2)/(t_1))
            a.append([A, B, C, D])
        # a = numpy.array(a)
        x = numpy.linalg.lstsq(a, b)
        print(x)


    #
    # class ArrivalCoord:
    #


def perform_test():
    multiSystem = MultiSystem([(2.0, 3.0, 0.0), (-2.1, 3.1, 0.0), (-1, -3.1, 0.0), (3, -5, 0), (2, 3, 2)])
    multiSystem.addTime(0.0072, 0)
    multiSystem.addTime(0.0114, 1)
    multiSystem.addTime(0.0137, 2)
    multiSystem.addTime(0.0188, 3)
    multiSystem.addTime(0.0088, 4)

    multiSystem.perform_multilateration()


# Main

perform_test()

# End main

