import sys
from collections import deque

def solve() -> None:
    data = sys.stdin.read().strip().split()
    if not data:
        return
    it = iter(data)
    n = int(next(it))
    m = int(next(it))
    adj = [[] for _ in range(n + 1)]
    for _ in range(m):
        u = int(next(it)); v = int(next(it))
        if u == v:
            print("NO")
            return
        adj[u].append(v)
        adj[v].append(u)

    color = [ -1 ] * (n + 1)   # -1 unvisited, 0 -> state 1, 1 -> state 2
    for i in range(1, n + 1):
        if color[i] != -1:
            continue
        # start new component, give smallest index node state 1 (color 0)
        q = deque([i])
        color[i] = 0
        while q:
            u = q.popleft()
            cu = color[u]
            for v in adj[u]:
                if color[v] == -1:
                    color[v] = cu ^ 1
                    q.append(v)
                elif color[v] == cu:
                    print("NO")
                    return

    # all good
    print("YES")
    res = [str(1 if color[i] == 0 else 2) for i in range(1, n + 1)]
    print(' '.join(res))

if __name__ == "__main__":
    solve()