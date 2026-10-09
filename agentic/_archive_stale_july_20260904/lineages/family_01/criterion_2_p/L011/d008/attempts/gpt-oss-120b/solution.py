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
        adj[u].append(v)
        adj[v].append(u)

    colour = [-1] * (n + 1)          # -1 unvisited, 0/1 bipartite colour
    ans = [0] * (n + 1)

    for start in range(1, n + 1):
        if colour[start] != -1:
            continue
        # BFS this component
        q = deque([start])
        colour[start] = 0
        comp = []
        while q:
            v = q.popleft()
            comp.append(v)
            cv = colour[v]
            for to in adj[v]:
                if colour[to] == -1:
                    colour[to] = cv ^ 1
                    q.append(to)
                elif colour[to] == cv:
                    print("NO")
                    return
        # orientation: smallest index gets value 1
        vmin = min(comp)
        if colour[vmin] == 0:
            for v in comp:
                ans[v] = 1 if colour[v] == 0 else 2
        else:
            for v in comp:
                ans[v] = 2 if colour[v] == 0 else 1

    # all done
    print("YES")
    print(' '.join(str(ans[i]) for i in range(1, n + 1)))

if __name__ == "__main__":
    solve()