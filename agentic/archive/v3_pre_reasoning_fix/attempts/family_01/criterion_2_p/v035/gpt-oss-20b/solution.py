import sys
from collections import deque

def solve() -> None:
    data = list(map(int, sys.stdin.buffer.read().split()))
    if not data:
        return
    it = iter(data)
    n = next(it)
    m = next(it)
    g = [[] for _ in range(n)]
    for _ in range(m):
        u = next(it) - 1
        v = next(it) - 1
        g[u].append(v)
        g[v].append(u)

    color = [-1] * n          # 0 or 1 for bipartite coloring
    shift = [0] * n           # final assignment 1 or 2
    for i in range(n):
        if color[i] != -1:
            continue
        q = deque([i])
        color[i] = 0
        comp = [i]
        min_idx = i
        while q:
            v = q.popleft()
            for nb in g[v]:
                if color[nb] == -1:
                    color[nb] = color[v] ^ 1
                    q.append(nb)
                    comp.append(nb)
                    if nb < min_idx:
                        min_idx = nb
                elif color[nb] == color[v]:
                    print("NO")
                    return

        # choose orientation giving 1 at the smallest index
        if color[min_idx] == 0:
            for v in comp:
                shift[v] = 1 if color[v] == 0 else 2
        else:
            for v in comp:
                shift[v] = 2 if color[v] == 0 else 1

    print("YES")
    print(' '.join(map(str, shift)))

if __name__ == "__main__":
    solve()