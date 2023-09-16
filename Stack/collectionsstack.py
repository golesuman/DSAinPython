import collections

stack = collections.deque()
print(stack)
stack.append(5)
print(stack)
stack.append(3)
stack.append(6)
stack.append(9)

stack.append(4)
stack.append(8)
print(stack)
stack.pop()
print(stack)
stack.pop()
print(stack)
stack.pop()
print(stack)
