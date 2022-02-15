from itertools import combinations
import sys

T = int(sys.stdin.readline())

def combinationLength(n,m):
    top = 1
    bottom = 1
    for i in range(1, m + 1):
        top *= (n - i + 1)
        bottom *= (m - i + 1)
        
    return top // bottom


for i in range(T):
    N,M = map(int, sys.stdin.readline().split())
    print(combinationLength(M, N))
    # MList = [0]* M
    # combi = list(combinations(MList, N))
    # print(len(combi))
    