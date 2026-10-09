import sys
from collections import deque

def solve() -> None:
    data = sys.stdin.read().strip().split()
    if not data:
        return
    it = iter(data)
    n = int(next(it))
    m = int(next(it))
    g = [[] for _ in range(n)]
    for _ in range(m):
        u = int(next(it)) - 1
        v = int(next(it)) - 1
        g[u].append(v)
        g[v].append(u)

    color = [-1] * n          # 0 / 1 during BFS
    ans = [0] * n             # final protocols (1 or 2)
    visited = [False] * n

    # components will be processed in order of their minimal vertex
    for start in range(n):
        if color[start] != -1:
            continue
        # BFS this component
        q = deque([start])
        color[start] = 0
        comp = [start]
        ok = True
        while q:
            v = q.popleft()
            for to in g[v]:
                if color[to] == -1:
                    color[to] = color[v] ^ 1
                    q.append(to)
                    comp.append(to)
                elif color[to] == color[v]:
                    print("NO")
                    return
        # decide which coloring to use
        comp.sort()
        # candidate 1: color 0 -> protocol 1, color 1 -> 2
        # candidate 2: swapped
        better = 0  # 0 means cand1, 1 means cand2
        for v in comp:
            c = color[v]
            p1 = 1 if c == 0 else 2
            p2 = 2 if c == 0 else 1
            if p1 < p2:
                better = 0
                break
            if p2 < p1:
                better = 1
                break
        # apply chosen candidate
        for v in comp:
            c = color[v]
            ans[v] = 1 if (c == 0) ^ better else 2

    print("YES")
    print(' '.join(map(str, ans)))

if __name__ == "__main__":
    solve()