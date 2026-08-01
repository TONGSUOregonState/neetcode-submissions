from collections import Counter
from typing import Dict


class Solution:
    def minWindow(self, s: str, t: str) -> str:
        if not s or not t:
            return ""

        # need：记录 t 中每个字符需要的数量（含重复）
        need: Dict[str, int] = Counter(t)
        # window：记录当前窗口中每个字符出现的数量
        window: Dict[str, int] = {}

        left, right = 0, 0
        valid = 0  # window中，已经有多少种字符达到了need要求的数量
        # 记录最小覆盖窗口的起点和长度
        start, min_len = 0, float('inf')

        while right < len(s):
            # 扩大窗口：把 s[right] 加入窗口
            c = s[right]
            right += 1
            if c in need:
                window[c] = window.get(c, 0) + 1
                if window[c] == need[c]:
                    valid += 1

            # 窗口已经满足条件（覆盖了t的所有字符，含重复），开始尝试收缩
            while valid == len(need):
                # 每次收缩前，先检查当前窗口是不是比之前记录的更短
                if right - left < min_len:
                    start = left
                    min_len = right - left

                # 收缩左边界
                d = s[left]
                left += 1
                if d in need:
                    if window[d] == need[d]:
                        valid -= 1
                    window[d] -= 1

        return "" if min_len == float('inf') else s[start:start + min_len]