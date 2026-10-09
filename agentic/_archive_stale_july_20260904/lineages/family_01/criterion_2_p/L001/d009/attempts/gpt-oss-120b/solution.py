import sys
from collections import deque

def solve() -> None:
    data = list(map(int, sys.stdin.buffer.read().split()))
    if not data:
        return
    it = iter(data)
    n = next(it)
    m = next(it)

    adj = [[] for _ in range(n)]
    for _ in range(m):
        u = next(it) - 1
        v = next(it) - 1
        if u == v:          # self‑loop -> impossible
            print("NO")
            return
        adj[u].append(v)
        adj[v].append(u)

    colour = [-1] * n          # -1 = unvisited, else 0/1
    ans = [0] * n

    for start in range(n):
        if colour[start] != -1:
            continue
        # BFS of this component
        q = deque([start])
        colour[start] = 0
        comp = [start]

        while q:
            v = q.popleft()
            cv = colour[v]
            for nb in adj[v]:
                if colour[nb] == -1:
                    colour[nb] = cv ^ 1
                    q.append(nb)
                    comp.append(nb)
                elif colour[nb] == cv:
                    print("NO")
                    return

        # smallest index in component = start (because we iterate increasingly)
        p = min(comp)          # defensive, actually equals start
        col_p = colour[p]
        for v in comp:
            ans[v] = 1 if colour[v] == col_p else 2

    print("YES")
    print(' '.join(map(str, ans)))

if __name__ == "__main__":
    solve()