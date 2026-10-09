import sys
sys.setrecursionlimit(300000)

def solve():
    input = sys.stdin.readline
    N, E, F = map(int, input().split())
    critical = set(map(int, input().split()))
    
    adj = [[] for _ in range(N+1)]
    for _ in range(E):
        u, v, w = map(int, input().split())
        adj[u].append((v, w))
        adj[v].append((u, w))
    
    if F <= 1:
        print(0)
        return
    
    # DFS to find minimal subtree spanning critical nodes
    parent = [0]*(N+1)
    parent_edge_cost = [0]*(N+1)
    visited = [False]*(N+1)
    
    # First DFS to get parent info from arbitrary root (1)
    stack = [1]
    visited[1] = True
    order = []
    while stack:
        u = stack.pop()
        order.append(u)
        for v, w in adj[u]:
            if not visited[v]:
                visited[v] = True
                parent[v] = u
                parent_edge_cost[v] = w
                stack.append(v)
    
    # Mark which nodes are needed in the minimal subtree
    needed = [False]*(N+1)
    for c in critical:
        needed[c] = True
    
    # Process in reverse order to propagate need upward
    total_cost = 0
    for u in reversed(order):
        if needed[u] and u != 1:
            total_cost += parent_edge_cost[u]
            needed[parent[u]] = True
    
    print(total_cost)

if __name__ == "__main__":
    solve()