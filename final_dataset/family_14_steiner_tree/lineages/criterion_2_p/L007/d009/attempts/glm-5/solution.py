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
    
    target_indices = set()
    for _ in range(t):
        target_indices.add(int(next(it)))
    
    adj = [[] for _ in range(n + 1)]
    for _ in range(m):
        u = int(next(it))
        v = int(next(it))
        w = int(next(it))
        adj[u].append((v, w))
        adj[v].append((u, w))
    
    # Prim's algorithm to find MST
    # Start from any target node
    start = next(iter(target_indices))
    in_mst = [False] * (n + 1)
    min_heap = [(0, start)]
    total_cost = 0
    
    while min_heap:
        w, u = heapq.heappop(min_heap)
        if in_mst[u]:
            continue
        in_mst[u] = True
        total_cost += w
        for v, weight in adj[u]:
            if not in_mst[v]:
                heapq.heappush(min_heap, (weight, v))
    
    print(total_cost)

if __name__ == "__main__":
    solve()