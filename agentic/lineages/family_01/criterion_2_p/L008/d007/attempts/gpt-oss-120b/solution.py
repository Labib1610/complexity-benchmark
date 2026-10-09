import sys
sys.setrecursionlimit(1 << 25)

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
        if u == v:          # self‑loop -> impossible
            print("NO")
            return
        adj[u].append(v)
        adj[v].append(u)

    colour = [-1] * (n + 1)          # -1 unvisited, 0/1 bipartite colour
    ans = [0] * (n + 1)

    from collections import deque

    for start in range(1, n + 1):
        if colour[start] != -1:
            continue
        # BFS this component
        q = deque([start])
        colour[start] = 0
        comp = [start]
        while q:
            v = q.popleft()
            for to in adj[v]:
                if colour[to] == -1:
                    colour[to] = colour[v] ^ 1
                    q.append(to)
                    comp.append(to)
                elif colour[to] == colour[v]:
                    print("NO")
                    return
        # decide mapping to 1/2
        v_min = min(comp)
        if colour[v_min] == 0:
            map0, map1 = 1, 2
        else:
            map0, map1 = 2, 1
        for v in comp:
            ans[v] = map0 if colour[v] == 0 else map1

    print("YES")
    print(' '.join(str(ans[i]) for i in range(1, n + 1)))

if __name__ == "__main__":
    solve()