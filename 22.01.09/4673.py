def D(a: int()):
    return sum(map(int, str(a))) + a

array = list()
for i in range(1, 10001):
    array.append(i)

excecpt = list()

for i in array:
    if(D(i) <= 10000):
        excecpt.append(array[array.index(D(i))])
    
newList = list(set(excecpt))

for i in range(len(newList)):
    array.remove(newList[i])

for i in array:
    print(i)