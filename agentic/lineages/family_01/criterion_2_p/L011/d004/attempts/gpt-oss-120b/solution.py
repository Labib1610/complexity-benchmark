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
        adj[u].append(v)
        adj[v].append(u)

    color = [-1] * (n + 1)          # 0/1 bipartite colors
    comp_id = [-1] * (n + 1)
    comps = []                     # list of (vertices list, min_vertex)
    from collections import deque

    for start in range(1, n + 1):
        if color[start] != -1:
            continue
        # BFS this component
        q = deque([start])
        color[start] = 0
        comp_vertices = [start]
        ok = True
        while q:
            u = q.popleft()
            for v in adj[u]:
                if color[v] == -1:
                    color[v] = color[u] ^ 1
                    q.append(v)
                    comp_vertices.append(v)
                elif color[v] == color[u]:
                    print("NO")
                    return
        min_v = min(comp_vertices)
        comps.append((comp_vertices, min_v))

    # decide orientation per component
    result = [0] * (n + 1)
    for verts, min_v in comps:
        # if min_v currently has color 0, keep; else flip
        flip = 1 if color[min_v] == 1 else 0
        for v in verts:
            final = color[v] ^ flip
            result[v] = 1 if final == 0 else 2

    # output
    print("YES")
    print(' '.join(str(result[i]) for i in range(1, n + 1)))

if __name__ == "__main__":
    solve()