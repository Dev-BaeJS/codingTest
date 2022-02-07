N = int(input())

inputs = list(map(int, input().split()))

def check(num):
    count = 0
    
    for i in range(1, num+1):
        if num % i == 0:
            count += 1
        if count > 2:
            return False
    
    if count == 2:
        return True

checkNum = 0
for i in inputs:
    if check(i) :
        checkNum += 1
        
print(checkNum)