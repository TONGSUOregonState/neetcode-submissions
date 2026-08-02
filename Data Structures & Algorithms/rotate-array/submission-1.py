def reverse(nums: list[int], left: int, right: int) -> None:
    """原地反转 nums[left..right] 这个闭区间"""
    while left < right:
        # 交换两端元素
        nums[left], nums[right] = nums[right], nums[left]
        left += 1    # 左指针右移
        right -= 1   # 右指针左移


class Solution:
    def rotate(self, nums: list[int], k: int) -> None:
        n = len(nums)
        k %= n  # k 可能大于 n,取余(转一圈等于没转)

        # 数组切成两段: A = nums[0 .. n-k-1], B = nums[n-k .. n-1]
        # 目标 A+B → B+A,依据 B+A = reverse(reverse(A) + reverse(B))
        reverse(nums, 0, n - k - 1)   # 第一步: 反转 A
        reverse(nums, n - k, n - 1)   # 第二步: 反转 B
        reverse(nums, 0, n - 1)       # 第三步: 整体反转