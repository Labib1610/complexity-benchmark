import sys
from collections import deque, defaultdict

def solve():
    data = sys.stdin.read().strip().split()
    if not data:
        return
    it = iter(data)
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
    
    # earliest possible slot for each job
    earliest = [1] * (n + 1)
    # queue of jobs with indegree 0, sorted by earliest slot
    q = []
    for i in range(1, n + 1):
        if indeg[i] == 0:
            q.append(i)
    
    # We'll use a min-heap by earliest slot
    import heapq
    heapq.heapify(q)
    
    slot = [0] * (n + 1)
    # capacity per slot
    cap = [M] * (T + 1)
    
    processed = 0
    while q:
        # pick job with smallest earliest slot
        u = heapq.heappop(q)
        # assign to earliest slot with capacity
        s = earliest[u]
        while s <= T and cap[s] == 0:
            s += 1
        if s > T:
            print("NO")
            return
        slot[u] = s
        cap[s] -= 1
        processed += 1
        
        for v in adj[u]:
            indeg[v] -= 1
            if indeg[v] == 0:
                earliest[v] = max(earliest[v], s + 1)
                heapq.heappush(q, v)
            else:
                # update earliest based on this predecessor
                earliest[v] = max(earliest[v], s + 1)
    
    if processed != n:
        print("NO")
        return
    
    print("YES")
    print(" ".join(str(slot[i]) for i in range(1, n + 1)))

if __name__ == "__main__":
    solve()