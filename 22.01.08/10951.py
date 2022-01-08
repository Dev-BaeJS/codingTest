import sys

while True :
    try:
        n,m = map(int, sys.stdin.readline().split())
        print(n+m)
    except:
        break
        
# try- except 문없이 하기.
# import sys
# for line in sys.stdin:
#   a,b = map(int,line.split())
#   print(a+b)
