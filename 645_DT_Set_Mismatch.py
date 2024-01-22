class Solution:
    def findErrorNums(self, nums: List[int]) -> List[int]:

        n = len(nums)
        counts = {k:0 for k in range(1,n+1)}
    
        for val in nums:
            counts[val] = counts.get(val,0)+1
            if counts[val] > 1:
                dups = val
            if counts[val] == 0:
                missing = val

        # for k,v in counts.items():
        #     if v > 1:
        #         dups = k
        #     if v == 0:
        #         missing = k
                
        return [dups, missing]

        
