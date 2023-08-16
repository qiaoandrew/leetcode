class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

def partition(head, x):
    before_sentinel = ListNode(0)
    after_sentinel = ListNode(0)
    
    before, after = before_sentinel, after_sentinel
    
    while head:
        if head.val < x:
            before.next = head
            before = before.next
        else:
            after.next = head
            after = after.next
        head = head.next
    
    before.next = after_sentinel.next
    after.next = None
    
    return before_sentinel.next