word = input()
Check = ['c=', 'c-','dz=', 'd-', 'lj', 'nj', 's=', 'z=']

length = 0
for i in range(len(Check)):
    word = word.replace(Check[i], str(i))

print(len(word))