def has_cycle(nodes):
    slow = nodes
    fast = nodes
    
    while fast and fast.next:
        slow = slow.next
        fast = fast.next.next
        
        if slow == fast:
            return True
        
    return False