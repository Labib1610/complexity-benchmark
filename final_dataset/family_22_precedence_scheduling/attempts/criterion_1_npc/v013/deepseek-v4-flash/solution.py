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
    
    # min-heap of (earliest_time, task_index)
    heap = []
    for i in range(n):
        if indeg[i] == 0:
            heapq.heappush(heap, (1, i))
    
    schedule = [0] * n
    assigned = 0
    
    for t in range(1, T + 1):
        if not heap:
            break
        # take up to M tasks
        batch = []
        for _ in range(M):
            if not heap:
                break
            earliest, task = heapq.heappop(heap)
            if earliest > t:
                # cannot schedule this task now, put back and stop
                heapq.heappush(heap, (earliest, task))
                break
            schedule[task] = t
            assigned += 1
            batch.append(task)
        
        # update dependencies
        for task in batch:
            for nxt in adj[task]:
                indeg[nxt] -= 1
                if indeg[nxt] == 0:
                    heapq.heappush(heap, (t + 1, nxt))
    
    if assigned == n:
        print("YES")
        print(" ".join(map(str, schedule)))
    else:
        print("NO")

if __name__ == "__main__":
    solve()