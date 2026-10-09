from collections import defaultdict, deque
import sys

def main():
    import sys
    input = sys.stdin.read
    data = input().split()
    
    idx = 0
    j = int(data[idx])
    idx += 1
    m = int(data[idx])
    idx += 1
    
    jobs = []
    total_ops = 0
    for _ in range(j):
        o = int(data[idx])
        idx += 1
        ops = []
        for _ in range(o):
            machine = int(data[idx])
            idx += 1
            duration = int(data[idx])
            idx += 1
            ops.append((machine, duration))
        jobs.append(ops)
        total_ops += o

    # We'll use a backtracking approach with pruning
    # State: for each job, we track which operation index it's at
    # For each machine, we track when it becomes free
    
    # Precompute job precedence constraints
    # For each job, operation i must finish before operation i+1 starts
    # So we need to track end times per job
    
    # Let's model this as a state-space search with memoization
    # But given small constraints, we can try all permutations respecting constraints
    
    # Better approach: since order within jobs is fixed, we can think of this as scheduling
    # a set of operations with dependencies. This is a classic Job Shop Scheduling problem.
    # We can solve it with branch and bound or backtracking with pruning.
    
    # Let's implement a recursive backtracking solution with pruning
    
    # Global variables for backtracking
    min_time = [float('inf')]
    
    # For each job, track the current operation index and earliest start time
    # For each machine, track the timeline of usage (list of (start, end) intervals)
    
    def backtrack(job_op_indices, machine_timelines, current_max_time):
        # job_op_indices[i] = next operation index for job i
        # machine_timelines[m] = list of (start, end) when machine m is busy
        # current_max_time = current makespan
        
        if current_max_time >= min_time[0]:
            return  # Pruning
        
        # Check if all jobs are done
        all_done = True
        for i in range(j):
            if job_op_indices[i] < len(jobs[i]):
                all_done = False
                break
        if all_done:
            min_time[0] = min(min_time[0], current_max_time)
            return
            
        # Find all possible next operations
        # An operation can be scheduled if:
        # 1. Its job's previous operation is done
        # 2. Its machine is free during the required time interval
        
        candidates = []
        for job_id in range(j):
            op_idx = job_op_indices[job_id]
            if op_idx >= len(jobs[job_id]):
                continue
            machine, duration = jobs[job_id][op_idx]
            
            # Earliest time this operation can start is:
            # max(current time, when the machine is free, when previous operation of this job finishes)
            prev_end_time = 0
            if op_idx > 0:
                # We need to know when the previous operation of this job ended
                # This is tricky in our current state representation
                # Let's restructure: keep track of end times for each job
                pass
                
            # Actually, let's keep track of end times for each job
            # job_end_times[i] = time when job i's last operation finished
            # Then for job i, operation op_idx can start at max(job_end_times[i], earliest machine free time)
                
        # Let's restructure the state
        # We'll pass in job_end_times: list where job_end_times[i] is when job i last finished
        # And machine_timelines as before
        
    # Let's restart with better state representation
    min_time[0] = float('inf')
    
    # job_positions[i] = index of next operation for job i
    # job_end_times[i] = time when job i's last operation finished
    # machine_next_free[m] = time when machine m becomes free
    
    def get_machine_next_free(machine_timelines, machine):
        # machine_timelines[machine] is list of (start, end)
        # return the time when machine becomes free
        if not machine_timelines[machine]:
            return 0
        return machine_timelines[machine][-1][1]
        
    def find_earliest_slot(machine_timelines, machine, duration, start_after):
        # Find earliest time >= start_after when machine is free for 'duration' time units
        intervals = machine_timelines[machine]
        t = start_after
        # Simple greedy check - check if [t, t+duration] is free
        # Since intervals are added in order, we can just check conflicts
        while True:
            end_t = t + duration
            conflict = False
            for (s, e) in intervals:
                if not (end_t <= s or t >= e):  # overlap
                    t = e  # jump to end of this interval
                    conflict = True
                    break
            if not conflict:
                return t
            if t > min_time[0]:  # Pruning
                return None
                
    def backtrack_v2(job_positions, job_end_times, machine_timelines, current_max_time):
        if current_max_time >= min_time[0]:
            return
            
        # Check if done
        done = True
        for i in range(j):
            if job_positions[i] < len(jobs[i]):
                done = False
                break
        if done:
            min_time[0] = min(min_time[0], current_max_time)
            return
            
        # Try to schedule next operation for each job
        for job_id in range(j):
            op_idx = job_positions[job_id]
            if op_idx >= len(jobs[job_id]):
                continue
            machine, duration = jobs[job_id][op_idx]
            
            # Earliest this op can start is max of:
            # 1. When the job's previous op finished (job_end_times[job_id])
            # 2. When the machine is free
            earliest_start = job_end_times[job_id]
            # Now check machine availability
            start_time = find_earliest_slot(machine_timelines, machine, duration, earliest_start)
            if start_time is None or start_time > min_time[0]:
                continue
                
            end_time = start_time + duration
            
            # Make the move
            job_positions[job_id] += 1
            old_job_end = job_end_times[job_id]
            job_end_times[job_id] = end_time
            machine_timelines[machine].append((start_time, end_time))
            new_max_time = max(current_max_time, end_time)
            
            # Recurse
            backtrack_v2(job_positions, job_end_times, machine_timelines, new_max_time)
            
            # Undo the move
            job_positions[job_id] -= 1
            job_end_times[job_id] = old_job_end
            machine_timelines[machine].pop()
            
    # Initial call
    initial_positions = [0] * j
    initial_end_times = [0] * j
    initial_machine_timelines = [[] for _ in range(m+1)]  # 1-indexed
    
    backtrack_v2(initial_positions, initial_end_times, initial_machine_timelines, 0)
    
    print(min_time[0])

if __name__ == "__main__":
    main()