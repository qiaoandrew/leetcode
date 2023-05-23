class ListNode:

    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


# separate list into two halves
# reverse the second half
# weave both halves together
def reorder_list(head):

    def reverse(head):
        prev = None
        cur = head

        while cur:
            nxt = cur.next
            cur.next = prev

            prev = cur
            cur = nxt

        return prev

    slow = head
    fast = head

    while fast and fast.next:
        slow = slow.next
        fast = fast.next.next

    first_half = head
    second_half = reverse(slow.next)
    slow.next = None

    sentinel = ListNode()
    cur = sentinel

    while first_half:
        cur.next = first_half
        cur = cur.next
        first_half = first_half.next

        if second_half:
            cur.next = second_half
            cur = cur.next
            second_half = second_half.next

    return sentinel.next