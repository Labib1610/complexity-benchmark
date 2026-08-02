#!/usr/bin/env python3
import sys
import threading
import itertools

def solve() -> None:
    data = sys.stdin.read().strip().split()
    if not data:
        return
    it = iter(data)
    n = int(next(it))
    m = int(next(it))
    adj = [[] for _ in range(n + 1)]
    edge = [[False] * (n + 1) for _ in range(n + 1)]
    for _ in range(m):
        a = int(next(it))
        b = int(next(it))
        if a == b:
            continue
        adj[a].append(b)
        adj[b].append(a)
        edge[a][b] = edge[b][a] = True

    # Pre-check for 4-clique
    for a, b, c, d in itertools.combinations(range(1, n + 1), 4):
        if (edge[a][b] and edge[a][c] and edge[a][d] and
            edge[b][c] and edge[b][d] and edge[c][d]):
            print("NO")
            return

    colors = [0] * (n + 1)          # 0 unassigned, 1-3 assigned
    counts = [[0, 0, 0] for _ in range(n + 1)]  # counts[v][color] (# of colored neighbors with this color)
    solution = []

    sys.setrecursionlimit(10000)

    def dfs(idx: int) -> bool:
        if idx > n:
            # All vertices assigned
            solution.extend(colors[1:])  # store result
            return True

        # Try colors 1..3
        for c in range(3):  # c = 0,1,2
            # Conflict check
            conflict = False
            for w in adj[idx]:
                if colors[w] == c + 1:
                    conflict = True
                    break
            if conflict:
                continue

            # Assign
            colors[idx] = c + 1
            for w in adj[idx]:
                counts[w][c] += 1

            # Prune: check future uncolored vertices
            prune_ok = True
            for v in range(idx + 1, n + 1):
                if colors[v] == 0:
                    if all(counts[v][i] > 0 for i in range(3)):
                        prune_ok = False
                        break
            if prune_ok:
                if dfs(idx + 1):
                    return True

            # Revert
            for w in adj[idx]:
                counts[w][c] -= 1
            colors[idx] = 0

        return False

    if dfs(1):
        print("YES")
        print(' '.join(str(x) for x in solution))
    else:
        print("NO")

def main():
    solve()

if __name__ == "__main__":
    main()