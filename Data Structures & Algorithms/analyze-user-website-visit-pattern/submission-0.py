from collections import defaultdict, Counter
from itertools import combinations
from typing import List


class Solution:
    def mostVisitedPattern(
        self, username: List[str], timestamp: List[int], website: List[str]
    ) -> List[str]:

        # ------------------------------------------------------------------
        # 第一步:按用户分组
        # 用哈希表(defaultdict)把散落在三个数组里的记录,按"用户名"归类到一起
        # key = 用户名, value = 这个用户的所有 (timestamp, website) 记录
        # ------------------------------------------------------------------
        user_visits = defaultdict(list)
        for u, t, w in zip(username, timestamp, website):
            user_visits[u].append((t, w))  # O(1) 定位到 u 对应的桶,append 进去

        # ------------------------------------------------------------------
        # 第二步:每个用户内部按 timestamp 排序,得到"时间顺序访问序列"
        # 排序之后,时间戳这个"脚手架"就没用了,只保留网站名
        # ------------------------------------------------------------------
        user_sequence = {}
        for u, visits in user_visits.items():
            visits.sort(key=lambda pair: pair[0])        # 按时间戳(pair[0])排序
            user_sequence[u] = [w for _, w in visits]    # 只保留网站名(丢弃时间戳)

        # ------------------------------------------------------------------
        # 第三步:枚举每个用户的三元组模式,去重后累加到全局计数器
        #
        # combinations(seq, 3):
        #   枚举 seq 里所有"长度为3、保持相对顺序"的组合(组合数学,不是排列)
        #
        # set(...):
        #   对同一个用户去重 —— 因为同一用户即使重复走了同一个模式好几次,
        #   也只能贡献 1 票,不能重复计数
        #
        # pattern_count[pattern] += 1:
        #   全局哈希表(Counter)计数,O(1) 操作。
        #   不同用户之间会在这里持续累加,这就是"多个用户命中同一模式"
        #   得以被正确记录、累加变高的地方
        # ------------------------------------------------------------------
        pattern_count = Counter()

        for u, seq in user_sequence.items():
            # 该用户去重后、真正各不相同的模式集合(set 本身只负责去重,不计数)
            distinct_patterns_for_user = set(combinations(seq, 3))

            # 把这个用户贡献的每个不同模式,各自在全局计数器里 +1
            for pattern in distinct_patterns_for_user:
                pattern_count[pattern] += 1

        # ------------------------------------------------------------------
        # 第四步:找出得分最高、且字典序最小的模式
        #
        # key=lambda x: (-x[1], x[0])
        #   -x[1]:次数取负数,这样用 min() 就能找到"次数最大"的那个
        #   x[0]:如果次数打平了,再按模式本身的字典序取最小的
        # ------------------------------------------------------------------
        best_pattern = min(pattern_count.items(), key=lambda x: (-x[1], x[0]))

        return list(best_pattern[0])
