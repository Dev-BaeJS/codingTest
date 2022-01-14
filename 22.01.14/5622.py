import sys

string = list()
for i in range(ord('A'), ord('Z')+1):
    string.append(chr(i))

aArray = list()
for i in range(len(string) // 3):
    aArray.append(3+i)

sum = 0

A = sys.stdin.readline()

for i in range(len(A)-1):
    if(A[i] == 'Z'):
        sum += 10
    else:
        sum += 3 + string.index(A[i]) // 3
        
    
print(sum)


# alpabet_list = ['ABC','DEF','GHI','JKL','MNO','PQRS','TUV','WXYZ']
# word = input()

# time = 0
# for unit in alpabet_list :  
#     for i in unit:  # alpabet 리스트에서 각 요소를 꺼내서 한글자씩 분리
#         for x in word :  # 입력받은 문자를 하나씩 분리
#             if i == x :  # 두 알파벳이 같으면
#                 time += alpabet_list.index(unit) +3  # time = time + index +3
# print(time)