import sys
import heapq

def solve():
    data = list(map(int, sys.stdin.buffer.read().split()))
    if not data:
        return
    n, M, T, m = data[0], data[1], data[2], data[3]
    
    succ = [[] for _ in range(n + 1)]
    indeg = [0] * (n + 1)   # for scheduling
    indeg_topo = [0] * (n + 1) # for topological sort
    
    idx = 4
    for _ in range(m):
        a = data[idx]; b = data[idx + 1]; idx += 2
        succ[a].append(b)
        indeg[b] += 1
        indeg_topo[b] += 1
    
    # topological order and compute earliest
    earliest = [1] * (n + 1)
    q = []
    for i in range(1, n + 1):
        if indeg_topo[i] == 0:
            q.append(i)
    
    order = []
    head = 0
    while head < len(q):
        u = q[head]; head += 1
        order.append(u)
        for v in succ[u]:
            if earliest[u] + 1 > earliest[v]:
                earliest[v] = earliest[u] + 1
            indeg_topo[v] -= 1
            if indeg_topo[v] == 0:
                q.append(v)
    
    if len(order) != n:
        print("NO")
        return
    
    # compute latest via reverse topological order
    latest = [T] * (n + 1)
    for u in reversed(order):
        if succ[u]:
            best = T
            for v in succ[u]:
                if latest[v] - 1 < best:
                    best = latest[v] - 1
            latest[u] = best
        # else remains T
    
    for i in range(1, n + 1):
        if latest[i] < earliest[i]:
            print("NO")
            return
    
    # scheduling with EDF
    time = [0] * (n + 1)
    heap = []
    for i in range(1, n + 1):
        if indeg[i] == 0:
            heapq.heappush(heap, (latest[i], i)))
    
    for t in range(1, T + 1):
        if not heap:
            # no available jobs; maybe all done or waiting for predecessors
            # if all done, break; else impossible (cycle already checked)
            if all(time[i] != 0 for i in range(1, n + 1)):
                break
            continue
        
        # If the smallest latest among available is < t, it's already too late
        if heap[0][0] < t:
            print("NO")
            return
        
        # schedule up to M jobs
        for _ in range(M):
            if not heap:
                break
            latest_i, u = heapq.heappop(heap)
            time[u] = t
            for v in succ[u]:
                indeg[v] -= 1
                if indeg[v] == 0:
                    heapq.heappush(heap, (latest[v], v))
    
    if any(time[i] == 0 for i in range(1, n + 1)):
        print("NO")
        return
    
    print("YES")
    print(" ".join(str(time[i]) for i in range(1, n + 1)))

if __name__ == "__main__":
    solve()