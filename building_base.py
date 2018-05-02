from itertools import product

class Building:
    def __init__(self, south, west, width_WE, width_NS, height=10):
        self.south = south
        self.west = west
        self.north = south + width_NS
        self.east = west + width_WE
        self.width_x = width_WE
        self.width_y = width_NS
        self.height = height

    def corners(self):
        corners_ = product({'south', 'north'}, {'west', 'east'})
        return {'-'.join(c): [getattr(self, v) for v in c] for c in corners_}

    def area(self):
        return self.width_x * self.width_y

    def volume(self):
        return self.area() * self.height

    def __repr__(self):
        return ('Building({0.south}, {0.west}, {0.width_x}, '
                         '{0.width_y}, {0.height})'.format(self))

