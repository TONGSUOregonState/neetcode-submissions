class Solution:
    def __init__(self, w: List[int]):
        self.prefix = []              # 加上 self.
        total = 0
        for weight in w:
            total += weight
            self.prefix.append(total)
        self.total = total            # 加上 self.，存起来给pickIndex用

    def pickIndex(self) -> int:
        target = random.randint(1, self.total)   # target挪到这里，每次调用都重新生成
        
        left, right = 0, len(self.prefix) - 1
        while left < right:
            mid = (left + right) // 2
            if self.prefix[mid] < target:
                left = mid + 1
            else:
                right = mid
        return left