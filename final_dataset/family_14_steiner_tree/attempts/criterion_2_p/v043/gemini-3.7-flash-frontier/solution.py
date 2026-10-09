import sys

def main():
    input_data = sys.stdin.read().split()
    if not input_data:
        return
    
    n = int(input_data[0])
    m = int(input_data[1])
    t = int(input_data[2])
    
    idx = 3
    critical = [int(x) for x in input_data[idx:idx + t]]
    idx += t
    
    if t <= 1:
        print(0)
        return
    
    is_critical = [False] * (n + 1)
    for c in critical:
        is_critical[c] = True
        
    adj = [[] for _ in range(n + 1)]
    for _ in range(m):
        u = int(input_data[idx])
        v = int(input_data[idx + 1])
        w = int(input_data[idx + 2])
        idx += 3
        adj[u].append((v, w))
        adj[v].append((u, w))
        
    root = critical[0]
    parent = [0] * (n + 1)
    edge_to_parent_weight = [0] * (n + 1)
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
                edge_to_parent_weight[v] = w
                stack.append(v)
                
    crit_count = [0] * (n + 1)
    for i in range(1, n + 1):
        if is_critical[i]:
            crit_count[i] = 1
            
    total_cost = 0
    for u in reversed(order):
        p = parent[u]
        if p != 0:
            if crit_count[u] > 0:
                total_cost += edge_to_parent_weight[u]
                crit_count[p] += crit_count[u]
                
    print(total_cost)

if __name__ == '__main__':
    main()