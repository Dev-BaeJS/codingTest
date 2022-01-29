n = int(input())

def Fib(a):
    if a == 0:
        return 0
    if a == 1:
        return 1
    
    
    return Fib(a-1)+Fib(a-2)
    
print(Fib(n))
