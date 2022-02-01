N = int(input())

num = 0
numList = []

while True:
    if str(num).__contains__('666'):
        numList.append(num)
        
    num += 1
    
    if len(numList) == N:
        break
print(numList[-1])
        
    


# 666 1666 2666 3666 4666 5666 
# 6660 6661 6662 6663 6664 6665 6666 6667 6668 6669
# 7666 8666 9666
#
# 10666 11666 -- 99666