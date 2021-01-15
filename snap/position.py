class Position:
    def __init__(self, x, y):
        self._x = x
        self._y = y

    def x(self):
        return self._x

    def y(self):
        return self._y

    def add(self, pos):
        self._x += pos.x()
        self._y += pos.y()
        return self

    def times(self, k):
        self._x *= k
        self._y *= k
        return self

    def mod(self, pos):
        self._x %= pos.x()
        self._y %= pos.y()
        return self

    def clone(self):
        return Position(self._x, self._y)

    def __eq__(self, other):
        return (self._x == other._x) and (self._y == other._y)
