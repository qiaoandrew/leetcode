def split_list_to_parts(head, k):
    length = 0
    cur = head
    while cur:
        length += 1
        cur = cur.next

    part_lengths = [length // k + (i < length % k) for i in range(k)]

    res = []
    cur = head

    for part_length in part_lengths:
        prev, cur_part = None, cur

        for _ in range(part_length):
            prev, cur = cur, cur.next
        
        if prev:
            prev.next = None
            
        res.append(cur_part)
    
    return res