# 用1*2、2*3两种木板填充n*m的容器
given = [(1, 2), (2, 1), (2, 3), (3, 2)]


def aa(n=4, m=4):
    a = [[float("inf") for j in range(0, m+1)] for i in range(0, n+1)]
    for j in range(1, n + 1):
        for i in range(1, m + 1):
            q = float("inf")
            if (i, j) in given:
                q = 1
            else:
                for y, x in [(j, num) for num in range(1, i + 1)] + [(num, i) for num in range(1, j + 1)]:
                    if y == j:
                        v = a[j][i - x]
                    else:
                        v = a[j - y][i]
                    q = min(q, v + a[y][x])
            a[j][i] = q
    print(a)
    return False if a[n][m] == float("inf") else a[n][m]
