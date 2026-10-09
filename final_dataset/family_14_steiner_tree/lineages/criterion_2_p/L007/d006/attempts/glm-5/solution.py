import sys
import heapq

def solve():
    input_data = sys.stdin.read().split()
    if not input_data:
        return
    it = iter(input_data)
    n = int(next(it))
    m = int(next(it))
    t = int(next(it))
    
    T = []
    for _ in range(t):
        T.append(int(next(it)))
    
    edges = []
    for _ in range(m):
        u = int(next(it))
        v = int(next(it))
        w = int(next(it))
        edges.append((u, v, w))
    
    # Special case: t <= 1, no transpositions needed
    if t <= 1:
        print(0)
        return
    
    # Build adjacency list for Prim's algorithm
    adj = [[] for _ in range(n + 1)]
    for u, v, w in edges:
        adj[u].append((v, w))
        adj[v].append((u, w))
    
    # Prim's algorithm to find MST
    total_cost = 0
    visited = [False] * (n + 1)
    min_heap = []
    
    # Start from first element in T
    start = T[0]
    visited[start] = True
    for v, w in adj[start]:
        heapq.heappush(min_heap, (w, v))
    
    nodes_in_mst = 1
    
    while min_heap and nodes_in_mst < n:
        w, u = heapq.heappop(min_heap)
        if visited[u]:
            continue
        visited[u] = True
        total_cost += w
        nodes_in_mst += 1
        for v, w2 in adj[u]:
            if not visited[v]:
                heapq.heappush(min_heap, (w2, v))
    
    print(total_cost)

if __name__ == "__main__":
    solve()