N=int(input())

answer=0

for i in range(N):
    word = input()
    for j in range(len(word)):
        if j!=len(word)-1:
            if word[j]==word[j+1]:
                pass
            elif word[j] in word[j+1:]:
                break
        else:
            answer+=1
print(answer)

# num = int(input())
# words = []
# for i in range(num):
#     words.append(input())
    
# # print(words)

# sum = 0

# for word in words:
#     group = []
#     for i in range(len(word)):
#         if i != len(word)-1:
#             if word[i] == word[i+1]:
#                 pass
#             elif word[i] in word[i+1]:
#                 break
#         else:
#             sum+=1
                        
#         # if word[i] not in group:
#         #     group.append(word[i])
#         # elif word[i] in group:
#         #     if word[i-1] == word[i]:
#         #         pass
#         #     else:
#         #         group.remove(word[i]) 
#     # # print(group)
#     # # print(word)
#     # result = ''.join(dict.fromkeys(word))
#     # # print(result)
#     # group = "".join(group)
#     # # print(group)
#     # if group == result:
#     #     sum+=1
        
# print(sum)