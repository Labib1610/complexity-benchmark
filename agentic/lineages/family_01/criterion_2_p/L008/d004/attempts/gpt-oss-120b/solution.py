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

    colour = [-1] * (n + 1)          # -1 unvisited, 0/1 colours
    ans = [0] * (n + 1)

    for start in range(1, n + 1):
        if colour[start] != -1:
            continue
        # BFS this component
        q = deque([start])
        colour[start] = 0
        comp = [start]
        while q:
            v = q.popleft()
            cv = colour[v]
            for to in adj[v]:
                if colour[to] == -1:
                    colour[to] = cv ^ 1
                    q.append(to)
                    comp.append(to)
                elif colour[to] == cv:
                    print("NO")
                    return
        # decide orientation: give shift 1 to colour of smallest vertex
        min_v = min(comp)
        if colour[min_v] == 0:
            for x in comp:
                ans[x] = 1 if colour[x] == 0 else 2
        else:
            for x in comp:
                ans[x] = 1 if colour[x] == 1 else 2

    # all components processed
    print("YES")
    sys.stdout.write(' '.join(str(ans[i]) for i in range(1, n + 1)))

if __name__ == "__main__":
    solve()