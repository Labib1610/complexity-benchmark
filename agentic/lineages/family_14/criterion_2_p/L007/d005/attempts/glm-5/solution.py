import sys
import heapq

def solve():
    input_data = sys.stdin.read().split()
    if not input_data:
        return
    it = iter(input_data)
    
    try:
        n = int(next(it))
        m = int(next(it))
        t = int(next(it))
    except StopIteration:
        return
    
    target = set()
    for _ in range(t):
        try:
            target.add(int(next(it)))
        except StopIteration:
            return
    
    adj = [[] for _ in range(n + 1)]
    for _ in range(m):
        try:
            u = int(next(it))
            v = int(next(it))
            w = int(next(it))
            adj[u].append((v, w))
            adj[v].append((u, w))
        except StopIteration:
            break
    
    # Prim's algorithm to find MST
    # Start from any target node
    if t == 0:
        print(0)
        return
    
    start = next(iter(target))
    in_mst = [False] * (n + 1)
    min_edge = [float('inf')] * (n + 1)
    min_edge[start] = 0
    
    heap = [(0, start)]
    total_cost = 0
    
    while heap:
        cost, u = heapq.heappop(heap)
        if in_mst[u]:
            continue
        in_mst[u] = True
        total_cost += cost
        
        for v, w in adj[u]:
            if not in_mst[v] and w < min_edge[v]:
                min_edge[v] = w
                heapq.heappush(heap, (w, v))
    
    print(total_cost)

if __name__ == "__main__":
    solve()