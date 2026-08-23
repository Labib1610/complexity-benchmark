#!/usr/bin/env python3
import sys
sys.setrecursionlimit(10000)

def main():
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

    allowed = [0b111] * n  # bitmask of allowed colors
    colors = [0] * n
    solution = None
    found = False

    def dfs(idx):
        nonlocal found, solution
        if found:
            return
        if idx == n:
            found = True
            solution = colors[:]
            return
        for color in (1, 2, 3):
            bit = 1 << (color - 1)
            if not (allowed[idx] & bit):
                continue
            # assign
            colors[idx] = color
            changes = []
            ok = True
            for nb in adj[idx]:
                if colors[nb] == 0:
                    prev = allowed[nb]
                    if prev & bit:
                        allowed[nb] = prev & ~bit
                        changes.append((nb, prev))
                        if allowed[nb] == 0:
                            ok = False
                            break
            if ok:
                dfs(idx + 1)
            # revert
            for nb, prev in changes:
                allowed[nb] = prev
            colors[idx] = 0
            if found:
                return

    dfs(0)
    out = sys.stdout
    if not found:
        out.write("NO\n")
    else:
        out.write("YES\n")
        out.write(' '.join(map(str, solution)))
        out.write('\n')

if __name__ == "__main__":
    main()