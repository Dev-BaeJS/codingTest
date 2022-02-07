import sys

N = int(sys.stdin.readline())

while True:
    if N == 1 :
        break
    for i in range(2, int(N)+1):
        if N % i == 0:
            print(i)
            N = N / i
            break
    