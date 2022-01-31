N = int(input())

def Sum(num):
    string = str(num)
    result = 0
    for i in range(len(string)):
        result += int(string[i])
    return result

index = 0

for i in range(N):
    if i + Sum(i) == N:
        index = i 
        break
    
print(index)