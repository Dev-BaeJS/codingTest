import sys

S = int(sys.stdin.readline())
sumNum = 0
i = 1
while True:
    sumNum += i
    if sumNum > S:
        sumNum -= i
        i -= 1
        break
    i += 1
    
print(i)
