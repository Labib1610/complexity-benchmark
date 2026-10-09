from collections import defaultdict, deque

def solve():
    j, m = map(int, input().split())
    
    # Parse sequences
    sequences = []
    for _ in range(j):
        line = list(map(int, input().split()))
        o = line[0]
        steps = []
        for i in range(o):
            instrument = line[1 + 2*i]
            duration = line[1 + 2*i + 1]
            steps.append((instrument, duration))
        sequences.append(steps)
    
    # For each sequence, we'll track which step it's on and when it can start next step
    # For each instrument, we'll track when it becomes free
    
    # Initialize: when each instrument becomes free
    instrument_free_time = [0] * (m + 1)  # 1-indexed
    
    # For each sequence, track current step index and earliest time it can start next step
    sequence_state = [(0, 0) for _ in range(j)]  # (current_step_index, earliest_start_time_for_next_step)
    
    # Total number of steps
    total_steps = sum(len(seq) for seq in sequences)
    completed_steps = 0
    
    # Keep track of when each sequence completes
    sequence_completion_times = [0] * j
    
    while completed_steps < total_steps:
        # Find the next step that can be scheduled
        best_seq = -1
        best_instrument = -1
        best_duration = -1
        best_start_time = float('inf')
        
        # Check all sequences for their next possible step
        for seq_idx in range(j):
            step_idx, earliest_start = sequence_state[seq_idx]
            if step_idx >= len(sequences[seq_idx]):
                continue  # This sequence is done
                
            instrument, duration = sequences[seq_idx][step_idx]
            # This step can start at max(earliest_start, instrument_free_time[instrument])
            start_time = max(earliest_start, instrument_free_time[instrument])
            
            # We want to schedule something, but we'll pick one that starts earliest
            if start_time < best_start_time:
                best_start_time = start_time
                best_seq = seq_idx
                best_instrument = instrument
                best_duration = duration
        
        # If we couldn't find any step, break (shouldn't happen with valid input)
        if best_seq == -1:
            break
            
        # Schedule this step
        start_time = best_start_time
        end_time = start_time + best_duration
        
        # Update instrument's free time
        instrument_free_time[best_instrument] = end_time
        
        # Update sequence state
        step_idx, _ = sequence_state[best_seq]
        if step_idx + 1 < len(sequences[best_seq]):
            # There's a next step, which can earliest start at end_time
            sequence_state[best_seq] = (step_idx + 1, end_time)
        else:
            # Sequence is complete
            sequence_state[best_seq] = (step_idx + 1, end_time)
            sequence_completion_times[best_seq] = end_time
            
        completed_steps += 1
    
    # The answer is the maximum completion time among all sequences
    print(max(sequence_completion_times))

solve()