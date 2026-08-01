from typing import List, Optional


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def buildTree(self, inorder: List[int], postorder: List[int]) -> Optional[TreeNode]:
        # 前提假设：树中所有节点值互不相同（题目保证）
        # 用哈希表记录每个值在 inorder 中的下标位置，避免每次线性查找 -> O(n)
        idx_map = {val: i for i, val in enumerate(inorder)}

        def helper(in_left: int, in_right: int) -> Optional[TreeNode]:
            # in_left, in_right 是当前子树对应的 inorder 区间 [in_left, in_right)
            if in_left == in_right:
                return None

            # postorder 的最后一个元素，就是"当前这段区间"对应子树的根
            # （后序遍历定义：左-右-根，根永远在最后）
            root_val = postorder.pop()
            root = TreeNode(root_val)

            # 查根值在 inorder 中的位置，从而把当前区间切成左右两段
            idx = idx_map[root_val]

            # 必须先构建右子树，再构建左子树
            # 因为 postorder 是从后往前 pop 的，倒序读出来是"根 -> 右 -> 左"
            # 如果先pop左子树，会把本该属于右子树的值错误地取走
            root.right = helper(idx + 1, in_right)   # inorder[idx+1 : in_right] -> 右子树
            root.left = helper(in_left, idx)          # inorder[in_left : idx]   -> 左子树

            return root

        return helper(0, len(inorder))