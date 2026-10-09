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
    answer = [0] * (n + 1)

    for start in range(1, n + 1):
        if colour[start] != -1:
            continue
        # BFS for this component
        q = deque([start])
        colour[start] = 0
        comp = [start]
        ok = True
        while q:
            v = q.popleft()
            cv = colour[v]
            for to in adj[v]:
                if colour[to] == -1:
                    colour[to] = cv ^ 1
                    q.append(to)
                    comp.append(to)
                elif colour[to] == cv:
                    # conflict -> not bipartite
                    print("NO")
                    return
        # choose orientation for lexicographically smallest result
        first = min(comp)
        if colour[first] == 0:
            map0, map1 = 1, 2
        else:
            map0, map1 = 2, 1
        for v in comp:
            answer[v] = map0 if colour[v] == 0 else map1

    # all components processed without conflict
    print("YES")
    sys.stdout.write(' '.join(str(answer[i]) for i in range(1, n + 1)))

if __name__ == "__main__":
    solve()