num_student = int(input())
student_list = []

for _ in range(num_student):
    weight, height = map(int, input().split())
    student_list.append((weight, height))

for i in student_list:
    rank = 1
    for j in student_list:
        if i[0] < j[0] and i[1] < j[1]:
                rank += 1
    print(rank, end = " ")

##########################
# 풀지 못한 이유 : count 와 rank 사이 수식을 구하지 못함

# from itertools import combinations
# from itertools import permutations

# N = int(input())
# person = list()
# ranking = list()
# for i in range(N):
#     person.append(list(map(int,input().split())))
#     ranking.append(0)

# for i in range(N-1):
#     for j in range(i,N):
#         if person[i][0] > person[j][0] and person[i][1] > person[j][1]:
#             ranking[i] += 1
#         elif person[i][0] < person[j][0] and person[i][1] < person[j][1]:
#             ranking[j] += 1
            
# print(ranking)

# newRanking = ranking[:]
# newRanking = list(set(newRanking))
# newRanking = sorted(newRanking, reverse=True)
# print(newRanking)
# print(ranking)

# resultRanking = ranking[:]
# # 순위 추가한 사람 갯수
# count = 0
# # 최근 순위
# rank = 1
# for i in range(len(newRanking)):
#     resultRanking[ranking.index(newRanking[i])] = rank + count
#     count += ranking.count(newRanking[i])
#     rank += count
    
# for i in resultRanking:
#     print(i, end=" ")