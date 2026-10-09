import sys

def main():
    input = sys.stdin.read
    data = input().split()
    if not data:
        return
    
    n = int(data[0])
    m = int(data[1])
    t = int(data[2])
    
    ptr = 3
    cores = [int(x) for x in data[ptr:ptr+t]]
    ptr += t
    
    if t <= 1:
        print(0)
        return
    
    is_core = [False] * (n + 1)
    for c in cores:
        is_core[c] = True
        
    adj = [[] for _ in range(n + 1)]
    for _ in range(m):
        u = int(data[ptr])
        v = int(data[ptr+1])
        w = int(data[ptr+2])
        ptr += 3
        adj[u].append((v, w))
        adj[v].append((u, w))
        
    root = cores[0]
    parent = [0] * (n + 1)
    edge_weight = [0] * (n + 1)
    order = []
    
    stack = [root]
    visited = [False] * (n + 1)
    visited[root] = True
    
    while stack:
        u = stack.pop()
        order.append(u)
        for v, w in adj[u]:
            if not visited[v]:
                visited[v] = True
                parent[v] = u
                edge_weight[v] = w
                stack.append(v)
                
    has_core = [False] * (n + 1)
    for c in cores:
        has_core[c] = True
        
    total_energy = 0
    for u in reversed(order):
        if u == root:
            continue
        if has_core[u]:
            total_energy += edge_weight[u]
            has_core[parent[u]] = True
            
    print(total_energy)

if __name__ == '__main__':
    main()