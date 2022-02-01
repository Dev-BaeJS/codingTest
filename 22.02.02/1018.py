M , N = map(int, input().split())
rowList = list()
for i in range(M):
    rowList.append(input())

minList = []

for i in range(0, M - 7): # 세로
    for j in range(0, N - 7): # 가로
        idx1 = 0
        idx2 = 0
        for a in range(i, i+8):
            for b in range(j, j+8):
                if (a+b) % 2 == 0:
                    if rowList[a][b] != 'W': idx1 +=1
                    if rowList[a][b] != 'B': idx2 +=1
                else:
                    if rowList[a][b] != 'B': idx1 +=1
                    if rowList[a][b] != 'W': idx2 +=1
        minList.append(idx1)
        minList.append(idx2)
    
print(min(minList))

## 3, 4번째 for문에서 꼬였음....
# 아쉽다