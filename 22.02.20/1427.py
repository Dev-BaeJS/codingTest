import sys

N = sys.stdin.readline().split()

array = [0]*10

for i in N[0]:
    array[int(i)] += 1
    
for i in range(9, -1, -1):
    for j in range(array[i]):
        print(i, end="")