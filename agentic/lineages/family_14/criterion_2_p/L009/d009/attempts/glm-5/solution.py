import sys
import heapq

def solve():
    input_data = sys.stdin.read().split()
    if not input_data:
        return
    
    iterator = iter(input_data)
    try:
        N = int(next(iterator))
        E = int(next(iterator))
        F = int(next(iterator))
    except StopIteration:
        return
    
    critical = []
    for _ in range(F):
        critical.append(int(next(iterator)))
    
    adj = [[] for _ in range(N + 1)]
    for _ in range(E):
        u = int(next(iterator))
        v = int(next(iterator))
        w = int(next(iterator))
        adj[u].append((v, w))
        adj[v].append((u, w))
    
    if F <= 1:
        print(0)
        return
    
    # Prim's algorithm to find MST
    total_cost = 0
    visited = [False] * (N + 1)
    min_edge = [float('inf')] * (N + 1)
    min_edge[1] = 0
    heap = [(0, 1)]
    
    while heap:
        w, u = heapq.heappop(heap)
        if visited[u]:
            continue
        visited[u] = True
        total_cost += w
        for v, weight in adj[u]:
            if not visited[v] and weight < min_edge[v]:
                min_edge[v] = weight
                heapq.heappush(heap, (weight, v))
    
    print(total_cost)

if __name__ == "__main__":
    solve()