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

    color = [-1] * (n + 1)          # 0/1 temporary colors
    result = [0] * (n + 1)          # final 1/2 values
    from collections import deque

    for start in range(1, n + 1):
        if color[start] != -1:
            continue
        # BFS this component
        q = deque([start])
        color[start] = 0
        comp = [start]
        ok = True
        while q:
            v = q.popleft()
            for to in g[v]:
                if color[to] == -1:
                    color[to] = color[v] ^ 1
                    q.append(to)
                    comp.append(to)
                elif color[to] == color[v]:
                    print("NO")
                    return
        # decide orientation: smallest index gets final 1
        min_vertex = min(comp)
        if color[min_vertex] == 1:
            # flip whole component
            for v in comp:
                color[v] ^= 1
        # map to 1/2
        for v in comp:
            result[v] = 1 if color[v] == 0 else 2

    print("YES")
    print(' '.join(str(result[i]) for i in range(1, n + 1)))

if __name__ == "__main__":
    solve()