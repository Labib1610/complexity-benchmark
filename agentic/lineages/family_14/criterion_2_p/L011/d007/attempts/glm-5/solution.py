import sys
from collections import deque

def solve():
    input_data = sys.stdin.buffer.read().split()
    idx = 0
    n = int(input_data[idx]); idx += 1
    m = int(input_data[idx]); idx += 1
    t = int(input_data[idx]); idx += 1
    
    is_anchor = [False] * (n + 1)
    for i in range(t):
        a = int(input_data[idx]); idx += 1
        is_anchor[a] = True
    
    adj = [[] for _ in range(n + 1)]
    total_weight = 0
    for i in range(m):
        u = int(input_data[idx]); idx += 1
        v = int(input_data[idx]); idx += 1
        w = int(input_data[idx]); idx += 1
        adj[u].append((v, w))
        adj[v].append((u, w))
        total_weight += w
    
    degree = [0] * (n + 1)
    for i in range(1, n + 1):
        degree[i] = len(adj[i])
    
    removed_weight = 0
    queue = deque()
    in_queue = [False] * (n + 1)
    
    for i in range(1, n + 1):
        if degree[i] <= 1 and not is_anchor[i]:
            queue.append(i)
            in_queue[i] = True
    
    while queue:
        node = queue.popleft()
        for neighbor, weight in adj[node]:
            if degree[neighbor] > 0:
                removed_weight += weight
                degree[neighbor] -= 1
                degree[node] -= 1
                if degree[neighbor] <= 1 and not is_anchor[neighbor] and not in_queue[neighbor]:
                    queue.append(neighbor)
                    in_queue[neighbor] = True
                break
    
    print(total_weight - removed_weight)

solve()