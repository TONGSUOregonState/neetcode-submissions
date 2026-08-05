class Solution:
    def searchRange(self, nums: list[int], target: int) -> list[int]:
        def lower_bound(target: int) -> int:
            # 找第一个 >= target 的下标
            lo, hi = 0, len(nums)
            while lo < hi:
                mid = (lo + hi) // 2
                if nums[mid] >= target:
                    hi = mid       # mid 可能是答案，收缩右边界
                else:
                    lo = mid + 1   # mid 太小，排除
            return lo

        left = lower_bound(target)
        # target 不存在的情况：越界，或者该位置的值不等于 target
        if left == len(nums) or nums[left] != target:
            return [-1, -1]

        # 右边界 = 第一个 >= target+1 的下标 - 1
        right = lower_bound(target + 1) - 1
        return [left, right]