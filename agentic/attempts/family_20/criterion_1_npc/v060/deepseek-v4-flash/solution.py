import sys
sys.setrecursionlimit(1000000)

def find_bridges(n, edges):
    g = [[] for _ in range(n)]
    for idx, (u, v) in enumerate(edges):
        g[u].append((v, idx))
        g[v].append((u, idx))
    
    visited = [False] * n
    tin = [-1] * n
    low = [-1] * n
    timer = [0]
    bridges = set()

    def dfs(v, p_edge):
        visited[v] = True
        tin[v] = low[v] = timer[0]
        timer[0] += 1
        for to, eid in g[v]:
            if eid == p_edge:
                continue
            if visited[to]:
                low[v] = min(low[v], tin[to])
            else:
                dfs(to, eid)
                low[v] = min(low[v], low[to])
                if low[to] > tin[v]:
                    bridges.add(eid)

    for i in range(n):
        if not visited[i]:
            dfs(i, -1)
    return bridges

def edge_color_cubic(n, edges):
    # construct adjacency with edge ids
    g = [[] for _ in range(n)]
    for idx, (u, v) in enumerate(edges):
        g[u].append((v, idx))
        g[v].append((u, idx))

    color = [-1] * len(edges)

    # Use Kempe chain recolor approach
    # Try to color greedily with 3 colors; if stuck, do chain recolor
    max_color = 3

    used_at_vertex = [set() for _ in range(n)]

    def get_free_color(vertex):
        for c in range(max_color):
            if c not in used_at_vertex[vertex]:
                return c
        return -1

    def swap_chain(v, c1, c2, prev_edge):
        # flip colors c1 & c2 along path from v
        stack = [(v, c1, c2, prev_edge)]
        while stack:
            vv, a, b, pe = stack.pop()
            # find edge with color a at vv and not pe
            for to, eid in g[vv]:
                if eid == pe:
                    continue
                if color[eid] == a:
                    color[eid] = b
                    used_at_vertex[vv].remove(a)
                    used_at_vertex[vv].add(b)
                    used_at_vertex[to].remove(a)
                    used_at_vertex[to].add(b)
                    stack.append((to, b, a, eid))
                    break

    for eid, (u, v) in enumerate(edges):
        cu = get_free_color(u)
        cv = get_free_color(v)
        if cu != -1 and (cu not in used_at_vertex[v] or cu == cv):
            if cu not in used_at_vertex[v]:
                color[eid] = cu
                used_at_vertex[u].add(cu)
                used_at_vertex[v].add(cu)
            else:
                # same color free at both? impossible since they both lack it
                color[eid] = cu
                used_at_vertex[u].add(cu)
                used_at_vertex[v].add(cu)
        elif cv != -1 and cv not in used_at_vertex[u]:
            color[eid] = cv
            used_at_vertex[u].add(cv)
            used_at_vertex[v].add(cv)
        else:
            # Both vertices fully colored with different colors: need Kempe chain
            cu = get_free_color(u)
            cv = get_free_color(v)
            # find a color missing at u and present at v, or vice versa
            missing_u = None
            for c in range(max_color):
                if c not in used_at_vertex[u] and c in used_at_vertex[v]:
                    missing_u = c
                    break
            if missing_u is None:
                for c in range(max_color):
                    if c not in used_at_vertex[v] and c in used_at_vertex[u]:
                        missing_u = c
                        break
            # At this point both are full, missing_u should exist
            # Find the other free color at the other vertex
            missing_v = None
            for c in range(max_color):
                if c not in used_at_vertex[v] and c in used_at_vertex[u]:
                    missing_v = c
                    break
            if missing_v is None:
                for c in range(max_color):
                    if c not in used_at_vertex[u] and c in used_at_vertex[v]:
                        missing_v = c
                        break
            # swap chain between missing_u and missing_v
            swap_chain(u, missing_u, missing_v, -1)
            # After swap, get colors again
            cu = get_free_color(u)
            cv = get_free_color(v)
            if cu != -1:
                color[eid] = cu
                used_at_vertex[u].add(cu)
                used_at_vertex[v].add(cu)
            else:
                color[eid] = cv
                used_at_vertex[u].add(cv)
                used_at_vertex[v].add(cv)
    return [c + 1 for c in color]

def main():
    data = sys.stdin.read().strip().split()
    if not data:
        return
    it = iter(data)
    n = int(next(it))
    m = int(next(it))
    edges = []
    for _ in range(m):
        u = int(next(it)) - 1
        v = int(next(it)) - 1
        edges.append((u, v))

    bridges = find_bridges(n, edges)
    if bridges:
        print("NO")
    else:
        coloring = edge_color_cubic(n, edges)
        print("YES")
        print(" ".join(map(str, coloring)))

if __name__ == "__main__":
    main()