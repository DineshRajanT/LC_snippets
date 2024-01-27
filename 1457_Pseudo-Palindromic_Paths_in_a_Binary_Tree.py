# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def pseudoPalindromicPaths (self, root: Optional[TreeNode]) -> int:
    
        res = [0]
        counter = [0] * 9 # 1 <= Node.val <= 9 so we maintain a counter list for the sets
        
        def dfs(node: Optional[TreeNode]) -> None:
                
            counter[node.val - 1] += 1
    
            if not node.left and not node.right and isPseudoPalindromic():
                res[0] += 1
            
            if node.left:
                dfs(node.left)
            if node.right:
                dfs(node.right) 

            counter[node.val - 1] -= 1

        def isPseudoPalindromic() -> bool:
            
            pathLength, numOdd = sum(counter), 0
            for count in counter:
                if count != 0 and (count % 2) == 1:
                    numOdd += 1 
            return numOdd <= 1

        dfs(root)
        return res[0]

        