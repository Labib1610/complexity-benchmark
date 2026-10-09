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
    
    # earliest shift for each node
    earliest = [1] * (n + 1)
    # heap entries: (earliest_shift, node)
    heap = []
    for i in range(1, n + 1):
        if indeg[i] == 0:
            heapq.heappush(heap, (1, i))
    
    shift_count = [0] * (T + 1)  # 1-indexed shifts
    assigned = [0] * (n + 1)
    processed = 0
    
    while heap:
        shift, u = heapq.heappop(heap)
        # find the actual shift respecting capacity
        while shift <= T and shift_count[shift] >= M:
            shift += 1
        if shift > T:
            print("NO")
            return
        assigned[u] = shift
        shift_count[shift] += 1
        processed += 1
        
        for v in adj[u]:
            indeg[v] -= 1
            if indeg[v] == 0:
                # earliest possible shift for v is at least shift+1
                heapq.heappush(heap, (shift + 1, v))
            else:
                # update earliest if needed (but we only push when indeg becomes 0)
                pass
    
    if processed != n:
        print("NO")
        return
    
    print("YES")
    print(" ".join(str(assigned[i]) for i in range(1, n + 1)))

if __name__ == "__main__":
    solve()