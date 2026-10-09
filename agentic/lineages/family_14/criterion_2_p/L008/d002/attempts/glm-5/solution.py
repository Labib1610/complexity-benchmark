import sys
import heapq

def solve():
    input_data = sys.stdin.read().split()
    if not input_data:
        return
    iterator = iter(input_data)
    
    try:
        R = int(next(iterator))
        S = int(next(iterator))
        P = int(next(iterator))
    except StopIteration:
        return

    priority_rooms = set()
    for _ in range(P):
        try:
            priority_rooms.add(int(next(iterator)))
        except StopIteration:
            return
    
    adj = [[] for _ in range(R + 1)]
    for _ in range(S):
        try:
            u = int(next(iterator))
            v = int(next(iterator))
            w = int(next(iterator))
            adj[u].append((v, w))
            adj[v].append((u, w))
        except StopIteration:
            return

    # Prim's algorithm starting from all priority rooms
    min_heap = []
    in_mst = [False] * (R + 1)
    
    for node in priority_rooms:
        heapq.heappush(min_heap, (0, node))
    
    total_cost = 0
    nodes_in_mst = 0
    
    while min_heap:
        cost, u = heapq.heappop(min_heap)
        
        if in_mst[u]:
            continue
        
        in_mst[u] = True
        total_cost += cost
        nodes_in_mst += 1
        
        for v, w in adj[u]:
            if not in_mst[v]:
                heapq.heappush(min_heap, (w, v))
    
    print(total_cost)

if __name__ == "__main__":
    solve()