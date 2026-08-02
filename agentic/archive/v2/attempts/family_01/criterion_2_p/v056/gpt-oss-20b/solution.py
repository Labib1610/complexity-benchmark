import sys
from collections import deque

def solve() -> None:
    data = list(map(int, sys.stdin.buffer.read().split()))
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

    color = [-1] * (n + 1)   # -1 unvisited, 0/1 colors
    ans = [0] * (n + 1)
    visited = [False] * (n + 1)

    for start in range(1, n + 1):
        if color[start] != -1:
            continue
        # BFS for component
        comp = []
        q = deque([start])
        color[start] = 0
        comp.append(start)
        while q:
            u = q.popleft()
            for v in adj[u]:
                if color[v] == -1:
                    color[v] = 1 - color[u]
                    q.append(v)
                    comp.append(v)
                elif color[v] == color[u]:
                    print("NO")
                    return
        # Determine orientation: make minimal vertex mode 1
        min_vertex = min(comp)
        if color[min_vertex] == 0:
            # orientation original
            for v in comp:
                ans[v] = color[v] + 1
        else:
            # orientation flipped
            for v in comp:
                ans[v] = 2 - (color[v] + 1)
    # All components processed
    print("YES")
    print(' '.join(str(ans[i]) for i in range(1, n + 1)))

if __name__ == "__main__":
    solve()