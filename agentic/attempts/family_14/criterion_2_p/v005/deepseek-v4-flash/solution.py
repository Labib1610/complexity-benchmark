import sys
sys.setrecursionlimit(300000)

def solve():
    input = sys.stdin.readline
    n, m, t = map(int, input().split())
    required = set(map(int, input().split()))
    
    adj = [[] for _ in range(n + 1)]
    for _ in range(m):
        u, v, w = map(int, input().split())
        adj[u].append((v, w))
        adj[v].append((u, w))
    
    # If only one required site, no cabling needed
    if t == 1:
        print(0)
        return
    
    # Find a required node to start DFS
    start = next(iter(required))
    
    # DFS to find distances from start to all nodes
    parent = [-1] * (n + 1)
    dist = [0] * (n + 1)
    stack = [(start, -1, 0)]
    while stack:
        u, p, d = stack.pop()
        parent[u] = p
        dist[u] = d
        for v, w in adj[u]:
            if v != p:
                stack.append((v, u, d + w))
    
    # Find farthest required node from start
    far_node = start
    max_dist = -1
    for node in required:
        if dist[node] > max_dist:
            max_dist = dist[node]
            far_node = node
    
    # DFS from far_node to find distances and mark edges on paths to required nodes
    dist2 = [0] * (n + 1)
    parent2 = [-1] * (n + 1)
    stack = [(far_node, -1, 0)]
    while stack:
        u, p, d = stack.pop()
        parent2[u] = p
        dist2[u] = d
        for v, w in adj[u]:
            if v != p:
                stack.append((v, u, d + w))
    
    # Find the other farthest required node
    far2 = far_node
    max_dist2 = -1
    for node in required:
        if dist2[node] > max_dist2:
            max_dist2 = dist2[node]
            far2 = node
    
    # Mark all nodes that are on paths between required nodes
    # We can do this by marking ancestors from each required node up to far_node and far2
    in_subtree = [False] * (n + 1)
    
    # Mark path from far_node to far2
    u = far2
    while u != -1:
        in_subtree[u] = True
        u = parent2[u]
    
    # For each required node, mark path to far_node
    for node in required:
        u = node
        while u != -1 and not in_subtree[u]:
            in_subtree[u] = True
            u = parent2[u]
    
    # Now sum edges where both endpoints are in_subtree
    total_cost = 0
    for u in range(1, n + 1):
        if in_subtree[u]:
            for v, w in adj[u]:
                if u < v and in_subtree[v]:
                    total_cost += w
    
    print(total_cost)

if __name__ == "__main__":
    solve()