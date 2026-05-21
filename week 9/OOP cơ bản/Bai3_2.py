class ColorPointTest:
    def testCase(self):
        c1 = ColorPoint()
        c1.print()

        data = input().split()

        if len(data) == 3:
            x = int(data[0])
            y = int(data[1])
            color = data[2]
        else:
            x = int(data[1])
            y = int(data[2])
            color = data[3]

        c2 = ColorPoint(x, y, color)
        c2.print()

        c3 = ColorPoint(c2)

        c2.move(5, 5)

        c2.print()
        c3.print()
