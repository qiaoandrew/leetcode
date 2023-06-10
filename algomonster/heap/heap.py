# Priority queue is abstract data type, heap is data structure used to implement it
# Priority queue: supports inserting item with key and getting / removing itme with smallest / largest key
# Heap: tree-based, filled except last level which is left-justified, no relationship between children unlike binary search tree
#   Min-heap: each node's key is greater than parent's key
#   Max-heap: each node's key is smaller than parent's key

# Implementing heap
# For node i, children stored at ki + 1 to ki + k, parent is at floor((i - 1) / k)

import math


class Heap:
    def __init__(self):
        self.heap = []

    def push(self, item):
        self.heap.append(item)
        self.bubble_up()

    def pop(self):
        if self.size() == 0:
            return None
        min = self.heap[0]
        self.heap[0] = self.heap[-1]
        self.heap.pop()
        self.bubble_down()
        return min

    def bubble_up(self):
        node_idx = len(self.heap) - 1
        while node_idx > 0:
            node = self.heap[node_idx]
            parent_idx = math.floor((node_idx - 1) / 2)
            parent = self.heap[parent_idx]
            if parent <= node:
                break
            self.heap[node_idx] = parent
            self.heap[parent_idx] = node
            node_idx = parent_idx

    def bubble_down(self):
        node_idx = 0
        n = len(self.heap)

        while node_idx < n:
            left = 2 * node_idx + 1
            right = left + 1
            min_idx = node_idx
            if left < n and self.heap[left] < self.heap[min_idx]:
                min_idx = left
            if right < n and self.heap[right] < self.heap[min_idx]:
                min_idx = right
            if min_idx == node_idx:
                break

            self.heap[min_idx], self.heap[node_idx] = self.heap[node_idx], self.heap[min_idx]
            node_idx = min_idx

    def peek(self):
        return self.heap[0]

    def size(self):
        return len(self.heap)
