n = input()

print(sum(map(int,input())))

#############################

n = input()
nums = input()
total = 0
for i in nums :
    total += int(i)  # total= total+int(i)
print(total)

#############################

n = input()
nums = input()
total = 0
for i in range(n) :  # 0부터 n-1까지
    total += int(nums[i])
print(total)