def reverse_between(head, left, right):
    prev, cur = None, head
    for _ in range(left - 1):
        prev, cur = cur, cur.next
    
    last_node_first_part = prev
    last_node_second_part = cur

    for _ in range(right - left + 1):
        nxt = cur.next
        cur.next = prev
        prev, cur = cur, nxt
    
    if last_node_first_part:
        last_node_first_part.next = prev
    else:
        head = prev
    
    last_node_second_part.next = cur

    return head