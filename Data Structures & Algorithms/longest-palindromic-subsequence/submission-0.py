class Solution:
    def longestPalindromeSubseq(self, s: str) -> int:
        n = len(s)
        memo = {}

        def dp(i: int, j: int) -> int:
            if i > j:
                return 0          # 空区间
            if i == j:
                return 1          # 单字符
            if (i, j) in memo:
                return memo[(i, j)]

            if s[i] == s[j]:
                res = dp(i + 1, j - 1) + 2
            else:
                res = max(dp(i + 1, j), dp(i, j - 1))

            memo[(i, j)] = res
            return res

        return dp(0, n - 1)