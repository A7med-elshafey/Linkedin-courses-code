# try out the Python queue functions
from collections import deque

# ok create a new empty deque object that will function as a queue
ahmed = deque ()

# ok add some items to the queue
ahmed.append(1)
ahmed.append(2)
ahmed.append(3)
ahmed.append(4)

# ok print the queue contents
print(ahmed)

# ok pop an item off the front of the queue
# append one will removed because first in first out
x = ahmed.popleft()
print(x)
print(ahmed)