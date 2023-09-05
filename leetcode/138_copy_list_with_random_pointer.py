class Node:

    def __init__(self, x, next, random):
        self.val = int(x)
        self.next = next
        self.random = random


def copy_random_list(head):
    original_to_copy = { None: None }

    cur = head
    while cur:
        original_to_copy[cur] = Node(cur.val)
        cur = cur.next
    
    cur = head
    while cur:
        original_to_copy[cur].next = original_to_copy[cur.next]
        original_to_copy[cur].random = original_to_copy[cur.random]
        cur = cur.next
    
    return original_to_copy[head]