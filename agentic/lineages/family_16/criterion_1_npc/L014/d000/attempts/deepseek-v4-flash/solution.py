import sys
import heapq

def can_finish(queries, m, limit):
    # Each query: list of (resource, duration)
    j = len(queries)
    # next step index for each query
    next_step = [0] * j
    # time when each query's next step can start (after previous step finishes)
    query_ready = [0] * j
    # resource free time
    res_free = [0] * (m + 1)
    
    # Min-heap of (start_time, query_idx)
    heap = []
    for qi in range(j):
        if next_step[qi] < len(queries[qi]):
            heapq.heappush(heap, (query_ready[qi], qi))
    
    while heap:
        start, qi = heapq.heappop(heap)
        if start > limit:
            return False
        res, dur = queries[qi][next_step[qi]]
        # Earliest this step can start
        s = max(start, res_free[res])
        if s + dur > limit:
            return False
        # Update resource and query state
        res_free[res] = s + dur
        query_ready[qi] = s + dur
        next_step[qi] += 1
        if next_step[qi] < len(queries[qi]):
            heapq.heappush(heap, (query_ready[qi], qi))
    return True

def main():
    data = sys.stdin.read().strip().split()
    idx = 0
    j = int(data[idx]); idx += 1
    m = int(data[idx]); idx += 1
    queries = []
    for _ in range(j):
        o = int(data[idx]); idx += 1
        steps = []
        for _ in range(o):
            r = int(data[idx]); idx += 1
            d = int(data[idx]); idx += 1
            steps.append((r, d))
        queries.append(steps)
    
    lo, hi = 0, 10**9
    while lo < hi:
        mid = (lo + hi) // 2
        if can_finish(queries, m, mid):
            hi = mid
        else:
            lo = mid + 1
    print(lo)

if __name__ == "__main__":
    main()