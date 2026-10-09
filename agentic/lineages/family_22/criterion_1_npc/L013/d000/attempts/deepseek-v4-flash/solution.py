from collections import deque
import sys

def solve():
    input_data = sys.stdin.read().strip().split()
    if not input_data:
        return
    it = iter(input_data)
    n = int(next(it))
    M = int(next(it))
    T = int(next(it))
    m = int(next(it))
    
    adj = [[] for _ in range(n+1)]
    indeg = [0]*(n+1)
    
    for _ in range(m):
        a = int(next(it))
        b = int(next(it))
        adj[a].append(b)
        indeg[b] += 1
    
    # queue of available modules
    avail = [i for i in range(1, n+1) if indeg[i] == 0]
    avail.sort()
    
    term_assign = [0]*(n+1)
    done_count = 0
    
    # We can use a min-heap for stable ordering if needed
    import heapq
    heapq.heapify(avail)
    
    for term in range(1, T+1):
        if done_count == n:
            break
        # take up to M modules
        take = []
        while len(take) < M and avail:
            node = heapq.heappop(avail)
            take.append(node)
        if not take:
            # nothing available, but we still might have modules left
            # means impossible before deadline
            continue
        for node in take:
            term_assign[node] = term
            done_count += 1
            for nb in adj[node]:
                indeg[nb] -= 1
                if indeg[nb] == 0:
                    heapq.heappush(avail, nb)
    
    if done_count < n:
        print("NO")
    else:
        print("YES")
        print(" ".join(str(term_assign[i]) for i in range(1, n+1)))

if __name__ == "__main__":
    solve()