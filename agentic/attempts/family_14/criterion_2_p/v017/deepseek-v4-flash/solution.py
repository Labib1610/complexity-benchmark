import sys
sys.setrecursionlimit(300000)

def solve():
    input = sys.stdin.readline
    n, m, t = map(int, input().split())
    specials = set(map(int, input().split()))
    
    adj = [[] for _ in range(n + 1)]
    for _ in range(m):
        u, v, w = map(int, input().split())
        adj[u].append((v, w))
        adj[v].append((u, w))
    
    # Root at any special node
    root = next(iter(specials))
    
    parent = [0] * (n + 1)
    parent_w = [0] * (n + 1)
    order = [root]
    visited = [False] * (n + 1)
    visited[root] = True
    
    # BFS/DFS to set parent info
    stack = [root]
    while stack:
        u = stack.pop()
        for v, w in adj[u]:
            if not visited[v]:
                visited[v] = True
                parent[v] = u
                parent_w[v] = w
                stack.append(v)
                order.append(v)
    
    has_special = [False] * (n + 1)
    for s in specials:
        has_special[s] = True
    
    total_cost = 0
    # Process in reverse order (post-order)
    for u in reversed(order):
        if u == root:
            continue
        if has_special[u]:
            total_cost += parent_w[u]
            has_special[parent[u]] = True
    
    print(total_cost)

if __name__ == "__main__":
    solve()