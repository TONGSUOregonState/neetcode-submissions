import heapq

class MedianFinder:
    def __init__(self):
        # small: 大顶堆(存较小的一半),Python heapq是小顶堆,
        # 所以存负数来模拟大顶堆
        self.small: list[int] = []
        # large: 小顶堆(存较大的一半),直接用heapq原生小顶堆
        self.large: list[int] = []

    def addNum(self, num: int) -> None:
        # 1. 先无脑丢进small(注意取负号)
        heapq.heappush(self.small, -num)

        # 2. 把small的最大值"倒"进large,保证 small中所有数 <= large中所有数
        val = -heapq.heappop(self.small)
        heapq.heappush(self.large, val)

        # 3. 平衡大小:让small的元素数 >= large的元素数(最多多1个)
        if len(self.large) > len(self.small):
            val = heapq.heappop(self.large)
            heapq.heappush(self.small, -val)

    def findMedian(self) -> float:
        if len(self.small) > len(self.large):
            return float(-self.small[0])
        return (-self.small[0] + self.large[0]) / 2.0