class Solution:
    def lengthOfLIS(self, nums: List[int]) -> int:
        n=len(nums)
        dp=[0]*n
        dp[0]=1
        for i in range(1,n):
            maxi=0
            for j in range(i):
                if nums[i]>nums[j]:
                    maxi=max(maxi,dp[j])
            dp[i]+=maxi+1
        return max(dp)
                    



        