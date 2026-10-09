import sys

def solve():
    input = sys.stdin.read
    data = input().split()
    if not data:
        return
    
    n = int(data[0])
    m = int(data[1])
    t = int(data[2])
    
    ptr = 3
    is_terminal = [0] * (n + 1)
    for _ in range(t):
        term = int(data[ptr])
        is_terminal[term] = 1
        ptr += 1
        
    if t <= 1:
        print(0)
        return

    adj = [[] for _ in range(n + 1)]
    for _ in range(m):
        u = int(data[ptr])
        v = int(data[ptr + 1])
        w = int(data[ptr + 2])
        adj[u].append((v, w))
        adj[v].append((u, w))
        ptr += 3

    # BFS from node 1 to establish tree structure and traversal order
    parent = [0] * (n + 1)
    edge_weight = [0] * (n + 1)
    order = []
    
    queue = [1]
    visited = [False] * (n + 1)
    visited[1] = True
    
    head = 0
    while head < len(queue):
        u = queue[head]
        head += 1
        order.append(u)
        for v, w in adj[u]:
            if not visited[v]:
                visited[v] = True
                parent[v] = u
                edge_weight[v] = w
                queue.append(v)
                
    cnt = list(is_terminal)
    total_cost = 0
    
    for u in reversed(order):
        p = parent[u]
        if p != 0:
            if 0 < cnt[u] < t:
                total_cost += edge_weight[u]
            cnt[p] += cnt[u]
            
    print(total_cost)

if __name__ == '__main__':
    solve()