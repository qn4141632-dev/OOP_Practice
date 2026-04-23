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
    def distance(self,P=None):
        if P is None:
            return math.sqrt(self.__x**2+self.__y**2)
        else:
            dx = self.__x - P.__x
            dy = self.__y - P.__y
            return math.sqrt(dx**2 +dy**2)
if __name__ == "__main__":
    print("=== Kiem thu lop Point ===")


    p0 = Point()
    print("Diem p0:",end="")
    p0.print()


    p2 = Point(3,4)
    print("Diem p2:",end="")
    p2.print()


    print("Nhap toa do cho p0:")
    p0.read()
    print("Sau khi nhap,p0=",end="")
    p0.print()


    p0.move(2,-1)
    print("Sau khi di chuyen p0:",end="")
    p0.print()


    print("Hoanh do p0:",p0.getX())
    print("Tung do p0:",p0.getY())


    print("Khoang cach p2 den goc:",p2.distance())


    print("Khoang cach p0 den p2:",p0.distance(p2))


