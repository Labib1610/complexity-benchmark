import sys
sys.setrecursionlimit(300000)

def solve():
    input = sys.stdin.readline
    n, m, t = map(int, input().split())
    flagged = list(map(int, input().split()))
    flag_set = set(flagged)
    
    adj = [[] for _ in range(n + 1)]
    for _ in range(m):
        u, v, w = map(int, input().split())
        adj[u].append((v, w))
        adj[v].append((u, w))
    
    if t == 1:
        print(0)
        return
    
    # Step 1: Mark flagged nodes and count flagged in subtree
    parent = [0] * (n + 1)
    depth = [0] * (n + 1)
    dist = [0] * (n + 1)
    order = []
    stack = [1]
    parent[1] = -1
    while stack:
        u = stack.pop()
        order.append(u)
        for v, w in adj[u]:
            if v != parent[u]:
                parent[v] = u
                depth[v] = depth[u] + 1
                dist[v] = dist[u] + w
                stack.append(v)
    
    # Step 2: Find virtual tree edges
    # Sort flagged nodes by DFS order (we can use depth order from our traversal)
    flagged.sort(key=lambda x: depth[x])
    
    # LCA via binary lifting
    LOG = (n).bit_length()
    up = [[0] * (n + 1) for _ in range(LOG)]
    for i in range(1, n + 1):
        up[0][i] = parent[i] if parent[i] != -1 else i
    for k in range(1, LOG):
        for i in range(1, n + 1):
            up[k][i] = up[k-1][up[k-1][i]]
    
    def lca(u, v):
        if depth[u] < depth[v]:
            u, v = v, u
        diff = depth[u] - depth[v]
        for k in range(LOG):
            if diff & (1 << k):
                u = up[k][u]
        if u == v:
            return u
        for k in range(LOG - 1, -1, -1):
            if up[k][u] != up[k][v]:
                u = up[k][u]
                v = up[k][v]
        return parent[u]
    
    # Build virtual tree
    nodes = flagged[:]
    # Add LCAs of consecutive flagged nodes in DFS order
    for i in range(t - 1):
        nodes.append(lca(flagged[i], flagged[i+1]))
    nodes = list(set(nodes))
    nodes.sort(key=lambda x: depth[x])
    
    # Stack method to build virtual tree
    stack = []
    edges = []
    for u in nodes:
        if not stack:
            stack.append(u)
            continue
        while stack and lca(stack[-1], u) != stack[-1]:
            stack.pop()
        if stack:
            edges.append((stack[-1], u))
        stack.append(u)
    
    # Step 3: Compute total weight of minimal subtree connecting flagged nodes
    # The minimal subtree is the union of paths between flagged nodes in virtual tree
    # We can compute total weight by summing distances along virtual tree edges
    total = 0
    for u, v in edges:
        total += dist[u] + dist[v] - 2 * dist[lca(u, v)]
    
    print(total)

if __name__ == "__main__":
    solve()