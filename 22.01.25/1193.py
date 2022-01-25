import sys
X = int(sys.stdin.readline())
# X = 3

# if X == 1:
#     print(1/1)
# else:
array = []
count = 1
while True:
    N = (int)(count * (count+1) / 2)
    if(N > X):
        break
    elif N == X:
        array.append(N)
        break
    array.append(N)
    count += 1
    
print(array)
print(count)

gap = X - array[-1] 


if(count % 2 == 0):
    if(gap == 0):
        print(str(count) +'/'+str(1))
    else:
        print(str(gap) +'/'+str(count+1 - gap))
else:
    if(gap == 0):
        print(str(1) +'/'+ str(count) )
    else:
        print(str(count+1 - gap)+'/'+str(gap) )

# 1 3 6 10 15 21 28 36
###################################
# X=int(input())

# line=1
# while X>line:
#     X-=line
#     line+=1
    
# if line%2==0:
#     a=X
#     b=line-X+1
# else:
#     a=line-X+1
#     b=X
    
# print(a, '/', b, sep='')