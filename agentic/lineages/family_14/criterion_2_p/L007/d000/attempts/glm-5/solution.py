import sys
from collections import deque

def solve():
    input = sys.stdin.read
    data = input().split()
    if not data:
        return
    
    n = int(data[0])
    m = int(data[1])
    t = int(data[2])
    
    leased = set()
    idx = 3
    for _ in range(t):
        leased.add(int(data[idx]))
        idx += 1
        
    adj = [[] for _ in range(n + 1)]
    for _ in range(m):
        u = int(data[idx])
        v = int(data[idx+1])
        w = int(data[idx+2])
        adj[u].append((v, w))
        adj[v].append((u, w))
        idx += 3
        
    if t <= 1:
        print(0)
        return
        
    parent = [0] * (n + 1)
    parent_weight = [0] * (n + 1)
    depth = [0] * (n + 1)
    children = [[] for _ in range(n + 1)]
    
    root = next(iter(leased))
    queue = deque([root])
    parent[root] = -1
    visited = [False] * (n + 1)
    visited[root] = True
    
    while queue:
        u = queue.popleft()
        for v, w in adj[u]:
            if not visited[v]:
                visited[v] = True
                parent[v] = u
                parent_weight[v] = w
                depth[v] = depth[u] + 1
                children[u].append(v)
                queue.append(v)
                
    dp = [0] * (n + 1)
    stack = [root]
    order = []
    while stack:
        u = stack.pop()
        order.append(u)
        for v in children[u]:
            stack.append(v)
            
    for u in reversed(order):
        if u in leased:
            dp[u] = parent_weight[u]
        else:
            if children[u]:
                min_child = min(dp[v] for v in children[u])
                dp[u] = min(parent_weight[u], min_child)
            else:
                dp[u] = parent_weight[u]
                
    total_cost = 0
    for v in children[root]:
        total_cost += dp[v]
        
    print(total_cost)

if __name__ == '__main__':
    solve()