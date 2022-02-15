import sys

N,K = map(int, sys.stdin.readline().split())

numList = list()

for i in range(1, N+1):
    if N % i == 0:
        numList.append(i)
    
if K-1 > len(numList) -1 :
    print(0)
else:
    print(numList[K-1])