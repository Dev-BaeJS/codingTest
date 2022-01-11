# import sys

# S = list(sys.stdin.readline())

# aList = list()

# for i in range(ord('a'),ord('z')+1):
#     aList.append(i)

# count = 0
# for i in S:
#     if(ord(i) in aList):
#         aList[aList.index(ord(i))] = count
#     count+=1
    
# for i in aList:
#     if i >= 97:
#         print(-1, end=' ')
#     else:
#         print(i, end=' ')
  
# 정답...          
string = input()
alphabet = "abcdefghijklmnopqrstuvwxyz"
for i in alphabet:
    print(string.find(i), end = ' ')