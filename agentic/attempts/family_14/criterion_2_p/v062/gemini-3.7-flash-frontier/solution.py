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
    
    ptr = 3
    critical_nodes = [int(data[ptr + i]) for i in range(t)]
    ptr += t
    
    is_critical = [0] * (n + 1)
    for u in critical_nodes:
        is_critical[u] = 1
        
    head = [-1] * (n + 1)
    to = [0] * (2 * m)
    weight = [0] * (2 * m)
    nxt = [-1] * (2 * m)
    
    edge_idx = 0
    for _ in range(m):
        u = int(data[ptr])
        v = int(data[ptr + 1])
        w = int(data[ptr + 2])
        ptr += 3
        
        to[edge_idx] = v
        weight[edge_idx] = w
        nxt[edge_idx] = head[u]
        head[u] = edge_idx
        edge_idx += 1
        
        to[edge_idx] = u
        weight[edge_idx] = w
        nxt[edge_idx] = head[v]
        head[v] = edge_idx
        edge_idx += 1
        
    parent = [0] * (n + 1)
    parent_w = [0] * (n + 1)
    order = []
    order_append = order.append
    
    queue = [1]
    visited = [False] * (n + 1)
    visited[1] = True
    
    head_q = 0
    while head_q < len(queue):
        u = queue[head_q]
        head_q += 1
        order_append(u)
        
        e = head[u]
        while e != -1:
            v = to[e]
            if not visited[v]:
                visited[v] = True
                parent[v] = u
                parent_w[v] = weight[e]
                queue.append(v)
            e = nxt[e]
            
    c = is_critical[:]
    total_cost = 0
    
    for i in range(n - 1, 0, -1):
        u = order[i]
        p = parent[u]
        if 0 < c[u] < t:
            total_cost += parent_w[u]
        c[p] += c[u]
        
    print(total_cost)

if __name__ == '__main__':
    solve()