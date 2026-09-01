import sys
from functools import lru_cache

def solve():
    data = sys.stdin.read().split()
    if not data:
        return
    it = iter(data)
    n = int(next(it))
    m = int(next(it))
    adj = [0] * (n + 1)
    for _ in range(m):
        u = int(next(it))
        v = int(next(it))
        adj[u] |= 1 << v
        adj[v] |= 1 << u

    full = (1 << (n + 1)) - 1

    @lru_cache(maxsize=None)
    def dfs(pos, used1, used2, used3):
        if pos > n:
            return True
        mask = adj[pos]
        for color in (1, 2, 3):
            if color == 1:
                if used1 & mask:
                    continue
                if dfs(pos + 1, used1 | (1 << pos), used2, used3):
                    return True
            elif color == 2:
                if used2 & mask:
                    continue
                if dfs(pos + 1, used1, used2 | (1 << pos), used3):
                    return True
            else:
                if used3 & mask:
                    continue
                if dfs(pos + 1, used1, used2, used3 | (1 << pos)):
                    return True
        return False

    if not dfs(1, 0, 0, 0):
        print("NO")
        return

    dfs.cache_clear()

    used1 = 0
    used2 = 0
    used3 = 0
    ans = []
    for pos in range(1, n + 1):
        mask = adj[pos]
        placed = False
        for color in (1, 2, 3):
            if color == 1:
                if used1 & mask:
                    continue
                if dfs(pos + 1, used1 | (1 << pos), used2, used3):
                    used1 |= 1 << pos
                    ans.append(1)
                    placed = True
                    break
            elif color == 2:
                if used2 & mask:
                    continue
                if dfs(pos + 1, used1, used2 | (1 << pos), used3):
                    used2 |= 1 << pos
                    ans.append(2)
                    placed = True
                    break
            else:
                if used3 & mask:
                    continue
                if dfs(pos + 1, used1, used2, used3 | (1 << pos)):
                    used3 |= 1 << pos
                    ans.append(3)
                    placed = True
                    break
        if not placed:
            print("NO")
            return

    print("YES")
    print(" ".join(map(str, ans)))

solve()