
from MultiSystem import MultiSystem

class Coord:
    x = None
    y = None
    z = None

    def __init__(self, x, y, z):
        self.x = x
        self.y = y
        self.z = z

# TODO: Implement tests
# TODO: Refactor error cases into exceptions, should not be passing null

class CoordHandler:
    _abs_coords = None
    _multi_system = None

    @staticmethod
    def update_loc(sensor_loc):
        if sensor_loc is None:
            return 'false'
        CoordHandler._multi_system = MultiSystem(sensor_loc)
        return 'true'

    @staticmethod
    def update_abs_loc(x, y, z):
        if x is None or y is None or z is None:
            return 'false'
        CoordHandler._abs_coords = Coord(x, y, z)
        return 'true'

    @staticmethod
    def get_loc(arrival_times):
        if CoordHandler._multi_system is None:
            raise ValueError("Sensor locations required")
        if arrival_times is not None:
            arrival_times = arrival_times.split(', ')
            arrival_times = list(map(lambda x:float(x), arrival_times))
            MultiSystem.add_times(CoordHandler._multi_system, arrival_times)

        return MultiSystem.get_source_pos(CoordHandler._multi_system)
        # return CoordHandler.merge_coords()

    @staticmethod
    def merge_coords():
        if CoordHandler._coords is None or CoordHandler._abs_coords is None:
            return None
        return CoordHandler._add_coords(CoordHandler._coords, CoordHandler._abs_coords)

    @staticmethod
    def _add_coords(coords, absCoords):
        return (coords.x + absCoords.x,
                coords.y + absCoords.y,
                coords.z + absCoords.z)

    @staticmethod
    def get_sensor_loc():
        if CoordHandler._multi_system is None:
            return None
        return MultiSystem.get_sensor_loc(CoordHandler._multi_system)

    @staticmethod
    def get_abs_loc():
        if CoordHandler._abs_coords is None:
            return None
        return CoordHandler._abs_coords.x, CoordHandler._abs_coords.y, CoordHandler._abs_coords.z

    @staticmethod
    def multilateration(arrival_times):
        if arrival_times is None:
            raise ValueError("Arrival times required")
        if CoordHandler._multi_system is None:
            raise ValueError("Sensor locations required")

        return MultiSystem._perform_multilateration(CoordHandler._multi_system)