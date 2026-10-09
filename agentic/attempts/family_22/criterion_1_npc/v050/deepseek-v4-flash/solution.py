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
    
    section = [0] * n
    current_section = 1
    count_in_section = 0
    
    placed = 0
    while heap:
        if current_section > T:
            print("NO")
            return
        # Take as many as possible for this section
        next_batch = []
        while heap and count_in_section < M:
            u = heapq.heappop(heap)
            section[u] = current_section
            count_in_section += 1
            placed += 1
            next_batch.append(u)
        
        # After placing, reduce indegrees
        for u in next_batch:
            for v in adj[u]:
                indeg[v] -= 1
                if indeg[v] == 0:
                    heapq.heappush(heap, v)
        
        # Move to next section
        current_section += 1
        count_in_section = 0
    
    if placed != n:
        print("NO")
        return
    
    # Check if all sections are within T
    if max(section) > T:
        print("NO")
        return
    
    print("YES")
    print(" ".join(str(x) for x in section))

if __name__ == "__main__":
    solve()