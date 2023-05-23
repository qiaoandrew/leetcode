class TreeNode:

    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


def sorted_array_to_bst(nums):

    def get_bst(left, right):
        if left > right:
            return None

        mid = left + (right - left) // 2

        root = TreeNode(nums[mid])

        root.left = get_bst(left, mid - 1)
        root.right = get_bst(mid + 1, right)

        return root

    return get_bst(0, len(nums) - 1)
