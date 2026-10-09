import sys

def main():
    input = sys.stdin.read
    data = input().split()
    if not data:
        return
    
    n = int(data[0])
    m = int(data[1])
    t = int(data[2])
    
    idx = 3
    is_priority = [0] * (n + 1)
    for _ in range(t):
        is_priority[int(data[idx])] = 1
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

    # BFS to establish parent relationships and order
    parent = [0] * (n + 1)
    edge_weight_to_parent = [0] * (n + 1)
    visited = [False] * (n + 1)
    
    order = []
    queue = [1]
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
                edge_weight_to_parent[v] = w
                queue.append(v)
                
    count = list(is_priority)
    total_cost = 0
    
    for u in reversed(order):
        p = parent[u]
        if p != 0:
            if 0 < count[u] < t:
                total_cost += edge_weight_to_parent[u]
            count[p] += count[u]
            
    print(total_cost)

if __name__ == '__main__':
    main()