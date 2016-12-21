import sys

# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def maxPathSum(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        self.max_sum = -sys.maxsize
        self.max_path(root)
        return self.max_sum

    def max_path(self, node):
        if not node:
            return 0
        left = self.max_path(node.left)
        right = self.max_path(node.right)
        self.max_sum = max(self.max_sum, node.val + left + right, node.val, node.val + left, node.val + right)
        return node.val + max(left, right)

class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

    def __str__(self):
        return "{}({}, {})".format(self.val, str(self.left), str(self.right))

    def add(self, x):
        if x <= self.val:
            if self.left:
                self.left.add(x)
            else:
                self.left = TreeNode(x)
        else:
            if self.right:
                self.right.add(x)
            else:
                self.right = TreeNode(x)

    

        
