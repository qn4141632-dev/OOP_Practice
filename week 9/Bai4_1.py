import math
import sys 

class TuLanh:
    def __init__(self, nhanhieu="Elextrolux", maso="UNKNOWN", nuocsx="Việt Nam", 
                 tkdien=True, dungtich=256, gia=7000000):
        self.__nhanhieu = nhanhieu
        self.__maso = maso
        self.__nuocsx = nuocsx
        self.__tkdien = tkdien
        self.__dungtich = dungtich
        self.__gia = gia

    def makeCopy(self, tl):
        self.__nhanhieu = tl.__nhanhieu
        self.__maso = tl.__maso
        self.__nuocsx = tl.__nuocsx
        self.__tkdien = tl.__tkdien
        self.__dungtich = tl.__dungtich
        self.__gia = tl.__gia

    def nhapThongTin(self):
        # Đọc dữ liệu từ bàn phím (mỗi thuộc tính một dòng)
        self.__nhanhieu = input()
        self.__maso = input()
        self.__nuocsx = input()
        self.__tkdien = input().strip().lower() == 'true'
        self.__dungtich = int(input())
        self.__gia = int(input())

    def layNhanHieu(self):
        return self.__nhanhieu

    def layGia(self):
        return self.__gia

    def soNguoiSD(self):
        return int(self.__dungtich // 100)

    def cungNhanHieu(self, tl):
        return self.__nhanhieu == tl.__nhanhieu

    def nhHon(self, tl):
        return self.__dungtich < tl.__dungtich

    def hienThi(self):
        print(self)

    def __str__(self):

        tiet_kiem = "Có" if self.__tkdien else "Không"
        
        lines = [
            f"Nhãn hiệu: {self.__nhanhieu}",
            f"Mã số: {self.__maso}",
            f"Nước SX: {self.__nuocsx}",
            f"T/K điện: {tiet_kiem}",
            f"Dung tích: {self.__dungtich}L",
            f"Giá: {self.__gia}VNĐ",

        ]
        return "\n".join(lines)
