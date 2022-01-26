import sys

def cal(number, divider):
    return number // divider , number % divider
    

container = [3, 5]
answer = [0,0]
N = int(sys.stdin.readline())

num = N
while True:
    a , b = cal(num, container[1])
    if b == 0:
        answer[1] = a
        num = b
        break
    else:
        if(num < container[0]):
            break
        num -= container[0]
        answer[0] += 1
        continue

if num != 0:
    print(-1)
else:
    print(answer[0] + (answer[1]))