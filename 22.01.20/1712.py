inputs = list(map(int, input().split()))


if(inputs[1] >= inputs[2]):
    print(-1);
else:
    print(inputs[0]//(inputs[2] - inputs[1]) +1)

# idx = 1;

# while (inputs[0] + inputs[1] * idx) >= inputs[2] * idx:
#     idx+=1;
    
# print(idx)