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
    ans = [0] * (n + 1)              # final values (1-indexed)

    for start in range(1, n + 1):
        if colour[start] != -1:
            continue
        # BFS this component
        q = deque([start])
        colour[start] = 0
        comp = [start]
        ok = True
        while q:
            u = q.popleft()
            cu = colour[u]
            for v in adj[u]:
                if colour[v] == -1:
                    colour[v] = cu ^ 1
                    q.append(v)
                    comp.append(v)
                elif colour[v] == cu:
                    print("NO")
                    return
        # decide mapping to values 1/2
        r = min(comp)               # smallest index in component
        # side containing r gets value 1
        side_one = colour[r]        # colour that will be mapped to 1
        for v in comp:
            ans[v] = 1 if colour[v] == side_one else 2

    # all components processed without conflict
    print("YES")
    print(' '.join(str(ans[i]) for i in range(1, n + 1)))

if __name__ == "__main__":
    solve()