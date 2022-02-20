import sys

N = int(sys.stdin.readline())

array = list()
for i in range(N):
    array.append(list(map(int, sys.stdin.readline().split())))
    
# print(array)

array.sort(key = lambda x:x[1])
array.sort(key = lambda x:x[0])
for i in array:
    print(i[0], i[1])