import sys
sys.setrecursionlimit(300000)

def solve():
    input = sys.stdin.readline
    R, S, P = map(int, input().split())
    injected = set(map(int, input().split()))
    
    adj = [[] for _ in range(R + 1)]
    edges = []
    for _ in range(S):
        u, v, w = map(int, input().split())
        adj[u].append((v, w))
        adj[v].append((u, w))
        edges.append((u, v, w))
    
    # DFS to count injected nodes in subtree
    visited = [False] * (R + 1)
    def dfs(u):
        visited[u] = True
        count = 1 if u in injected else 0
        for v, w in adj[u]:
            if not visited[v]:
                count += dfs(v)
        return count
    
    # Start from any injected node
    start = next(iter(injected))
    total_cost = 0
    
    # We need to traverse and check each edge
    # Use iterative DFS to avoid recursion depth issues
    stack = [(start, -1, 0)]  # (node, parent, edge_weight_to_parent)
    visited = [False] * (R + 1)
    while stack:
        u, parent, w_parent = stack.pop()
        if visited[u]:
            continue
        visited[u] = True
        if parent != -1:
            # Check if subtree below u has any injected node
            # We'll do a second DFS to count injected in subtree
            # But we can do it with a post-order approach
            pass
        for v, w in adj[u]:
            if v != parent:
                stack.append((v, u, w))
    
    # Better: do a post-order DFS to count injected nodes in subtree
    visited = [False] * (R + 1)
    def dfs_count(u):
        visited[u] = True
        cnt = 1 if u in injected else 0
        for v, w in adj[u]:
            if not visited[v]:
                cnt += dfs_count(v)
        return cnt
    
    # We'll compute subtree counts and then sum edges where subtree count > 0
    # But we need to know which edges are in the minimal subtree.
    # Approach: root at start, compute subtree injected counts.
    # Then for each edge (parent->child), if child's subtree count > 0, include edge.
    
    parent = [0] * (R + 1)
    weight_to_parent = [0] * (R + 1)
    order = []
    stack = [start]
    visited = [False] * (R + 1)
    visited[start] = True
    while stack:
        u = stack.pop()
        order.append(u)
        for v, w in adj[u]:
            if not visited[v]:
                visited[v] = True
                parent[v] = u
                weight_to_parent[v] = w
                stack.append(v)
    
    subtree_count = [0] * (R + 1)
    for u in reversed(order):
        cnt = 1 if u in injected else 0
        for v, w in adj[u]:
            if parent[v] == u:
                cnt += subtree_count[v]
        subtree_count[u] = cnt
    
    total_cost = 0
    for u in range(1, R + 1):
        if u != start and subtree_count[u] > 0:
            total_cost += weight_to_parent[u]
    
    print(total_cost)

if __name__ == "__main__":
    solve()