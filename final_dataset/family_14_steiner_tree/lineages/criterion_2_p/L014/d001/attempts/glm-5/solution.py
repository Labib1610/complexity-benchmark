import sys
import heapq

def solve():
    input = sys.stdin.read().split()
    ptr = 0
    n = int(input[ptr]); ptr += 1
    m = int(input[ptr]); ptr += 1
    t = int(input[ptr]); ptr += 1
    
    required = [False] * (n + 1)
    for _ in range(t):
        u = int(input[ptr]); ptr += 1
        required[u] = True
    
    adj = [[] for _ in range(n + 1)]
    for _ in range(m):
        u = int(input[ptr]); ptr += 1
        v = int(input[ptr]); ptr += 1
        w = int(input[ptr]); ptr += 1
        adj[u].append((v, w))
        adj[v].append((u, w))
    
    # Prim's algorithm starting from required nodes
    in_mst = [False] * (n + 1)
    min_edge = [float('inf')] * (n + 1)
    pq = []
    
    for i in range(1, n + 1):
        if required[i]:
            min_edge[i] = 0
            heapq.heappush(pq, (0, i))
    
    total_cost = 0
    nodes_in_mst = 0
    
    while pq and nodes_in_mst < n:
        cost, u = heapq.heappop(pq)
        if in_mst[u]:
            continue
        in_mst[u] = True
        total_cost += cost
        nodes_in_mst += 1
        
        for v, w in adj[u]:
            if not in_mst[v] and w < min_edge[v]:
                min_edge[v] = w
                heapq.heappush(pq, (w, v))
    
    print(total_cost)

if __name__ == "__main__":
    solve()