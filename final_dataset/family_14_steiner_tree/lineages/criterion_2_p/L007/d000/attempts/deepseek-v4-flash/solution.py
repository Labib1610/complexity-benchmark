import sys
sys.setrecursionlimit(300000)

def solve():
    input = sys.stdin.readline
    n, m, t = map(int, input().split())
    leased = set(map(int, input().split()))
    
    adj = [[] for _ in range(n + 1)]
    for _ in range(m):
        u, v, w = map(int, input().split())
        adj[u].append((v, w))
        adj[v].append((u, w))
    
    if t == 1:
        print(0)
        return
    
    # DFS to mark nodes that are part of the minimal subtree
    parent = [0] * (n + 1)
    parent_edge_weight = [0] * (n + 1)
    visited = [False] * (n + 1)
    
    # Start DFS from any leased node
    start = next(iter(leased))
    stack = [start]
    visited[start] = True
    
    order = []
    while stack:
        u = stack.pop()
        order.append(u)
        for v, w in adj[u]:
            if not visited[v]:
                visited[v] = True
                parent[v] = u
                parent_edge_weight[v] = w
                stack.append(v)
    
    # Mark which nodes are needed
    needed = [False] * (n + 1)
    for node in leased:
        needed[node] = True
    
    # Process nodes in reverse DFS order
    total_cost = 0
    for u in reversed(order):
        if needed[u] and parent[u] != 0:
            total_cost += parent_edge_weight[u]
            # Mark parent as needed
            needed[parent[u]] = True
    
    print(total_cost)

if __name__ == "__main__":
    solve()