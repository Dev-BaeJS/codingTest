import sys
N = int(sys.stdin.readline())

def factorial(i):
    if i == 1:
        return 1
    else:
        return i * factorial(i-1)
        
print(factorial(N))

# def multiply(n, m):
#     return n*m

# N = int(input())
# count = 1
# mul = 1
# while True:
#     mul = multiply(mul, count)
#     if count == N:
#         break
#     count+=1

# print(mul)

############################### 정답
# def factorial(n):
#     result = 1
#     if n > 0 :
#         result = n * factorial(n-1)
#     return result

# n = int(input())
# print(factorial(n))