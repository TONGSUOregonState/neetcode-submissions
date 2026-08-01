class Solution:
    def appendCharacters(self, s: str, t: str) -> int:
        i, j = 0, 0  # i 指向 s，j 指向 t
        n, m = len(s), len(t)
        
        while i < n and j < m:
            if s[i] == t[j]:
                j += 1  # t[j] 匹配上了，移动 t 的指针
            i += 1      # s 的指针总是移动
        
        # j 就是 t 中已经被匹配的字符数
        # 剩下 (m - j) 个字符需要追加
        return m - j