class ListNode:

    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


def merge_two_lists(list1, list2):
    sentinel = ListNode()
    cur = sentinel

    while list1 or list2:
        if not list1:
            cur.next = list2
            break
        elif not list2:
            cur.next = list1
            break
        elif list1.val < list2.val:
            cur.next = ListNode(list1.val)
            list1 = list1.next
        else:
            cur.next = ListNode(list2.val)
            list2 = list2.next

        cur = cur.next

    return sentinel.next