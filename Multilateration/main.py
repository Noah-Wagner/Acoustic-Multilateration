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
        b = numpy.array([0] * (len(self._arrival_times) - 2))
        a = []

        for i in range(2, len(self._arrival_times)):
            A = ((2 * self._sensor_coords[i][0])/(self.SOUND_SPEED * (self._arrival_times[i] - self._arrival_times[0]))) - \
                ((2 * self._sensor_coords[1][0]) / (self.SOUND_SPEED * (self._arrival_times[1] - self._arrival_times[0])))

            B = ((2 * self._sensor_coords[i][1]) / (self.SOUND_SPEED * (self._arrival_times[i] - self._arrival_times[0]))) - \
                ((2 * self._sensor_coords[1][1]) / (self.SOUND_SPEED * (self._arrival_times[1] - self._arrival_times[0])))

            C = ((2 * self._sensor_coords[i][2]) / (self.SOUND_SPEED * (self._arrival_times[i] - self._arrival_times[0]))) - \
                ((2 * self._sensor_coords[1][2]) / (self.SOUND_SPEED * (self._arrival_times[1] - self._arrival_times[0])))

            D = self.SOUND_SPEED*(self._arrival_times[i] - self._arrival_times[1]) - \
                (self._sensor_coords[i][0]**2 + self._sensor_coords[i][1]**2 + self._sensor_coords[i][2]**2)/(self.SOUND_SPEED * (self._arrival_times[i] - self._arrival_times[0])) + \
                (self._sensor_coords[1][0] ** 2 + self._sensor_coords[1][1] ** 2 + self._sensor_coords[1][2] ** 2)/(self.SOUND_SPEED * (self._arrival_times[1] - self._arrival_times[0]))
            a.append(numpy.array([A, B, C, D]))



        x = numpy.linalg.solve(a, b)
        print(x)
    #
    # class ArrivalCoord:
    #

multiSystem = MultiSystem([(2.0, 3.0, 0.0), (-2.1, 3.1, 0.0), (-1, -3.1, 0.0), (3, -5, 0)])
multiSystem.addTime(0.0106, 0)
multiSystem.addTime(0.0110, 1)
multiSystem.addTime(0.0096, 2)
multiSystem.addTime(0.0171, 3)

multiSystem.perform_multilateration()
