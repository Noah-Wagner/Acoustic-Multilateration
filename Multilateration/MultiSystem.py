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
        return self.__perform_multilateration_linear()

    def __perform_multilateration_linear(self):

        temp_time = self._arrival_times[0]
        for i in range(0, len(self._sensor_coords)):
            self._arrival_times[i] -= temp_time

        b = []
        a = []

        A = [0] * (len(self._arrival_times) - 2)
        B = [0] * (len(self._arrival_times) - 2)
        C = [0] * (len(self._arrival_times) - 2)
        D = [0] * (len(self._arrival_times) - 2)

        t_1 = self.SOUND_SPEED * (self._arrival_times[1] - self._arrival_times[0])
        for i in range(2, len(self._arrival_times)):
            t_m = self.SOUND_SPEED * (self._arrival_times[i] - self._arrival_times[0])
            if (t_m == 0):
                raise Exception("Move sensors")

            A[i - 2] = 2 * ((self._sensor_coords[i][0] / t_m) - (self._sensor_coords[1][0] / t_1))

            B[i - 2] = 2 * ((self._sensor_coords[i][1] / t_m) - (self._sensor_coords[1][1] / t_1))

            C[i - 2] = 2 * ((self._sensor_coords[i][2] / t_m) - (self._sensor_coords[1][2] / t_1))

            D[i - 2] = t_m - t_1 - \
                       ((self._sensor_coords[i][0] ** 2 + self._sensor_coords[i][1] ** 2 + self._sensor_coords[i][
                           2] ** 2) / t_m) + \
                       ((self._sensor_coords[1][0] ** 2 + self._sensor_coords[1][1] ** 2 + self._sensor_coords[1][
                           2] ** 2) / t_1)

            a.append([A[i - 2], B[i - 2], C[i - 2]])
            b.append(-D[i - 2])
        x = numpy.linalg.lstsq(a, b)
        return x
