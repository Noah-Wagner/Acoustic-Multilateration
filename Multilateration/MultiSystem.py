import numpy


class MultiSystem:
    DIMENSION = 3
    SOUND_SPEED = 340.29
    _cached_result = None
    _sensor_coords = []
    _arrival_times = []

    def __init__(self, tup):
        self._sensor_coords = tup
        self._arrival_times = [None] * len(tup)

    def add_times(self, times):
        if len(times) < MultiSystem.DIMENSION + 2:
            raise ValueError("Not enough arrival times")

        self._cached_result = None
        self._arrival_times = times
        # TODO: Probably should have some validation here lol

    def get_sensor_loc(self):
        return self._sensor_coords

    # Memoization :D
    def get_source_pos(self):
        if self._cached_result is not None:
            return self._cached_result
        return self._perform_multilateration()

    def _perform_multilateration(self):
        return self._perform_multilateration_linear()

    def _perform_multilateration_linear(self):

        if len(self._sensor_coords) < 5:
            raise ValueError("Not enough sensors")
        if len(self._arrival_times) < 5:
            raise ValueError()

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
        self._cached_result = numpy.linalg.lstsq(a, b)
        return self._cached_result
