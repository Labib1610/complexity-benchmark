import sys
import heapq

def main():
    data = sys.stdin.read().strip().split()
    if not data:
        return
    idx = 0
    j = int(data[idx]); idx += 1
    m = int(data[idx]); idx += 1
    
    sequences = []
    for _ in range(j):
        o = int(data[idx]); idx += 1
        steps = []
        for _ in range(o):
            inst = int(data[idx]); idx += 1
            dur = int(data[idx]); idx += 1
            steps.append((inst, dur))
        sequences.append(steps)
    
    # For each sequence, track next step index
    next_step = [0] * j
    # Track when each instrument becomes free
    free_at = [0] * (m + 1)
    
    # Min-heap of (finish_time, seq_idx)
    heap = []
    
    # Initialize: start first step of each sequence if possible
    for s in range(j):
        inst, dur = sequences[s][0]
        start = max(free_at[inst], 0)
        finish = start + dur
        free_at[inst] = finish
        next_step[s] = 1
        heapq.heappush(heap, (finish, s))
    
    max_finish = 0
    
    while heap:
        finish_time, s = heapq.heappop(heap)
        max_finish = max(max_finish, finish_time)
        if next_step[s] < len(sequences[s]):
            inst, dur = sequences[s][next_step[s]]
            start = max(free_at[inst], finish_time)
            finish = start + dur
            free_at[inst] = finish
            next_step[s] += 1
            heapq.heappush(heap, (finish, s))
    
    print(max_finish)

if __name__ == "__main__":
    main()