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
    
    adj = [[] for _ in range(n)]
    indeg = [0] * n
    
    for _ in range(m):
        a = int(next(it)) - 1
        b = int(next(it)) - 1
        adj[a].append(b)
        indeg[b] += 1
    
    # Min-heap of available nodes (in-degree 0)
    heap = []
    for i in range(n):
        if indeg[i] == 0:
            heapq.heappush(heap, i)
    
    shift_assignment = [0] * n
    assigned = 0
    
    for shift in range(1, T + 1):
        if assigned == n:
            break
        # Take up to M nodes for this shift
        current = []
        for _ in range(M):
            if not heap:
                break
            node = heapq.heappop(heap)
            current.append(node)
            shift_assignment[node] = shift
            assigned += 1
        
        if not current:
            # No progress possible
            break
        
        # Update in-degrees
        for node in current:
            for nxt in adj[node]:
                indeg[nxt] -= 1
                if indeg[nxt] == 0:
                    heapq.heappush(heap, nxt)
    
    if assigned == n:
        print("YES")
        print(" ".join(str(x) for x in shift_assignment))
    else:
        print("NO")

if __name__ == "__main__":
    solve()