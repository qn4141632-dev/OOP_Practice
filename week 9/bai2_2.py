class LineSegmentTest:

    def testCase(self):
        x1, y1, x2, y2 = map(int, input().split())
        ls1 = LineSegment(x1,y1,x2,y2)
        ls1.print()
        print(ls1.length())
        print(ls1.angle())
        ls2 = LineSegment(ls1)
        ls1.move(1,1)
        ls1.print()
        ls2.print()
