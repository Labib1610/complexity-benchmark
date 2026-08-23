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
    neigh = [set() for _ in range(n)]
    for _ in range(m):
        u = int(next(it)) - 1
        v = int(next(it)) - 1
        if u == v:
            continue
        neigh[u].add(v)
        neigh[v].add(u)

    color = [0] * n          # 0 = uncolored, 1-3 = color
    domain = [0b111] * n     # bitmask of possible colors for each node

    solution = None

    def dfs(k):
        nonlocal solution
        if k == n:
            solution = color[:]
            return True
        # try colors 1..3
        for c in (1, 2, 3):
            # check conflict with already colored neighbors
            conflict = False
            for nb in neigh[k]:
                if color[nb] == c:
                    conflict = True
                    break
            if conflict:
                continue
            # assign
            color[k] = c
            changes = []
            fail = False
            # forward-checking: update domains of uncolored neighbors
            for nb in neigh[k]:
                if color[nb] == 0:
                    old = domain[nb]
                    new = old & (~(1 << (c - 1)))
                    if new == 0:
                        fail = True
                        break
                    if new != old:
                        changes.append((nb, old))
                        domain[nb] = new
            if not fail:
                if dfs(k + 1):
                    return True
            # revert
            for nb, old in reversed(changes):
                domain[nb] = old
            color[k] = 0
        return False

    if dfs(0):
        print("YES")
        print(' '.join(str(x) for x in solution))
    else:
        print("NO")

if __name__ == "__main__":
    main()