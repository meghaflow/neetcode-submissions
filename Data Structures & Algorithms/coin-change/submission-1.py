class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:
        n=len(coins)
        dp=[float('inf')]*(amount+1)
        dp[0]=0
        for i in range(amount+1):
            for j in range(n):
                if coins[j]<=i and dp[i-coins[j]]<float('inf'):
                    dp[i]=min(dp[i],1+dp[i-coins[j]])
        return dp[amount] if dp[amount]!=float('inf') else -1

        