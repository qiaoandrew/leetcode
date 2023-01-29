class ListNode:

    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


def add_two_numbers(l1, l2):
    head = ListNode(0)
    cur = head

    carry = 0

    while l1 or l2 or carry:
        cur_sum = carry

        if l1:
            cur_sum += l1.val
            l1 = l1.next

        if l2:
            cur_sum += l2.val
            l2 = l2.next

        carry = cur_sum // 10

        l1 = l1.next
        l2 = l2.next

        cur.next = ListNode(cur_sum % 10)
        cur = cur.next

    return head.next