from collections import deque
queue=deque()
queue.append(3)
queue.append(5)
queue.append(1)
queue.popleft()

for i in range(len(queue)):
 print(queue[i])

test=[]
test.append(3)
test.append(5)
test.append(1)
test.pop()

print(test)