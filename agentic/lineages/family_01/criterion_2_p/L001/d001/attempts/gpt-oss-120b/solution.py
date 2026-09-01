import sys
from collections import deque

def solve() -> None:
    data = sys.stdin.read().strip().split()
    if not data:
        return
    it = iter(data)
    n = int(next(it))
    m = int(next(it))

    g = [[] for _ in range(n + 1)]
    for _ in range(m):
        u = int(next(it)); v = int(next(it))
        g[u].append(v)
        g[v].append(u)

    colour = [-1] * (n + 1)          # -1 unvisited, 0/1 bipartite colour
    ans = [0] * (n + 1)

    for start in range(1, n + 1):
        if colour[start] != -1:
            continue
        # BFS this component
        q = deque([start])
        colour[start] = 0
        comp = [start]
        while q:
            x = q.popleft()
            cx = colour[x]
            for y in g[x]:
                if colour[y] == -1:
                    colour[y] = cx ^ 1
                    q.append(y)
                    comp.append(y)
                elif colour[y] == cx:
                    print("NO")
                    return
        # decide orientation
        min_v = min(comp)
        if colour[min_v] == 0:
            for v in comp:
                ans[v] = 1 if colour[v] == 0 else 2
        else:
            for v in comp:
                ans[v] = 1 if colour[v] == 1 else 2

    # all done
    print("YES")
    sys.stdout.write(' '.join(str(ans[i]) for i in range(1, n + 1)))

if __name__ == "__main__":
    solve()