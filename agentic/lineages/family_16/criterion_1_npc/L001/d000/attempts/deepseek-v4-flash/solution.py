import sys
import heapq

def solve():
    input_data = sys.stdin.read().strip().split()
    idx = 0
    j = int(input_data[idx]); idx += 1
    m = int(input_data[idx]); idx += 1
    
    docs = []
    for _ in range(j):
        o = int(input_data[idx]); idx += 1
        reviews = []
        for _ in range(o):
            official = int(input_data[idx]); idx += 1
            duration = int(input_data[idx]); idx += 1
            reviews.append((official, duration))
        docs.append(reviews)
    
    # For each document, track next review index
    next_review = [0] * j
    # For each official, track when they become free
    free_time = [0] * (m + 1)
    
    # Min-heap: (available_time, doc_index)
    # Initially all docs can start their first review at time 0
    heap = []
    for d in range(j):
        if docs[d]:
            heapq.heappush(heap, (0, d))
    
    max_finish = 0
    
    while heap:
        t, d = heapq.heappop(heap)
        if next_review[d] >= len(docs[d]):
            continue
        official, dur = docs[d][next_review[d]]
        start = max(t, free_time[official])
        finish = start + dur
        free_time[official] = finish
        next_review[d] += 1
        max_finish = max(max_finish, finish)
        if next_review[d] < len(docs[d]):
            heapq.heappush(heap, (finish, d))
    
    print(max_finish)

if __name__ == "__main__":
    solve()