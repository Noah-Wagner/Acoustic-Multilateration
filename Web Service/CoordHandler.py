

class CoordHandler:
    coords = None

    @staticmethod
    def update_loc(x, y):
        CoordHandler.coords = (x, y)
        return 'true'

    @staticmethod
    def get_loc():
        return CoordHandler.coords

