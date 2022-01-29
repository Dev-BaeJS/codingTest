import sys
sys.setrecursionlimit(10 ** 6)

def operate(index, start, end):
    if index == 1:
        print(start, end)
        return
    
    operate(index -1, start, 6 - start - end)
    print(start, end)
    operate(index -1, 6 - start - end, end)

N = int(sys.stdin.readline().strip())
print(2**N -1)
operate(N, 1, 3)
    
"""
해설 : https://study-all-night.tistory.com/6   
"""