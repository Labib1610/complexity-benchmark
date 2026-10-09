import sys

def solve():
    input = sys.stdin.read
    data = input().split()
    if not data:
        return
    
    n = int(data[0])
    m = int(data[1])
    t = int(data[2])
    
    idx = 3
    is_terminal = [False] * (n + 1)
    for _ in range(t):
        term = int(data[idx])
        is_terminal[term] = True
        idx += 1
        
    if t <= 1:
        print(0)
        return

    adj = [[] for _ in range(n + 1)]
    for _ in range(m):
        u = int(data[idx])
        v = int(data[idx+1])
        w = int(data[idx+2])
        adj[u].append((v, w))
        adj[v].append((u, w))
        idx += 3

    # BFS/DFS to establish parent pointers and order for post-order processing
    parent = [0] * (n + 1)
    parent_edge_weight = [0] * (n + 1)
    order = []
    stack = [1]
    visited = [False] * (n + 1)
    visited[1] = True
    
    # We can use BFS to find parents and BFS order
    head = 0
    bfs_queue = [1]
    while head < len(bfs_queue):
        u = bfs_queue[head]
        head += 1
        for v, w in adj[u]:
            if not visited[v]:
                visited[v] = True
                parent[v] = u
                parent_edge_weight[v] = w
                bfs_queue.append(v)
                
    # Post-order: reverse of BFS queue
    terminal_count = [1 if is_terminal[i] else 0 for i in range(n + 1)]
    total_energy = 0
    
    for u in reversed(bfs_queue):
        if u == 1:
            continue
        p = parent[u]
        terminal_count[p] += terminal_count[u]
        if 0 < terminal_count[u] < t:
            total_energy += parent_edge_weight[u]
            
    print(total_energy)

if __name__ == '__main__':
    solve()