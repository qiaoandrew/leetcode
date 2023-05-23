from collections import deque


class MyStack:

    def __init__(self):
        self.stack = deque()
        self.reverse_stack = deque()

    def push(self, x):
        self.stack.append(x)
        self.reverse_stack.appendleft(x)

    def pop(self):
        self.reverse_stack.popleft()
        return self.stack.pop()

    def top(self):
        return self.stack[-1]

    def empty(self):
        return len(self.stack) == 0
