class Solution:
    def longestCommonSubsequence(self, text1: str, text2: str) -> int:
        
        # Initalize a 2D DP Array
        dp = [[0] * (len(text2) + 1) for _ in range(len(text1) + 1)]

        for i in range(1, len(text1) + 1):
            for j in range(1, len(text2) + 1):
                # If the values are equal, increment the diagonal value by one
                if text1[i - 1] == text2[j - 1]:
                    dp[i][j] = dp[i - 1][j - 1] + 1
                # If not, take the max of the left and the top
                else:
                    dp[i][j] = max(dp[i - 1][j], dp[i][j - 1])
        
        return dp[len(text1)][len(text2)]