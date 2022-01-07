import sys

N, X = map(int, sys.stdin.readline().split())
idxList = list(map(int, sys.stdin.readline().split()))

for i in range(N):
    if(idxList[i] < X):
        print(idxList[i] , end= ' ')