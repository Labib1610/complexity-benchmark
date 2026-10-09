import sys

def solve():
    input_data = sys.stdin.read().split()
    if not input_data:
        return
    
    n = int(input_data[0])
    m = int(input_data[1])
    t = int(input_data[2])
    
    idx = 3
    flagged = [0] * (n + 1)
    for _ in range(t):
        flagged[int(input_data[idx])] = 1
        idx += 1
        
    if t <= 1:
        print(0)
        return

    adj = [[] for _ in range(n + 1)]
    for _ in range(m):
        u = int(input_data[idx])
        v = int(input_data[idx + 1])
        w = int(input_data[idx + 2])
        idx += 3
        adj[u].append((v, w))
        adj[v].append((u, w))
        
    parent = [0] * (n + 1)
    parent_edge_w = [0] * (n + 1)
    order = []
    
    # BFS to establish parent relationships and topological order
    queue = [1]
    parent[1] = 1
    
    for u in queue:
        order.append(u)
        for v, w in adj[u]:
            if not parent[v]:
                parent[v] = u
                parent_edge_w[v] = w
                queue.append(v)
                
    cnt = list(flagged)
    total_energy = 0
    
    # Post-order traversal using reversed BFS order
    for u in reversed(order):
        if u == 1:
            continue
        p = parent[u]
        cnt[p] += cnt[u]
        if 0 < cnt[u] < t:
            total_energy += parent_edge_w[u]
            
    print(total_energy)

if __name__ == '__main__':
    solve()