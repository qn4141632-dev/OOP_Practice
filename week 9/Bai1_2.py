import math
class Point:
    def __init__(self,x=0,y=0):
        self.__x = x
        self.__y = y
    def read(self):
        x,y = map(int,input("Nhập tọa độ (x,y):").split())
        self .__x=x
        self.__y=y
    def print(self):
        print(f"({self.__x},{self.__y})")
    def move(self,dx,dy):
        self.__x+= dx
        self.__y+= dy
    def getX(self):
        return self .__x
    def getY(self):
        return self .__y
    def distance(self, other =None):
        if other is None:
            return math.sqrt(self.__x**2 + self.__y**2)
        return math.sqrt((self.__x - other.getX())**2 +(self.__y - other.getY())**2)

