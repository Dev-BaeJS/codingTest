import sys
inputs = list(map(int, sys.stdin.readline().split()))
# print(inputs)

gap = inputs[0] - inputs[1]
# print(gap)

if inputs[2] == inputs[0]:
    print(1)
else:
    if((inputs[2]-inputs[0]) % gap == 0):
        print((inputs[2]-inputs[0]) // gap + 1)
    else:
        print((inputs[2]-inputs[0]) // gap + 2)