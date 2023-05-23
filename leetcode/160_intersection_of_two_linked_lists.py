def get_intersection_node(head1, head2):
    p1 = head1
    p2 = head2

    while p1 != p2:
        p1 = p1.next if p1 else head2
        p2 = p2.next if p2 else head1

    return p1
