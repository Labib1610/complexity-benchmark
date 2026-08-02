import sys
from collections import deque

def solve() -> None:
    data = sys.stdin.buffer.read().split()
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

    color = [-1] * n  # -1 unvisited, 0 or 1

    for start in range(n):
        if color[start] != -1:
            continue
        # BFS for this component, start with color 0
        q = deque([start])
        color[start] = 0
        while q:
            u = q.popleft()
            cu = color[u]
            for v in adj[u]:
                cv = color[v]
                if cv == -1:
                    color[v] = cu ^ 1
                    q.append(v)
                elif cv == cu:
                    print("NO")
                    return

    # Build result: 1 for color 0, 2 for color 1
    res = ['1' if c == 0 else '2' for c in color]
    print("YES")
    print(' '.join(res))

if __name__ == "__main__":
    solve()