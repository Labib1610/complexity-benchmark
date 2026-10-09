import sys
import heapq

def solve():
    input_data = sys.stdin.read().strip().split()
    idx = 0
    
    j = int(input_data[idx]); idx += 1
    m = int(input_data[idx]); idx += 1
    
    sequences = []
    for _ in range(j):
        o = int(input_data[idx]); idx += 1
        seq = []
        for _ in range(o):
            emitter = int(input_data[idx]); idx += 1
            duration = int(input_data[idx]); idx += 1
            seq.append((emitter, duration))
        sequences.append(seq)
    
    # Each emitter's next available time
    emitter_free = [0] * (m + 1)
    
    # For each sequence, track its current time
    seq_time = [0] * j
    
    # We'll process sequences in order, but we can also use a priority queue
    # to always pick the sequence with the smallest current time.
    # However, since sequences are independent except for emitter conflicts,
    # we can just simulate each sequence step by step.
    
    # We'll use a min-heap of (current_time, seq_index, step_index)
    heap = []
    for i in range(j):
        if sequences[i]:
            emitter, duration = sequences[i][0]
            heapq.heappush(heap, (0, i, 0))
    
    max_time = 0
    
    while heap:
        cur_time, seq_idx, step_idx = heapq.heappop(heap)
        emitter, duration = sequences[seq_idx][step_idx]
        
        # Wait for emitter to be free
        start_time = max(cur_time, emitter_free[emitter])
        finish_time = start_time + duration
        emitter_free[emitter] = finish_time
        
        max_time = max(max_time, finish_time)
        
        # Move to next step in this sequence
        if step_idx + 1 < len(sequences[seq_idx]):
            heapq.heappush(heap, (finish_time, seq_idx, step_idx + 1))
    
    print(max_time)

if __name__ == "__main__":
    solve()