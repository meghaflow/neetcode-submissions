class Solution:
    def rob(self, nums: List[int]) -> int:
        if len(nums)==1:
            return max(0,nums[0])
        def f(nums):
            n=len(nums)
            if n==0:
                return 0
            dp=[0]*n
            dp[0]=nums[0]
            if n<=1:
                return max(nums[0],0)
            dp[1]=max(nums[0],nums[1])
            for i in range(2,n):
                dp[i]=max(dp[i-1],dp[i-2]+nums[i])
            return dp[n-1]
        return max(f(nums[:-1]),f(nums[1:]))


        