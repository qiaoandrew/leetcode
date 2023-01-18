def remove_nth_from_end(head, n):
    sentinel = ListNode(0, head)

    slow = sentinel
    fast = sentinel

    for _ in range(n + 1):
        fast = fast.next

    while fast:
        slow = slow.next
        fast = fast.next

    slow.next = slow.next.next

    return sentinel.next