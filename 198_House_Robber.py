from typing import List

class Solution:
    def rob(self, nums: List[int]) -> int:
        # T: O(n)
        # S: O(1)

        rob1, rob2 = 0, 0 # rob1 is n-1, rob2 is n-2

        for n in nums:
            temp = max(rob2 + n, rob1)
            rob2 = rob1
            rob1 = temp
            
        return rob1