import sys
import heapq

def solve():
    data = sys.stdin.read().strip().split()
    if not data:
        return
    it = iter(data)
    j = int(next(it))
    m = int(next(it))
    
    docs = []
    for _ in range(j):
        o = int(next(it))
        reviews = []
        for _ in range(o):
            official = int(next(it))
            duration = int(next(it))
            reviews.append((official, duration))
        docs.append(reviews)
    
    # Each review: (doc_index, review_index)
    # We'll keep track of next review index for each doc
    next_idx = [0] * j
    # official_available_time
    avail = [0] * (m + 1)
    
    # Min-heap: (start_time, doc_idx, review_idx, duration, official)
    heap = []
    
    # Initialize with first review of each doc
    for d in range(j):
        off, dur = docs[d][0]
        heapq.heappush(heap, (0, d, 0, dur, off))
    
    max_finish = 0
    
    while heap:
        start, d, r, dur, off = heapq.heappop(heap)
        # Earliest start is max(prev finish of this doc, official available)
        # But we already pushed with start = max(prev_finish, avail[off]) at push time
        finish = start + dur
        max_finish = max(max_finish, finish)
        # Update official availability
        avail[off] = finish
        # Schedule next review of this doc if any
        next_idx[d] += 1
        if next_idx[d] < len(docs[d]):
            n_off, n_dur = docs[d][next_idx[d]]
            n_start = max(finish, avail[n_off])
            heapq.heappush(heap, (n_start, d, next_idx[d], n_dur, n_off))
    
    print(max_finish)

if __name__ == "__main__":
    solve()