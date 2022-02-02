import sys

N = int(sys.stdin.readline())

inputList = list()

for i in range(N):
    inputList.append(int(sys.stdin.readline()))
    
for i in sorted(inputList):
    print(i)
    
# 기존 내장된 sorted 함수는 시간복잡도 O(nlogn)이다.
# 참고 : https://velog.io/@gndan4/%EC%A0%95%EB%A0%AC-%EC%95%8C%EA%B3%A0%EB%A6%AC%EC%A6%98