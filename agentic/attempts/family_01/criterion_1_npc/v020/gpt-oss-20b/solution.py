#!/usr/bin/env python3
import sys
sys.setrecursionlimit(10000)

def main():
    data = sys.stdin.read().strip().split()
    if not data:
        return
    it = iter(data)
    n = int(next(it)); m = int(next(it))
    adj = [[] for _ in range(n)]
    for _ in range(m):
        u = int(next(it)) - 1
        v = int(next(it)) - 1
        if v not in adj[u]:
            adj[u].append(v)
            adj[v].append(u)

    allowed = [7] * n  # bits 0,1,2 correspond to colors 1,2,3
    color = [0] * n    # 0 unassigned

    def dfs(idx):
        if idx == n:
            return True
        node = idx
        if allowed[node] == 0:
            return False
        for c in range(1, 4):
            if not (allowed[node] & (1 << (c - 1))):
                continue
            # check conflict with already colored neighbors
            conflict = False
            for nb in adj[node]:
                if color[nb] == c:
                    conflict = True
                    break
            if conflict:
                continue
            color[node] = c
            changes = []
            bad = False
            bit = 1 << (c - 1)
            for nb in adj[node]:
                if color[nb] == 0:
                    old = allowed[nb]
                    new = old & ~bit
                    if new != old:
                        allowed[nb] = new
                        changes.append((nb, old))
                        if new == 0:
                            bad = True
                            break
            if not bad and dfs(idx + 1):
                return True
            # revert
            for nb, old in changes:
                allowed[nb] = old
            color[node] = 0
        return False

    if dfs(0):
        out = ['YES', ' '.join(str(col) for col in color)]
    else:
        out = ['NO']
    sys.stdout.write('\n'.join(out))

if __name__ == "__main__":
    main()