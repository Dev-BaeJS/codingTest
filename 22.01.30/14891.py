import sys, collections
s = []
for _ in range(4):
    s.append(collections.deque(list(input())))


K = int(sys.stdin.readline())
R = [list(map(int, sys.stdin.readline().split())) for _ in range(K)]

#왼쪽 톱니바퀴 확인
def left(num, direction): 
    if num < 0:
        return 
    if s[num][2] != s[num+1][6]:
        left(num-1, -direction)
        s[num].rotate(direction)

#오른쪽 톱니바퀴 확인
def right(num, direction): 
    if num > 3:
        return
    if s[num][6] != s[num-1][2]:
        right(num+1, -direction)
        s[num].rotate(direction)

for i in range(K):
    num = R[i][0] - 1
    direction = R[i][1]
    
    left(num-1, -direction)
    right(num+1, -direction)
    s[num].rotate(direction)

res = 0

if s[0][0] == '1':
    res += 1
if s[1][0] == '1':
    res += 2
if s[2][0] == '1':
    res += 4
if s[3][0] == '1':
    res += 8
    
print(res)

# 출처 
# https://hapbbying.tistory.com/64
# https://yeoping.tistory.com/19

######################################################

# import sys

# def rotate(string, dir):
#     if dir > 0 : # 시계방향
#         # string = ['123123']
#         last = string.pop(len(string)-1)
#         print("###"+str(last))
#         string.insert(0, last)
#         return string
#     else: # 반시계방향
#         first = string.pop(0)
#         string.insert(len(string), first)
#         return string

# def com(a, aindex,  b, bindex):
#     if(a[aindex] == b[bindex]):
#         return True
#     else:
#         return False
    
# # 입력
# wheels = []
# for i in range(4):
#     wheels.append(sys.stdin.readline().split())

# K = int(sys.stdin.readline())
# directions = []
# for i in range(K):
#     directions = list(map(int, sys.stdin.readline().split()))
#     # print(str(directions[0]) + "#####" + str(directions[1]))
#     # if directions[0]
#     directions[0] -= 1
#     print(wheels[directions[0]])
#     wheels[directions[0]] = rotate(str(wheels[directions[0]]) , directions[1])
#     print(wheels[directions[0]])

    
#     # print(com(wheels[directions[0]], 4, wheels[directions[1]], 0))