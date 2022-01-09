import sys

C = int(sys.stdin.readline())
for i in range(C):
    array = list(map(int,sys.stdin.readline().split()))
    count = array[0]
    del array[0]
    avg = sum(array, 0) / count
    newList = list(filter(lambda x: x>avg, array))
    result = len(newList) / count * 100
    print("{:.3f}".format(round(result, 3)) + "%")