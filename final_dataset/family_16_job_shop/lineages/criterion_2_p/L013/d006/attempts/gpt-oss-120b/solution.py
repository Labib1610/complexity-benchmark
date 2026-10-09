import sys, heapq

def feasible(T, items):
    # each item: (p1, d) where d = p1 - p2
    # deadline = T - p1
    arr = [(T - p1, d) for p1, d in items]
    arr.sort()                     # sort by deadline ascending
    cur = 0
    heap = []                      # max-heap of d (store -d)
    for deadline, d in arr:
        cur += d
        heapq.heappush(heap, -d)   # push negative to simulate max-heap
        if cur > deadline:
            # move the job with largest d to later (remove its contribution)
            largest = -heapq.heappop(heap)
            cur -= largest
            # if after removal cur still exceeds deadline, continue removing
            while cur > deadline:
                if not heap:
                    return False
                largest = -heapq.heappop(heap)
                cur -= largest
    return True

def solve() -> None:
    data = sys.stdin.read().strip().split()
    if not data:
        return
    it = iter(data)
    n = int(next(it))
    items = []
    total_p2 = 0
    max_single = 0
    for _ in range(n):
        p1 = int(next(it)); p2 = int(next(it))
        d = p1 - p2
        items.append((p1, d))
        total_p2 += p2
        max_single = max(max_single, p1 + p2)
    low = max_single
    high = sum(p1 for p1, _ in items) + total_p2
    while low < high:
        mid = (low + high) // 2
        if feasible(mid, items):
            high = mid
        else:
            low = mid + 1
    print(low)

if __name__ == "__main__":
    solve()