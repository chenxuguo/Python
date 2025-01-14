import cached_property

class Location:
    def __init__(self, x=0, y=0):
        self.x = x
        self.y = y
        self._loc = [self.x, self.y]

    cached_property
    def loc(self):
        print("computing...")
        return [self.x, self.y]

    def move_left(self):
        self.x -= 1

    def move_right(self):
        self.x += 1

    def move_up(self):
        self.y -= 1

    def move_down(self):
        self.y += 1


    def __repr__(self):
        return f'{type(self).__name__}(x={self.x}, y={self.y})'


socket(AF_Net, )