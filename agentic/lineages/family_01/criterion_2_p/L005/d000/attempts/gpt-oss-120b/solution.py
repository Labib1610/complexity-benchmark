import sys
sys.setrecursionlimit(1 << 25)

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

    color = [ -1 ] * (n + 1)          # parity 0/1 for bipartition, -1 = unvisited
    ans = [0] * (n + 1)               # final schedule 1/2

    from collections import deque

    for start in range(1, n + 1):
        if color[start] != -1:
            continue
        # BFS this component
        q = deque([start])
        color[start] = 0
        comp = [start]
        min_node = start
        while q:
            v = q.popleft()
            if v < min_node:
                min_node = v
            for to in g[v]:
                if color[to] == -1:
                    color[to] = color[v] ^ 1
                    q.append(to)
                    comp.append(to)
                elif color[to] == color[v]:
                    print("NO")
                    return
        # decide which parity gets schedule 1
        parity_min = color[min_node]          # parity that should become 1
        for v in comp:
            ans[v] = 1 if color[v] == parity_min else 2

    print("YES")
    print(' '.join(str(ans[i]) for i in range(1, n + 1)))

if __name__ == "__main__":
    solve()