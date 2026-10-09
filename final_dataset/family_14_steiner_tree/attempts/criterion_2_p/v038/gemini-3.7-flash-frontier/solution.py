import sys

def main():
    input_data = sys.stdin.read().split()
    if not input_data:
        return
    
    n = int(input_data[0])
    m = int(input_data[1])
    t = int(input_data[2])
    
    if t <= 1:
        print(0)
        return
    
    idx = 3
    priority = set()
    for _ in range(t):
        priority.add(int(input_data[idx]))
        idx += 1
    
    adj = [[] for _ in range(n + 1)]
    for _ in range(m):
        u = int(input_data[idx])
        v = int(input_data[idx + 1])
        w = int(input_data[idx + 2])
        adj[u].append((v, w))
        adj[v].append((u, w))
        idx += 3
    
    parent = [0] * (n + 1)
    edge_weight = [0] * (n + 1)
    order = []
    
    # BFS to establish tree structure rooted at 1
    queue = [1]
    parent[1] = -1
    head = 0
    while head < len(queue):
        u = queue[head]
        head += 1
        order.append(u)
        for v, w in adj[u]:
            if parent[v] == 0:
                parent[v] = u
                edge_weight[v] = w
                queue.append(v)
    
    cnt = [0] * (n + 1)
    for u in priority:
        cnt[u] = 1
    
    total_cost = 0
    for u in reversed(order):
        if u == 1:
            continue
        p = parent[u]
        cnt[p] += cnt[u]
        if 0 < cnt[u] < t:
            total_cost += edge_weight[u]
            
    print(total_cost)

if __name__ == '__main__':
    main()