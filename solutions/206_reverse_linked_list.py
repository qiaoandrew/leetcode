def reverse_list(head):
    prev = None
    cur = head

    while cur:
        nxt = cur.next

        cur.next = prev

        prev = cur
        cur = nxt

    return prev
