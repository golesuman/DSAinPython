import queue

stack = queue.LifoQueue(5)
stack.put(3)
stack.put(5)
stack.put(8)
stack.put(9)
stack.put(10)
print(stack.get())
print(stack.get())
print(stack.get())
print(stack.get())
print(stack.get())
