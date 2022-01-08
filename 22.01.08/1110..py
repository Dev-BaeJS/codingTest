import sys

i = 0;
N = int(sys.stdin.readline())
new = N

while True:
    i+=1
    
    if(new // 10 < 1):
        a = 0 
    else:
        a = new // 10
        
    b = new % 10
    
    if(a+b >= 10):
        new = b*10 + (a+b) % 10
    else:
        new = b*10 + a + b
        
    if(new == N):
        break

print(i)

