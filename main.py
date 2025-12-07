from collections import deque

class TreeNode:
    """
    Binary tree node for Wi-Fi routers.

    value: integer capacity
    left, right: TreeNode or None
    """

    def __init__(self, value, left=None, right=None):
        self.value = value
        self.left = left
        self.right = right


def max_level_sum(root):
    """
    Return (best_level_index, best_sum) where best_level_index is the level
    with the highest sum of node values, and best_sum is that sum.

    For an empty tree (root is None), return (None, 0).
    """

    if root is None:
        return (None, 0)

    queue = deque([root])
    level = 0
    best_level = 0
    best_sum = float("-inf")

    while queue:
        level_size = len(queue)
        level_sum = 0

        for _ in range(level_size):
            node = queue.popleft()
            level_sum += node.value

            if node.left:
                queue.append(node.left)
            if node.right:
                queue.append(node.right)

        # check if this level is better than previous best
        if level_sum > best_sum:
            best_sum = level_sum
            best_level = level

        level += 1

    return (best_level, best_sum)
