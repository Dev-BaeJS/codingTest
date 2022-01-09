import sys

T = int(sys.stdin.readline())
for i in range(T):
    string = sys.stdin.readline()
    score = 0
    loop = 0 # 몇 번 연속으로 정답을 맞췄는지
    for i in range(len(string)):
        if(string[i] == 'O'):
            score+= 1+loop
            loop+=1
        else:
            loop = 0
    
    print(score)