import functools

class Solution:
    def isInterleave(self, s1: str, s2: str, s3: str) -> bool:
        s1_len = len(s1)
        s2_len = len(s2)

        @functools.lru_cache()
        def dfs(left, loc1, loc2):
            if left:
                if loc1 <= s1_len - 1 and left[0] == s1[loc1]:
                    if dfs(left[1:], loc1 + 1, loc2):
                        return True
                if loc2 <= s2_len - 1 and left[0] == s2[loc2]:
                    if dfs(left[1:], loc1, loc2 + 1):
                        return True
                else:
                    return False
            if loc1 == s1_len and loc2 == s2_len:
                return True
            else:
                return False
        return dfs(s3, 0, 0)
