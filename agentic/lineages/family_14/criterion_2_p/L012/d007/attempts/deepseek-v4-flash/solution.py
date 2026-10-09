import sys
sys.setrecursionlimit(300000)

def solve():
    input = sys.stdin.readline
    n, m, t = map(int, input().split())
    primary = set(map(int, input().split()))
    
    adj = [[] for _ in range(n+1)]
    for _ in range(m):
        u, v, w = map(int, input().split())
        adj[u].append((v, w))
        adj[v].append((u, w))
    
    # DFS to find which edges are needed
    parent = [0]*(n+1)
    parent_weight = [0]*(n+1)
    visited = [False]*(n+1)
    stack = [next(iter(primary))]
    visited[stack[0]] = True
    
    order = []
    while stack:
        u = stack.pop()
        order.append(u)
        for v, w in adj[u]:
            if not visited[v]:
                visited[v] = True
                parent[v] = u
                parent_weight[v] = w
                stack.append(v)
    
    # Determine which nodes have primary in subtree
    has_primary = [False]*(n+1)
    for p in primary:
        has_primary[p] = True
    
    total_cost = 0
    # Process in reverse order of DFS
    for u in reversed(order):
        if u != next(iter(primary)):
            p = parent[u]
            if has_primary[u]:
                has_primary[p] = True
                total_cost += parent_weight[u]
    
    print(total_cost)

if __name__ == "__main__":
    solve()