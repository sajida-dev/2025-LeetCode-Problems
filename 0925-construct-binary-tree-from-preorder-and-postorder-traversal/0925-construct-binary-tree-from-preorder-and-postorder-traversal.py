class Solution:
    def constructFromPrePost(
        self, preorder: List[int], postorder: List[int]
    ) -> Optional[TreeNode]:
        n = len(preorder)
        return self._construct_tree(0, n-1, 0, preorder, postorder)

    # Helper function to construct the tree recursively
    def _construct_tree(
        self,
        pre_start: int,
        pre_end: int,
        post_start: int,
        preorder: List[int],
        postorder: List[int],
    ) -> Optional[TreeNode]:
        if pre_start > pre_end:
            return None

        if pre_start == pre_end:
            return TreeNode(preorder[pre_start])

        left_root = preorder[pre_start + 1]

        num_of_nodes_in_left = 1
        while postorder[post_start + num_of_nodes_in_left - 1] != left_root:
            num_of_nodes_in_left += 1

        root = TreeNode(preorder[pre_start])

        root.left = self._construct_tree(
            pre_start + 1,
            pre_start + num_of_nodes_in_left,
            post_start,
            preorder,
            postorder,
        )

        root.right = self._construct_tree(
            pre_start + num_of_nodes_in_left + 1,
            pre_end,
            post_start + num_of_nodes_in_left,
            preorder,
            postorder,
        )

        return root