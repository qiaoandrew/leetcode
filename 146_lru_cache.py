class Node:

    def __init__(self, key, val):
        self.key = key
        self.val = val

        self.next = None
        self.prev = None


class LRUCache:

    def __init__(self, capacity):
        self.capacity = capacity
        self.nodes = {}

        self.left = Node(0, 0)
        self.right = Node(0, 0)

        self.left.next = self.right
        self.right.prev = self.left

    def get(self, key):
        if key in self.nodes:
            self.remove(self.nodes[key])

            self.insert(self.nodes[key])

            return self.nodes[key].val
        else:
            return -1

    def put(self, key, value):
        if key in self.nodes:
            self.remove(self.nodes[key])

        self.nodes[key] = Node(key, value)
        self.insert(self.nodes[key])

        if len(self.nodes) > self.capacity:
            lru = self.left.next
            self.remove(lru)
            del self.nodes[lru.key]

    def insert(self, node):
        prev = self.right.prev
        nxt = self.right

        node.prev = prev
        node.next = nxt

        nxt.prev = node
        prev.next = node

    def remove(self, node):
        prev = node.prev
        nxt = node.next

        prev.next = nxt
        nxt.prev = prev


# class ListNode:

#     def __init__(self, key, val):
#         self.key = key
#         self.val = val
#         self.prev = None
#         self.next = None

# class LRUCache:

#     def __init__(self, capacity):
#         self.capacity = capacity
#         self.cache = {}

#         self.left = ListNode(0, 0)
#         self.right = ListNode(0, 0)

#         self.left.next = self.right
#         self.right.prev = self.left

#     def get(self, key):
#         if key in self.cache:
#             self.remove(self.cache[key])
#             self.insert(self.cache[key])

#             return self.cache[key].val
#         else:
#             return -1

#     def put(self, key, value):
#         if key in self.cache:
#             self.remove(self.cache[key])

#         self.cache[key] = ListNode(key, value)
#         self.insert(self.cache[key])

#         if len(self.cache) > self.capacity:
#             lru = self.left.next

#             self.remove(lru)

#             del self.cache[lru.key]

#     def insert(self, node):
#         prev = self.right.prev
#         nxt = self.right

#         prev.next = node
#         nxt.prev = node

#         node.next = nxt
#         node.prev = prev

#     def remove(self, node):
#         prev = node.prev
#         nxt = node.next

#         prev.next = nxt
#         nxt.prev = prev
