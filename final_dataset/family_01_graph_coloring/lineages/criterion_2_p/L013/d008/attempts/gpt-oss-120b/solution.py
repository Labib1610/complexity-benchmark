import sys
sys.setrecursionlimit(1 << 25)

def solve() -> None:
    data = sys.stdin.read().strip().split()
    if not data:
        return
    it = iter(data)
    n = int(next(it))
    m = int(next(it))
    adj = [[] for _ in range(n)]
    for _ in range(m):
        u = int(next(it)) - 1
        v = int(next(it)) - 1
        adj[u].append(v)
        adj[v].append(u)

    color = [-1] * n          # 0 or 1
    res = [2] * n             # default 2
    from collections import deque

    for start in range(n):
        if color[start] != -1:
            continue
        # BFS this component
        q = deque([start])
        color[start] = 0
        comp_vertices = [start]
        ok = True
        while q:
            v = q.popleft()
            for to in adj[v]:
                if color[to] == -1:
                    color[to] = color[v] ^ 1
                    q.append(to)
                    comp_vertices.append(to)
                elif color[to] == color[v]:
                    print("NO")
                    return
        # decide which side gets price 1
        # side containing the smallest index gets 1
        min_idx = min(comp_vertices)
        side_one = color[min_idx]          # this color will be 1
        for v in comp_vertices:
            res[v] = 1 if color[v] == side_one else 2

    print("YES")
    print(' '.join(map(str, res)))

if __name__ == "__main__":
    solve()