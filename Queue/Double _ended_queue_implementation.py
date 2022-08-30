# double ended queue
# append left and pop method
import collections
q = collections.deque()
q.appendleft(10)
q.appendleft(20)
q.appendleft(30)
q.pop()
q.pop()
q.pop()
print(q)

# append and pop left method
import collections
q = collections.deque()
q.append(10)
q.append(20)
q.append(30)
q.popleft()
q.popleft()
q.popleft()
print(q)
