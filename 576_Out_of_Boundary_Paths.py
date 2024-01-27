class Solution:
    def findPaths(self, m: int, n: int, maxMove: int, startRow: int, startColumn: int) -> int:
        if maxMove == 0:
            return 0  

        dp = [[[0 for _ in range(n)] for _ in range(m)] for _ in range(maxMove)]
        possibleDirections = [(1, 0), (-1, 0), (0, 1), (0, -1)]

        for i in range(m):
            for j in range(n):
                for dx, dy in possibleDirections:
                    row, col = i + dx, j + dy
                    if row < 0 or row >= m or col < 0 or col >= n:
                        dp[0][i][j] += 1

        for k in range(1, maxMove):
            for i in range(m):
                for j in range(n):
                    dp[k][i][j] = dp[0][i][j]
                    for dx, dy in possibleDirections:
                        row, col = i + dx, j + dy
                        if 0 <= row < m and 0 <= col < n:
                            dp[k][i][j] += dp[k - 1][row][col]

        return dp[maxMove - 1][startRow][startColumn] % (10**9 + 7)