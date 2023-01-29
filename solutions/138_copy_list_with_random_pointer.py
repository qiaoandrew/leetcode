class Node:

    def __init__(self, x, next, random):
        self.val = int(x)
        self.next = next
        self.random = random


# hashmap to map original node to copied node
# loop through list once to save copied node with values
# loop through list second time to save next and random pointers
def copy_random_list(head):
    original_to_copy = {None: None}

    cur = head

    while cur:
        copy = Node(cur.val)
        original_to_copy[cur] = copy
        cur = cur.next

    cur = head

    while cur:
        copy = original_to_copy[cur]
        copy.next = original_to_copy[cur.next]
        copy.random = original_to_copy[cur.random]
        cur = cur.next

    return original_to_copy[head]