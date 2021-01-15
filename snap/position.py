class Position:
    def __init__(self, x, y):
        self._x = x
        self._y = y

    def x(self):
        return self._x

    def y(self):
        return self._y

    def add(self, v):
        self._x += v[0]
        self._y += v[1]
        return self

    def mod(self, v):
        self._x %= v[0]
        self._y %= v[1]
        return self

    def clone(self):
        return Position(self._x, self._y)

    def __eq__(self, other):
        return (self._x == other._x) and (self._y == other._y)
