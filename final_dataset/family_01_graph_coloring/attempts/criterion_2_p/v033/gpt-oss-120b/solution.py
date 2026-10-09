import sys
sys.setrecursionlimit(1 << 25)

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

    colour = [-1] * (n + 1)          # 0 or 1
    comp_vertices = []               # temporary list for current component
    from collections import deque

    for start in range(1, n + 1):
        if colour[start] != -1:
            continue
        # BFS this component
        q = deque([start])
        colour[start] = 0
        comp_vertices.clear()
        comp_vertices.append(start)
        ok = True
        while q:
            u = q.popleft()
            cu = colour[u]
            for v in adj[u]:
                if colour[v] == -1:
                    colour[v] = 1 - cu
                    q.append(v)
                    comp_vertices.append(v)
                elif colour[v] == cu:
                    # conflict -> not bipartite
                    print("NO")
                    return
        # make smallest index vertex colour 0 (shift 1)
        min_v = min(comp_vertices)
        if colour[min_v] == 1:
            # flip whole component
            for v in comp_vertices:
                colour[v] ^= 1

    # all good
    out = ['YES']
    shifts = [str(colour[i] + 1) for i in range(1, n + 1)]
    out.append(' '.join(shifts))
    sys.stdout.write('\n'.join(out))

if __name__ == "__main__":
    solve()