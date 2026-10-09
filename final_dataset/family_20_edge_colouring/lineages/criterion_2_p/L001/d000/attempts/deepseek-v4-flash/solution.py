import sys
sys.setrecursionlimit(1 << 25)
input = sys.stdin.readline

nU, nD, m = map(int, input().split())
edges = []
adj = [[] for _ in range(nU + nD + 1)]  # vertices: 1..nU upstream, nU+1..nU+nD downstream
for i in range(m):
    u, v = map(int, input().split())
    v2 = nU + v
    edges.append((u, v2))
    adj[u].append((v2, i))
    adj[v2].append((u, i))

# Compute K
deg = [0] * (nU + nD + 1)
for u, v in edges:
    deg[u] += 1
    deg[v] += 1
K = max(deg) if m > 0 else 0

color = [0] * m

def edge_color(edge_list, max_deg):
    if max_deg == 0:
        return
    if max_deg == 1:
        # all edges get distinct colors? Actually in bipartite, max_deg=1 means matching, so all can be same color? No, edges sharing vertex can't. But if max_deg=1, each vertex has at most 1 edge, so all edges can be same color.
        for e in edge_list:
            color[e] = 1
        return
    # Build adjacency for this subgraph
    local_adj = [[] for _ in range(nU + nD + 1)]
    for e in edge_list:
        u, v = edges[e]
        local_adj[u].append((v, e))
        local_adj[v].append((u, e))
    # Find Euler circuits to split into two subgraphs
    # We'll use Hierholzer's algorithm
    used = [False] * len(edge_list)
    sub1 = []
    sub2 = []
    # We need to handle odd degree vertices
    # In bipartite graph, number of odd degree vertices is even
    # We'll pair them with dummy edges? Simpler: use DFS to find trails
    # Actually we can just do: while there are unused edges, find a trail
    stack = []
    # Start from any vertex with odd degree or any vertex with edges
    # We'll implement iterative Euler tour
    # But easier: use recursive DFS to find trails
    # We'll do:
    # For each vertex, if it has unused edges, start a trail
    # But we need to split edges alternately into two subgraphs
    # Standard method: find Euler circuits, then color alternate edges
    # Let's do:
    # Build adjacency list with edge indices
    adj_list = [[] for _ in range(nU + nD + 1)]
    for idx, e in enumerate(edge_list):
        u, v = edges[e]
        adj_list[u].append((v, e))
        adj_list[v].append((u, e))
    # We'll use iterative stack to find trails
    # We'll mark used edges
    used_edges = [False] * len(edge_list)
    for start in range(1, nU + nD + 1):
        if adj_list[start]:
            # find trail
            stack = [(start, -1)]  # vertex, parent edge
            trail = []
            while stack:
                v, pe = stack[-1]
                # find next unused edge
                found = False
                while adj_list[v]:
                    to, e = adj_list[v].pop()
                    if not used_edges[e]:
                        used_edges[e] = True
                        stack.append((to, e))
                        found = True
                        break
                if not found:
                    # backtrack
                    if pe != -1:
                        trail.append(pe)
                    stack.pop()
            # Now trail is in reverse order
            # Color alternately
            for i, e in enumerate(trail):
                if i % 2 == 0:
                    sub1.append(e)
                else:
                    sub2.append(e)
    # Now recurse
    # But we need to assign colors: sub1 gets colors 1..ceil(K/2), sub2 gets colors ceil(K/2)+1..K
    # Actually we can just recurse and then add offset
    # We'll do:
    # color_sub1 = edge_color(sub1, (max_deg+1)//2)
    # color_sub2 = edge_color(sub2, max_deg//2)
    # Then for sub2, add offset
    # But we need to return the color mapping? We'll directly set global color array.
    # So:
    if sub1:
        # assign colors 1..c1
        c1 = (max_deg + 1) // 2
        # We'll call recursively with a "color_offset" parameter? Simpler: we can just call and then add offset later.
        # But we need to know which edges are in sub1/sub2.
        # We'll pass a color_offset parameter.
        pass

# This is getting complicated. Let's implement with color offset.

def edge_color_rec(edge_list, max_deg, offset):
    if max_deg == 0:
        return
    if max_deg == 1:
        for e in edge_list:
            color[e] = offset + 1
        return
    # Build adjacency
    adj_list = [[] for _ in range(nU + nD + 1)]
    for e in edge_list:
        u, v = edges[e]
        adj_list[u].append((v, e))
        adj_list[v].append((u, e))
    used_edges = [False] * len(edge_list)
    sub1 = []
    sub2 = []
    for start in range(1, nU + nD + 1):
        if adj_list[start]:
            stack = [(start, -1)]
            trail = []
            while stack:
                v, pe = stack[-1]
                found = False
                while adj_list[v]:
                    to, e = adj_list[v].pop()
                    if not used_edges[e]:
                        used_edges[e] = True
                        stack.append((to, e))
                        found = True
                        break
                if not found:
                    if pe != -1:
                        trail.append(pe)
                    stack.pop()
            for i, e in enumerate(trail):
                if i % 2 == 0:
                    sub1.append(e)
                else:
                    sub2.append(e)
    c1 = (max_deg + 1) // 2
    c2 = max_deg // 2
    edge_color_rec(sub1, c1, offset)
    edge_color_rec(sub2, c2, offset + c1)

if m > 0:
    edge_color_rec(list(range(m)), K, 0)

print("YES")
print(" ".join(str(c) for c in color))