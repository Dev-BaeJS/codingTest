import sys
from collections import Counter

N = int(sys.stdin.readline())
inputs = list()
for i in range(N):
    inputs.append(int(sys.stdin.readline()))
    
def mode(some_list):
    count = Counter(some_list)
    count_order = count.most_common()
    maximum = count_order[0][1]

    modes = []
    for i in count_order:
        if i[1] == maximum:
            modes.append(i[0])

    sorted_modes = sorted(modes)
    if len(sorted_modes) > 1:
        return sorted_modes[1]
    else:
        return sorted_modes[0]

print(round(sum(inputs)/N))
print(sorted(inputs)[N//2])
newSet = set(inputs)
# print(sorted(newSet)[1])
# print(newSet)
# 최빈값 구해야함
print(mode(inputs))
print(sorted(inputs)[N-1] - sorted(inputs)[0])

##
# https://yoonsang-it.tistory.com/42
# #