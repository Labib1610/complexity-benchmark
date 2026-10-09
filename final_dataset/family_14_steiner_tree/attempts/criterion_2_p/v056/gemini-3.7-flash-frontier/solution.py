import sys

def solve():
    input_data = sys.stdin.read().split()
    if not input_data:
        return
    
    n = int(input_data[0])
    m = int(input_data[1])
    t = int(input_data[2])
    
    ptr = 3
    is_terminal = [False] * (n + 1)
    for _ in range(t):
        term = int(input_data[ptr])
        is_terminal[term] = True
        ptr += 1
        
    if t <= 1:
        print(0)
        return

    adj = [[] for _ in range(n + 1)]
    for _ in range(m):
        u = int(input_data[ptr])
        v = int(input_data[ptr + 1])
        w = int(input_data[ptr + 2])
        adj[u].append((v, w))
        adj[v].append((u, w))
        ptr += 3

    parent = [0] * (n + 1)
    weight_to_parent = [0] * (n + 1)
    order = []
    
    # BFS to establish parent relationships and order
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
                weight_to_parent[v] = w
                queue.append(v)
                
    terminal_count = [0] * (n + 1)
    for i in range(1, n + 1):
        if is_terminal[i]:
            terminal_count[i] = 1
            
    total_cost = 0
    for u in reversed(order):
        p = parent[u]
        if p != 0:
            if 0 < terminal_count[u] < t:
                total_cost += weight_to_parent[u]
            terminal_count[p] += terminal_count[u]

    print(total_cost)

if __name__ == '__main__':
    solve()