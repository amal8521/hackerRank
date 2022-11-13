from collections import deque

from collections import deque
q = deque()
q.append('a')
q.append('b')
q.append('c')

print(q)

# pop

print(q.popleft())
print(q.popleft())
print(q.popleft())

print(q)
