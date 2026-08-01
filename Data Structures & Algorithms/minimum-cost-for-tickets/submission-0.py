class Solution:
    def mincostTickets(self, days: List[int], costs: List[int]) -> int:

        tdays = set(days)
        last_day = days[-1]
        dp = [float('inf')] * (last_day + 1)
        dp [0] = 0
        for i in range(1,last_day+1):
            if i in tdays:
                dp[i]  = min(
                    costs[0] + dp[max(0,i-1)],
                    costs[1] + dp[max(0,i-7)],
                    costs[2] + dp[max(0,i-30)],
                            )
            else:
                dp[i] = dp[i-1]
        return dp[last_day]
