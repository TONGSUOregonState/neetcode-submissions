class Solution:
    def minSubArrayLen(self, target: int, nums: List[int]) -> int:
        ans = float('inf')
        total = 0
        left = 0
        for right in range(len(nums)):
            total += nums[right]
            
            while total >= target:
                ans = min(ans,right-left+1)
                total -= nums[left]
                left += 1
                
        return ans if ans != float('inf') else 0