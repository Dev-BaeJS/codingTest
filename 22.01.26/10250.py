import sys
import math

T = int(sys.stdin.readline())
inputs = []
answer = []
for i in range(T):
    inputs = list(map(int, sys.stdin.readline().split()))
    
    a = inputs[2] % inputs[0]
    if a == 0:
        a = inputs[0]
    
    b = math.ceil(inputs[2] / inputs[0])
    if b < 10 :
        b = "0"+str(b)

    answer.append(str(a) + str(b) )
    
for i in answer:
    print(i)