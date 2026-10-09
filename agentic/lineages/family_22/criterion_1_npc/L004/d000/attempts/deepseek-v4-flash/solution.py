import sys
import heapq

def solve():
    input_data = sys.stdin.read().strip().split()
    if not input_data:
        return
    it = iter(input_data)
    n = int(next(it))
    M = int(next(it))
    T = int(next(it))
    m = int(next(it))
    
    adj = [[] for _ in range(n + 1)]
    indeg = [0] * (n + 1)
    
    for _ in range(m):
        a = int(next(it))
        b = int(next(it))
        adj[a].append(b)
        indeg[b] += 1
    
    # If total capacity is less than number of relics, impossible
    if T * M < n:
        print("NO")
        return
    
    heap = []
    for i in range(1, n + 1):
        if indeg[i] == 0:
            heapq.heappush(heap, i)
    
    room_assignment = [0] * (n + 1)
    assigned_count = 0
    
    for room in range(1, T + 1):
        placed = 0
        # Place up to M relics in this room
        while placed < M and heap:
            node = heapq.heappop(heap)
            room_assignment[node] = room
            assigned_count += 1
            placed += 1
            
            for nxt in adj[node]:
                indeg[nxt] -= 1
                if indeg[nxt] == 0:
                    heapq.heappush(heap, nxt)
        
        if assigned_count == n:
            # All assigned, we can stop early
            break
    
    if assigned_count < n:
        print("NO")
        return
    
    # Check if all room numbers are within 1..T
    # They are by construction
    print("YES")
    print(" ".join(str(room_assignment[i]) for i in range(1, n + 1)))

if __name__ == "__main__":
    solve()