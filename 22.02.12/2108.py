import sys

N = int(sys.stdin.readline())
inputs = list()
for i in range(N):
    inputs.append(int(sys.stdin.readline()))
    
print(round(sum(inputs)/N))
print(sorted(inputs)[N//2])
newSet = set(inputs)
print(sorted(newSet)[1])
print(newSet)
# 최빈값 구해야함

print(sorted(inputs)[N-1] - sorted(inputs)[0])