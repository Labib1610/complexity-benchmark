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
    keyholders = set()
    for _ in range(t):
        keyholders.add(int(data[idx]))
        idx += 1
        
    if t <= 1:
        print(0)
        return
        
    adj = [[] for _ in range(n + 1)]
    for _ in range(m):
        u = int(data[idx])
        v = int(data[idx+1])
        w = int(data[idx+2])
        idx += 3
        adj[u].append((v, w))
        adj[v].append((u, w))
        
    # Tree traversal using BFS order
    parent = [0] * (n + 1)
    edge_to_parent_weight = [0] * (n + 1)
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
                edge_to_parent_weight[v] = w
                queue.append(v)
                
    count = [0] * (n + 1)
    for u in keyholders:
        count[u] = 1
        
    total_cost = 0
    for u in reversed(order):
        if u != 1:
            p = parent[u]
            count[p] += count[u]
            if 0 < count[u] < t:
                total_cost += edge_to_parent_weight[u]
                
    print(total_cost)

if __name__ == '__main__':
    main()