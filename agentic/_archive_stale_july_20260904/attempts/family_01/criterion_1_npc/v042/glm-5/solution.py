import sys

def solve():
    data = sys.stdin.read().split()
    if not data:
        return
    it = iter(data)
    n = int(next(it))
    m = int(next(it))

    adj = [set() for _ in range(n)]
    for _ in range(m):
        u = int(next(it)) - 1
        v = int(next(it)) - 1
        adj[u].add(v)
        adj[v].add(u)

    # Check if graph is 3-colorable
    # A graph is not 3-colorable if it contains K4 as a subgraph
    possible = True
    for u in range(n):
        neighbors_u = list(adj[u])
        for i in range(len(neighbors_u)):
            v = neighbors_u[i]
            if v < u: continue
            for j in range(i + 1, len(neighbors_u)):
                w = neighbors_u[j]
                if w < u: continue
                if w in adj[v]:
                    # u, v, w form a triangle
                    # Check for K4
                    for x in neighbors_u:
                        if x > u and x != v and x != w:
                            if x in adj[v] and x in adj[w]:
                                possible = False
                                break
                        if not possible: break
                    if not possible: break
            if not possible: break
        if not possible: break

    if not possible:
        print("NO")
        return

    # Find lexicographically smallest coloring
    colors = [0] * n
    
    def get_min_color(u):
        used = {colors[v] for v in adj[u] if colors[v] != 0}
        for c in range(1, 4):
            if c not in used:
                return c
        return 1

    for u in range(n):
        colors[u] = get_min_color(u)

    print("YES")
    print(" ".join(map(str, colors)))

if __name__ == '__main__':
    solve()