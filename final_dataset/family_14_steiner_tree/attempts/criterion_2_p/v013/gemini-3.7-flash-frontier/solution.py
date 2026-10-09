import sys
from collections import deque

def main():
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
    critical = [int(data[idx + i]) for i in range(t)]
    idx += t
    
    is_critical = [0] * (n + 1)
    for u in critical:
        is_critical[u] = 1
        
    adj = [[] for _ in range(n + 1)]
    for _ in range(m):
        u = int(data[idx])
        v = int(data[idx + 1])
        w = int(data[idx + 2])
        idx += 3
        adj[u].append((v, w))
        adj[v].append((u, w))
        
    order = []
    parent = [0] * (n + 1)
    parent_weight = [0] * (n + 1)
    visited = [False] * (n + 1)
    
    queue = deque([1])
    visited[1] = True
    
    while queue:
        u = queue.popleft()
        order.append(u)
        for v, w in adj[u]:
            if not visited[v]:
                visited[v] = True
                parent[v] = u
                parent_weight[v] = w
                queue.append(v)
                
    counts = list(is_critical)
    total_cost = 0
    
    for u in reversed(order):
        if u == 1:
            continue
        p = parent[u]
        counts[p] += counts[u]
        if 0 < counts[u] < t:
            total_cost += parent_weight[u]
            
    print(total_cost)

if __name__ == '__main__':
    main()