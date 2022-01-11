import sys

word = sys.stdin.readline().upper()

string = []
numList = list()
for i in range(ord('A'), ord('Z')+1):
    string.append(chr(i))
    numList.append(0)
    
for i in word:
    if i != '\n':
        numList[string.index(i)] += 1

newList = numList.copy()
numList.sort()
if(numList[-1] == numList[-2]):
    print('?')
else:
    print(string[newList.index(numList[-1])])