from collections import deque

deq = deque()

deq.append(1)
deq.append(2)
deq.append(3)

print(type(deq))
print(deq)

a = deq.pop()
print(a)
print(deq)

deq.append(4)
deq.append(5)
deq.append(6)

deq.rotate(1)
deq.rotate(1)

print(deq)