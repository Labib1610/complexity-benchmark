import sys
from collections import deque

def solve() -> None:
    data = list(map(int, sys.stdin.read().split()))
    if not data:
        return
    it = iter(data)
    n = next(it)
    m = next(it)
    adj = [[] for _ in range(n + 1)]
    for _ in range(m):
        u = next(it)
        v = next(it)
        adj[u].append(v)
        adj[v].append(u)

    color = [-1] * (n + 1)  # -1 uncolored, 0/1 bipartite colors

    for start in range(1, n + 1):
        if color[start] != -1:
            continue
        # start new component with color 0
        color[start] = 0
        q = deque([start])
        while q:
            u = q.popleft()
            cu = color[u]
            for w in adj[u]:
                if color[w] == -1:
                    color[w] = 1 - cu
                    q.append(w)
                elif color[w] == cu:
                    print("NO")
                    return

    # mapping 0 -> 1, 1 -> 2 gives lexicographically smallest
    res = ['1' if c == 0 else '2' for c in color[1:]]
    print("YES")
    print(' '.join(res))

if __name__ == "__main__":
    solve()