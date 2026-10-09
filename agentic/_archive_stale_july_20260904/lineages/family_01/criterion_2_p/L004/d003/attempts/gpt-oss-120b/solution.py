import sys
from collections import deque

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

    color = [-1] * n          # -1 unvisited, 0 -> band 1, 1 -> band 2
    for start in range(n):
        if color[start] != -1:
            continue
        # start new component, assign smallest possible (band 1) to this vertex
        color[start] = 0
        q = deque([start])
        while q:
            v = q.popleft()
            cv = color[v]
            for to in adj[v]:
                if color[to] == -1:
                    color[to] = cv ^ 1
                    q.append(to)
                elif color[to] == cv:
                    print("NO")
                    return

    # all good
    print("YES")
    res = ['1' if c == 0 else '2' for c in color]
    print(' '.join(res))

if __name__ == "__main__":
    solve()