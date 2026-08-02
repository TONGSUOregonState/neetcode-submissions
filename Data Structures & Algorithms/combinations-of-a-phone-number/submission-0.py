class Solution:
    def letterCombinations(self, digits: str) -> list[str]:
        # 边界情况:空字符串直接返回空列表
        if not digits:
            return []

        # 数字到字母的映射表(标准电话键盘)
        phone_map: dict[str, str] = {
            "2": "abc", "3": "def", "4": "ghi", "5": "jkl",
            "6": "mno", "7": "pqrs", "8": "tuv", "9": "wxyz"
        }

        result: list[str] = []

        def backtrack(index: int, path: list[str]) -> None:
            # 终止条件:path 长度等于 digits 长度,说明每一位都选完了
            if index == len(digits):
                result.append("".join(path))
                return

            # 当前这一位数字对应的所有可能字母
            possible_letters = phone_map[digits[index]]

            for letter in possible_letters:
                path.append(letter)              # 做选择:把字母加入路径
                backtrack(index + 1, path)        # 递归:处理下一位数字
                path.pop()                        # 撤销选择:为下一次循环做准备(回溯)

        backtrack(0, [])
        return result