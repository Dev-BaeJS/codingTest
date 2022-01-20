N = int(input())

start = 1;

Lasts = [1]
count = 1
while True:
    if(Lasts[-1] >= N):
        break
    Lasts.append( Lasts[-1] + 6*count )
    count += 1

print(count)

    

# 1 7 19 37 61 91

# 1     -1
# 2~7   -6
# 8~19  -12
# 20~37 -18
# 38~61 -24
# 62~91 -30
# 
