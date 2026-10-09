import sys
sys.setrecursionlimit(300000)

def solve():
    input = sys.stdin.readline
    n, m, t = map(int, input().split())
    essential = set(map(int, input().split()))
    
    adj = [[] for _ in range(n+1)]
    for _ in range(m):
        u, v, w = map(int, input().split())
        adj[u].append((v, w))
        adj[v].append((u, w))
    
    if t <= 1:
        print(0)
        return
    
    # Root at any essential site
    root = next(iter(essential))
    
    parent = [0]*(n+1)
    parent_edge_weight = [0]*(n+1)
    visited = [False]*(n+1)
    order = []
    
    stack = [root]
    visited[root] = True
    while stack:
        u = stack.pop()
        order.append(u)
        for v, w in adj[u]:
            if not visited[v]:
                visited[v] = True
                parent[v] = u
                parent_edge_weight[v] = w
                stack.append(v)
    
    essential_count = [0]*(n+1)
    for node in order[::-1]:
        if node in essential:
            essential_count[node] += 1
        if parent[node] != 0:
            essential_count[parent[node]] += essential_count[node]
    
    total_cost = 0
    for node in range(1, n+1):
        if node == root:
            continue
        cnt = essential_count[node]
        if cnt > 0 and cnt < t:
            total_cost += parent_edge_weight[node]
    
    print(total_cost)

if __name__ == "__main__":
    solve()