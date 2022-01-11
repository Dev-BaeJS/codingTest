import sys

T = int(sys.stdin.readline())

for i in range(T):
    lineInput = list(map(str, sys.stdin.readline().split()))
    text = ''
    for j in lineInput[1]:
        text += j*int(lineInput[0])
    print(text)