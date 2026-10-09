import sys
from collections import deque

def solve() -> None:
    data = sys.stdin.buffer.read().split()
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
            x = q.popleft()
            comp.append(x)
            for y in adj[x]:
                if colour[y] == -1:
                    colour[y] = colour[x] ^ 1
                    q.append(y)
                elif colour[y] == colour[x]:
                    sys.stdout.write("NO")
                    return
        # decide mapping to get smallest lexicographic
        p = min(comp)
        if colour[p] == 0:
            map0, map1 = 1, 2
        else:
            map0, map1 = 2, 1
        for v in comp:
            ans[v] = map0 if colour[v] == 0 else map1

    out = ["YES", " ".join(str(ans[i]) for i in range(1, n + 1))]
    sys.stdout.write("\n".join(out))

if __name__ == "__main__":
    solve()