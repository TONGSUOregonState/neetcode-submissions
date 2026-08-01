class Solution:
    def largestSubmatrix(self, matrix: list[list[int]]) -> int:
        m, n = len(matrix), len(matrix[0])
        
        # height[j]: 第j列从当前行往上数,连续1的高度
        # 相当于给每一行都算出一组"柱子高度"
        height = [0] * n
        ans = 0

        for i in range(m):
            # 1. 更新这一行每一列的累积高度
            #    遇到0直接清零(连续性断了),遇到1就在上一行基础上+1
            for j in range(n):
                if matrix[i][j] == 0:
                    height[j] = 0
                else:
                    height[j] += 1

            # 2. 因为列可以任意重排,把这一行的高度降序排序
            #    排序后第k个位置(0-indexed为k-1)的高度,
            #    就是"选最高的k根柱子"能达到的最小高度(=矩形高度)
            sorted_height = sorted(height, reverse=True)

            # 3. 枚举宽度k(1到n),计算面积并更新答案
            #    宽度k → 用排在前k位的柱子,高度取决于第k根(最矮的那根)
            for k in range(1, n + 1):
                area = sorted_height[k - 1] * k
                ans = max(ans, area)

        return ans