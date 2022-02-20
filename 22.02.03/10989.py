import sys

N = int(sys.stdin.readline())
sortedArray = [0]*(10000+1)
for i in range(N):
    sortedArray[int(sys.stdin.readline())] +=1
    
for i in range(len(sortedArray)):
    if sortedArray[i] != 0:
        for j in range(sortedArray[i]):
            print(i)
    # if sortedArray[i] > 0:
    #     print('{}\n'.format(i)*sortedArray[i], end='')


# 계수 정렬
# 참고 : https://velog.io/@gndan4/%EC%A0%95%EB%A0%AC-%EC%95%8C%EA%B3%A0%EB%A6%AC%EC%A6%98
# https://wikidocs.net/130182