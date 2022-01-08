import sys

array = []

for i in range(9):
    array.append(int(sys.stdin.readline())) 

print(max(array))
print(array.index(max(array)) + 1 )