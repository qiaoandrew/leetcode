# reverse second half
# loop through first half and second half
def is_palindrome(head):

    def reverse(node):
        prev = None
        cur = node

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

    first = head
    second = reverse(slow)

    while first and second:
        if first.val != second.val:
            return False

        first = first.next
        second = second.next

    return True