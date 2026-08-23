#!/usr/bin/env python3
import sys
sys.setrecursionlimit(10000)

def solve():
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

    colors = [0] * n
    found = False

    def dfs(idx):
        nonlocal found
        if found:
            return
        if idx == n:
            found = True
            return
        for c in (1,2,3):
            conflict = False
            for nb in adj[idx]:
                if nb < idx and colors[nb] == c:
                    conflict = True
                    break
            if conflict:
                continue
            colors[idx] = c
            dfs(idx+1)
            if found:
                return
            colors[idx] = 0

    dfs(0)
    out = []
    if not found:
        out.append("NO")
    else:
        out.append("YES")
        out.append(' '.join(str(colors[i]) for i in range(n)))
    sys.stdout.write('\n'.join(out))

if __name__ == "__main__":
    solve()