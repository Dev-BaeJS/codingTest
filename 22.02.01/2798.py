from itertools import combinations

N,M = map(int, input().split())
numList = list(map(int, input().split()))

combinationList = list(combinations(numList, 3))
nearCombination = 0

for cardCombi in combinationList:
    if nearCombination < sum(cardCombi) <= M:
        nearCombination = sum(cardCombi)
        
print(nearCombination)

##############################
# 1트에 틀린 이유, 문제를 제대로 이해하지 못함
# M을 넘지 않으면서 M에 가까운 3장의 합을 구하는 것이 문제인데
# M에 최대한 근접한 합을 찾는 것으로 풀었음..

# sumlist = list()

# for item in combinationList:
#     sumlist.append(sum(item))
#     # print(sum(item))
        
# sumlist = list(set(sumlist))
# newSumList = sumlist[:] # 얕은 복사

# for i in range(len(newSumList)):
#     newSumList[i] -= M
#     newSumList[i] = abs(newSumList[i])

# print(sumlist[newSumList.index(min(newSumList))])