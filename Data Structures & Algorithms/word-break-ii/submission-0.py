class Solution:
    def wordBreak(self, s: str, wordDict: List[str]) -> List[str]:

        word_set = set(wordDict)
        memo = {}
        
        def backtrack(start:int):
            #Termination condition
            if start == len(s):
                return [""]
            if start in memo:
                return memo[start] 
            
            result = []
            
            for end in range(start+1, len(s)+1):
                word = s[start:end]
                if word in word_set:
                    for rest in backtrack(end):

                        if end == len(s):
                            result.append(word)
                        else:
                            result.append(word + " " + rest) 
            memo[start] = result
            return result
        return backtrack(0)
