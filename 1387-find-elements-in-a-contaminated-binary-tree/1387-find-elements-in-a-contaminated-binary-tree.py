# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class FindElements:
    
    def __init__(self, root: Optional[TreeNode]):
        self.root = TreeNode()
        def rec(root):
            if(not root):
                return
            if(root.left):
                root.left.val = root.val*2+1
                rec(root.left)
            if(root.right):
                root.right.val = root.val*2+2
                rec(root.right)

        root.val = 0
        rec(root)
        self.root = root

    def find(self, target: int) -> bool:
        self.ans = self.root.val == target
        def rec(root):
            if not root:
                return
            if root.val == target:
                self.ans = True
                return 
            if(not self.ans):
                rec(root.left)
            if(not self.ans):
                rec(root.right)
        rec(self.root)
        return self.ans

# Your FindElements object will be instantiated and called as such:
# obj = FindElements(root)
# param_1 = obj.find(target)