#!/usr/bin/env python3
import sys

def solve() -> None:
    data = sys.stdin.read().strip().split()
    if not data:
        return
    it = iter(data)
    n = int(next(it))
    m = int(next(it))
    adj = [[] for _ in range(n)]
    for _ in range(m):
        u = int(next(it)) - 1
        v = int(next(it)) - 1
        adj[u].append(v)
        adj[v].append(u)

    color = [0] * n
    found = False

    def dfs(i: int) -> bool:
        nonlocal found
        if i == n:
            found = True
            return True
        for c in (1, 2, 3):
            conflict = False
            for nb in adj[i]:
                if nb < i and color[nb] == c:
                    conflict = True
                    break
            if not conflict:
                color[i] = c
                if dfs(i + 1):
                    return True
                color[i] = 0
        return False

    if dfs(0):
        print("YES")
        print(' '.join(str(color[i]) for i in range(n)))
    else:
        print("NO")

if __name__ == "__main__":
    solve()