import math
class TuLanhTest:
    def testCase(self):
        SEP = "= = = = = = = ="
        
        try:
            line1 = sys.stdin.readline().strip()
            if line1:
                parts1 = line1.split('|')
                tu1 = TuLanh(parts1[0], parts1[1], parts1[2], 
                             parts1[3] == 'True', int(parts1[4]), int(parts1[5]))
                
                # Đọc dòng 2
                line2 = sys.stdin.readline().strip()
                if line2:
                    parts2 = line2.split('|')
                    tu2 = TuLanh(parts2[0], parts2[1], parts2[2], 
                                 parts2[3] == 'True', int(parts2[4]), int(parts2[5]))
                   
                    print(SEP)
                    tu1.hienThi()
                    print(SEP)
                    tu2.hienThi()
                    print(SEP)
        except Exception:
            pass
