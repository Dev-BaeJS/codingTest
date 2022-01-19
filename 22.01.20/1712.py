inputs = list(map(int, input().split()))

idx = 1;

while (inputs[0] + inputs[1] * idx) > inputs[2] * idx:
    idx+=1;
print(idx)