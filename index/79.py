"""
79 单词搜索
"""
from collections import Counter


class Solution:
    def exist(self, board, word):
        m = len(board)
        if not m:
            return False
        n = len(board[0])

        ans = []
        for b in board:
            ans += b
        need = Counter(word)
        ans = Counter(ans)
        for k, v in need.items():
            if v > ans[k]:
                return False

        l = len(word)
        used = [[False] * n for _ in range(m)]
        bias = [(-1, 0), (1, 0), (0, -1), (0, 1)]

        def dfs(c, r, location):
            nonlocal used
            flag = False
            if board[c][r] == word[location]:
                if location == l - 1:
                    return True
                used[c][r] = True
                for dx, dy in bias:
                    x, y = c + dx, r + dy
                    if x < 0 or x >= m or y < 0 or y >= n:
                        continue
                    if not used[x][y]:
                        flag = flag or dfs(x, y, location + 1)
                used[c][r] = False
            return flag

        for i in range(m):
            for j in range(n):
                if dfs(i, j, 0):
                    return True
        return False
