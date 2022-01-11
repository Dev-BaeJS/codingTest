def func(a : []):
    return int(a[0]) * 100 + int(a[1]) * 10 + int(a[2])

import sys

nums = list(sys.stdin.readline().split())

firstNum = []
secondNum = []
for i in nums[0]:
    firstNum.insert(0, i)
    
for i in nums[1]:
    secondNum.insert(0, i)
  
if(func(firstNum) > func(secondNum)):
    print(func(firstNum))
else:
    print(func(secondNum))