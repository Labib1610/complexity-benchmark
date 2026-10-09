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
    
    # DFS to mark which edges are needed
    parent = [0] * (n + 1)
    parent_w = [0] * (n + 1)
    visited = [False] * (n + 1)
    
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
                parent_w[v] = w
                stack.append(v)
    
    needed = [False] * (n + 1)
    for r in required:
        needed[r] = True
    
    total_cost = 0
    # Process nodes in reverse order (post-order)
    for u in reversed(order):
        if needed[u] and parent[u] != 0:
            total_cost += parent_w[u]
            needed[parent[u]] = True
    
    print(total_cost)

if __name__ == "__main__":
    solve()