M = int(input())
N = int(input())

_sum = 0
_min = N+1

for i in range(M, N +1):
    count = 0
    for j in range(1, i+1):
        if i % j == 0:
            count += 1
        if count > 2:
            break
    
    if count == 2 :
        _sum += i
        if i < _min:
            _min = i

if _sum == 0:
    print(-1)
else:
    print(_sum)
    print(_min)
    