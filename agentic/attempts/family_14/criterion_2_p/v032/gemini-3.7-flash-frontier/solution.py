import sys

def solve():
    input = sys.stdin.read
    data = input().split()
    if not data:
        return
    
    n = int(data[0])
    m = int(data[1])
    t = int(data[2])
    
    if t <= 1:
        print(0)
        return

    idx = 3
    critical = [False] * (n + 1)
    for _ in range(t):
        c = int(data[idx])
        critical[c] = True
        idx += 1
    
    adj = [[] for _ in range(n + 1)]
    for _ in range(m):
        u = int(data[idx])
        v = int(data[idx+1])
        w = int(data[idx+2])
        adj[u].append((v, w))
        adj[v].append((u, w))
        idx += 3
    
    # Root the tree at 1
    parent = [0] * (n + 1)
    edge_weight = [0] * (n + 1)
    order = []
    
    stack = [1]
    visited = [False] * (n + 1)
    visited[1] = True
    
    while stack:
        u = stack.pop()
        order.append(u)
        for v, w in adj[u]:
            if not visited[v]:
                visited[v] = True
                parent[v] = u
                edge_weight[v] = w
                stack.append(v)
    
    cnt = [0] * (n + 1)
    for u in range(1, n + 1):
        if critical[u]:
            cnt[u] = 1
            
    total_cost = 0
    for u in reversed(order):
        if u != 1:
            p = parent[u]
            cnt[p] += cnt[u]
            if 0 < cnt[u] < t:
                total_cost += edge_weight[u]
                
    print(total_cost)

if __name__ == '__main__':
    solve()