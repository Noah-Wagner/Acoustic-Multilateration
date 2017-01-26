class Coord:
    x = None
    y = None

    def __init__(self, x, y):
        self.x = x
        self.y = y


class CoordHandler:
    coords = None
    abs_coords = None

    @staticmethod
    def update_loc(x, y):
        if x is None or y is None:
            return 'false'
        CoordHandler.coords = Coord(x, y)
        return 'true'

    @staticmethod
    def update_abs_loc(x, y):
        CoordHandler.abs_coords = Coord(x, y)

    @staticmethod
    def get_loc():
        return CoordHandler.merge_coords()

    @staticmethod
    def merge_coords():
        if CoordHandler.coords is None or CoordHandler.abs_coords is None:
            return None
        return CoordHandler.add_coords(CoordHandler.coords, CoordHandler.abs_coords)

    @staticmethod
    def add_coords(coords, absCoords):
        return (coords.x + absCoords.x,
                coords.y + absCoords.y)
