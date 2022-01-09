import sys

N = int(sys.stdin.readline())
array = list((map(int, sys.stdin.readline().split())))

top = max(array)

for i in range(len(array)):
    array[i]= array[i] / top * 100
    
print(sum(array, 0.0) / len(array))