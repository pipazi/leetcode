import functools


class Solution:
    def isScramble(self, s1: str, s2: str) -> bool:
        @functools.lru_cache()
        def dfs(str1, str2):
            if str1 == str2:
                return True
            for ch in set(str1):
                if str1.count(ch) != str2.count(ch):
                    return False
            for i in range(1, len(str1)):
                if dfs(str1[:i], str2[:i]) and dfs(str1[i:], str2[i:]):
                    return True
                if dfs(str1[:i], str2[-i:]) and dfs(str1[i:], str2[:-i]):
                    return True
            return False
        return dfs(s1, s2)
