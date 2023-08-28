from collections import deque


class MyStack:

    def __init__(self):
        self.queue1 = deque()
        self.queue2 = deque()
        self._top = 0

    def push(self, x: int) -> None:
        self.queue1.append(x)
        self._top = x

    def pop(self) -> int:
        while len(self.queue1) > 1:
            self._top = self.queue1.popleft()
            self.queue2.append(self._top)
        res = self.queue1.popleft()
        self.queue1, self.queue2 = self.queue2, self.queue1
        return res

    def top(self) -> int:
        return self._top

    def empty(self) -> bool:
        return len(self.queue1) == 0
