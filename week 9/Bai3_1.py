import math


class Point:
    def __init__(self, x=0, y=1):
        self.__x = x
        self.__y = y

    def read(self):
        self.__x, self.__y = map(int, input().split())

    def print(self):
        print(f"({self.__x}, {self.__y})")

    def move(self, dx, dy):
        self.__x += dx
        self.__y += dy

    def getX(self):
        return self.__x

    def getY(self):
        return self.__y

    def distance(self, P=None):

        if P is None:
            return math.sqrt(self.__x**2 + self.__y**2)

        return math.sqrt(
            (self.__x - P.getX())**2 +
            (self.__y - P.getY())**2
        )

    def __str__(self):
        return f"({self.__x}, {self.__y})"


class ColorPoint(Point):

    def __init__(self, *args):
        if len(args) == 0:
            super().__init__()
            self.__color = "xanh"
        elif len(args) == 3:
            super().__init__(args[0], args[1])
            self.__color = args[2]
        elif len(args) == 1 and isinstance(args[0], ColorPoint):
            cp = args[0]
            super().__init__(cp.getX(), cp.getY())
            self.__color = cp.__color

    def read(self):
        super().read()
        self.__color = input()

    def print(self):
        print(f"({self.getX()}, {self.getY()}): {self.__color}")

    def setColor(self, color):
        self.__color = color

    def __str__(self):
        return f"({self.getX()}, {self.getY()}): {self.__color}"
