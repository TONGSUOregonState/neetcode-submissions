from typing import List

class Solution:
    def wordBreak(self, s: str, wordDict: List[str]) -> List[str]:
        wordDict = set(wordDict)
        memo: dict[int, List[str]] = {}

        def backtrack(start: int) -> List[str]:
            if start in memo:
                return memo[start]
            if start == len(s):
                return [""]          # 代表“没有剩余部分需要拼接”

            sentences = []
            for end in range(start + 1, len(s) + 1):
                word = s[start:end]
                if word in wordDict:
                    for sub in backtrack(end):
                        # sub 为空字符串说明 word 已经是句尾，不需要加空格
                        sentences.append(word if sub == "" else word + " " + sub)

            memo[start] = sentences
            return sentences

        return backtrack(0)