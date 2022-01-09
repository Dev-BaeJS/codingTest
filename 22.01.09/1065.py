import sys

def func(a : int):
    if(a < 10):
        return 1
    
    array = list(map(int, str(a)))
    add = list()
    for i in range(len(array) - 1):
        # print("#"+str(array[i+1] - array[i]))
        add.append(array[i+1] - array[i])
        
    newList = list(set(add))
    # print(len(newList))
    return len(newList)

N = int(sys.stdin.readline())
count = 0
for i in range(1, N+1):
    if(func(i) == 1):
        count+=1
print(count)