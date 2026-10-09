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
    
    # min-heap of (earliest_slot, job_id)
    heap = []
    for i in range(1, n + 1):
        if indeg[i] == 0:
            heapq.heappush(heap, (1, i))
    
    slot = [0] * (n + 1)
    scheduled = 0
    
    for t in range(1, T + 1):
        # take up to M jobs that can start at or before t
        count = 0
        temp = []
        while heap and count < M:
            earliest, job = heapq.heappop(heap)
            if earliest <= t:
                slot[job] = t
                scheduled += 1
                count += 1
                # release successors
                for nxt in adj[job]:
                    indeg[nxt] -= 1
                    if indeg[nxt] == 0:
                        heapq.heappush(heap, (t + 1, nxt))
            else:
                temp.append((earliest, job))
                break
        # put back any not scheduled
        for item in temp:
            heapq.heappush(heap, item)
        # also push back any remaining from the while loop that were popped but not used
        # Actually the while loop only pops when count < M, so all popped are scheduled.
        # If we broke early, we already put back the one that was too early.
    
    if scheduled == n:
        print("YES")
        print(" ".join(str(slot[i]) for i in range(1, n + 1)))
    else:
        print("NO")

if __name__ == "__main__":
    solve()