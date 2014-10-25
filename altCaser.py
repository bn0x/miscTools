import sys

class caser(object):
    def __init__(self, ifStdin=False):
        self.stdin = ifStdin
        if ifStdin:
            self.oldStr = sys.stdin.read()
            self.operate(self.oldStr)

    def operate(self, oldStr):
        self.oldStr = oldStr
        self.newStr = ""
        for char in range(len(self.oldStr)):
            if self.is_odd(char):
                self.newStr += self.oldStr[char].lower()
            else:
                self.newStr += self.oldStr[char].upper()
        if self.stdin:
            print(self.newStr)
        else:
            return self.newStr

    def is_odd(self, num):
        return num & 0x1

if __name__ == "__main__":
    caser(ifStdin=True)