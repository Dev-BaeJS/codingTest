import sys

array = list()

for i in range(10):
    array.append(int(sys.stdin.readline()))
    array[i] = array[i] % 42

count = 0

for i in range(42):
    if(array.count(i) > 0):
        count+=1

print(count)
        