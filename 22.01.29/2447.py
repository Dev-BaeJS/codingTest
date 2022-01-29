import sys
sys.setrecursionlimit(10 ** 6)

def star(a):
    if a == 1:
        return ['*']
    
    Stars = star(a//3)
    L = []
    
    for S in Stars:
        L.append(S*3)
    for S in Stars:
        L.append(S+" "*(a//3)+S)
    for S in Stars:
        L.append(S*3)
    return L

N = int(sys.stdin.readline().strip()) # 3 9 27 81
print('\n'.join(star(N)))



"""
해설 : 
https://cotak.tistory.com/38
"""