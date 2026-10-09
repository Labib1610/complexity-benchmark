import sys
from collections import defaultdict, deque
import heapq

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
    for _ in range(j):
        o = int(data[idx])
        idx += 1
        ops = []
        for _ in range(o):
            machine = int(data[idx]) - 1  # Convert to 0-based
            idx += 1
            duration = int(data[idx])
            idx += 1
            ops.append((machine, duration))
        jobs.append(ops)
    
    # Number of operations
    num_ops = sum(len(job) for job in jobs)
    
    # Create operation nodes
    # Each operation is identified by (job_id, op_id)
    # We also compute precedence constraints
    
    # Build a graph for job precedences
    # And also track machine usage
    
    # For each operation, we'll have a node
    # Let's assign each operation a unique id
    op_index = {}  # (job_id, op_id) -> node_id
    node_id_counter = 0
    
    # First, assign node ids
    for job_id in range(j):
        for op_id in range(len(jobs[job_id])):
            op_index[(job_id, op_id)] = node_id_counter
            node_id_counter += 1
    
    num_nodes = node_id_counter
    
    # Now build the graph
    # Edges represent dependencies: u -> v means v cannot start until u finishes
    adj = [[] for _ in range(num_nodes)]
    indegree = [0] * num_nodes
    
    # Job precedence: each operation in a job must follow the previous one
    for job_id in range(j):
        job = jobs[job_id]
        for op_id in range(len(job) - 1):
            u = op_index[(job_id, op_id)]
            v = op_index[(job_id, op_id + 1)]
            adj[u].append(v)
            indegree[v] += 1
    
    # Machine conflicts: for each machine, operations on it must be ordered
    # We need to find all operations on each machine and create a chain
    # However, we don't know the order yet, so we'll handle this via search
    
    # Instead, let's model this properly as a job shop scheduling problem
    # and use a branch-and-bound approach or A* with a good heuristic
    
    # But given the small constraints (up to 10 jobs, 10 machines, 50 operations),
    # we can try a more direct approach like branch-and-bound
    
    # Let's try a simpler approach: use a priority queue to explore states
    # State: (time, job_positions, machine_end_times)
    
    # job_positions: for each job, which operation it's on (or -1 if done)
    # machine_end_times: for each machine, when it becomes free
    
    # Initial state
    job_positions = [0] * j  # Each job starts at operation 0
    machine_end_times = [0] * m  # All machines are free at time 0
    # Compute initial possible start times
    # For each operation that can start now (operation 0 of each job)
    
    # To make state hashable, we need to use tuples
    # But priority queue can work with lists if we don't put them in sets
    # Actually, for A*, we might want to avoid revisiting states
    # But state space is huge: positions of jobs and machine end times
    
    # Let's think differently. Use a timeline simulation with backtracking
    # This is essentially exploring all valid schedules
    
    # Better idea: use a search where at each step, we choose which operation to schedule next
    # But we need to respect both job precedence and machine availability
    
    # Let's use a recursive backtracking with memoization
    # But state is complex
    
    # Let's try an A* approach
    # State: (job_positions_tuple, machine_end_times_tuple)
    # Heuristic: max(machine_end_times) + estimate of remaining work
    
    # Estimate: for each remaining operation, add its duration
    # But this is not admissible because operations might overlap
    
    # More accurate heuristic: for each machine, sum of durations of remaining operations on it
    # Then take max over machines
    
    def get_heuristic(job_pos, mach_end):
        # For each machine, calculate total remaining time
        mach_load = [0] * m
        for job_id in range(j):
            pos = job_pos[job_id]
            job = jobs[job_id]
            for op_id in range(pos, len(job)):
                machine, duration = job[op_id]
                mach_load[machine] += duration
        return max(mach_end) + max(mach_load) if mach_load else 0
    
    # Memoization might be too much, let's just do best-first search without cycle detection
    # due to state explosion
    
    # Priority queue: (f_score, time, job_positions_list, machine_end_times_list)
    pq = []
    
    initial_job_pos = tuple([0] * j)
    initial_mach_end = tuple([0] * m)
    h = get_heuristic(initial_job_pos, initial_mach_end)
    heapq.heappush(pq, (h, 0, initial_job_pos, initial_mach_end))
    
    # To avoid TLE, we might need to limit the search
    # But let's implement it cleanly first
    
    visited = set()
    
    while pq:
        f, time, job_pos, mach_end = heapq.heappop(pq)
        
        # Check if all jobs are done
        if all(job_pos[job_id] == len(jobs[job_id]) for job_id in range(j)):
            print(time)
            return
        
        # To avoid visiting same state, we can memoize
        # But state is (job_pos, mach_end), which is large
        # Let's skip memoization for now and hope the pruning works
        
        # Determine which operations can be scheduled now
        # An operation can be scheduled if:
        # 1. Its preceding operation (if any) is done
        # 2. Its machine is free at some time >= current time
        
        # For simplicity, let's look for operations that can start exactly at 'time'
        # No, better to look for all possible next operations and schedule each at the earliest possible time
        
        for job_id in range(j):
            pos = job_pos[job_id]
            if pos < len(jobs[job_id]):
                machine, duration = jobs[job_id][pos]
                # Earliest start time is max(current_time, machine_free_time)
                start_time = max(time, mach_end[machine])
                end_time = start_time + duration
                
                # Create new state
                new_job_pos = list(job_pos)
                new_job_pos[job_id] = pos + 1
                new_mach_end = list(mach_end)
                new_mach_end[machine] = end_time
                
                new_job_pos_t = tuple(new_job_pos)
                new_mach_end_t = tuple(new_mach_end)
                
                # Heuristic
                h_new = get_heuristic(new_job_pos_t, new_mach_end_t)
                f_new = end_time + h_new  # g = end_time, h = heuristic
                
                heapq.heappush(pq, (f_new, end_time, new_job_pos_t, new_mach_end_t))

if __name__ == "__main__":
    main()