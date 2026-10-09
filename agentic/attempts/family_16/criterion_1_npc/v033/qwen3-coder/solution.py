from collections import defaultdict
import sys

def solve():
    j, m = map(int, input().split())
    
    queries = []
    for _ in range(j):
        line = list(map(int, input().split()))
        o = line[0]
        steps = []
        for i in range(o):
            resource = line[1 + 2*i]
            duration = line[1 + 2*i + 1]
            steps.append((resource, duration))
        queries.append(steps)
    
    # We'll try all possible orderings of queries on resources
    # But since j <= 10, we can model this as a scheduling problem
    
    # For each resource, maintain a list of time intervals when it's busy
    # Actually, let's think differently - we simulate the process
    
    # Let's use a greedy approach with backtracking or try all permutations
    # Since j is small (<= 10), we could try all permutations but that might be too much
    # Let's think of this as a job shop scheduling problem
    
    # Better approach: Use a simulation with priority queue
    # But actually, let's think of it this way:
    # At any time, we know which step of each query can potentially run
    # If its required resource is free, it can start
    
    # Let's simulate:
    # Keep track of when each resource becomes free
    # Keep track of where each query is in its processing
    
    # resources_free_time[r] = time when resource r becomes free (1-indexed)
    resources_free_time = [0] * (m + 1)
    
    # query_positions[q] = index of next step for query q (or len if done)
    query_positions = [0] * j
    
    # When each query finished its previous step
    query_step_finish_times = [0] * j
    
    # To make it optimal, we need to search through possibilities
    # But let's try a greedy simulation first
    
    # Actually, this is NP-hard (job shop scheduling) but with small inputs we can search
    
    # Let's do a recursive backtracking with memoization
    # State: for each query, how many steps have been completed
    
    def can_start_query_step(query_idx, step_idx):
        if step_idx >= len(queries[query_idx]):
            return False, 0
        resource, duration = queries[query_idx][step_idx]
        # This step can start at max(query_step_finish_times[query_idx], resources_free_time[resource])
        start_time = max(query_step_finish_times[query_idx], resources_free_time[resource])
        return True, start_time + duration
    
    # This greedy approach won't work optimally
    # We need to explore the state space
    
    # Let's define state as tuple of completion status
    # But better yet, let's enumerate all possible interleavings
    
    # With small constraints, we can model this as finding optimal schedule
    # Let's use BFS/DFS to find minimum time
    
    from functools import lru_cache
    
    # State: tuple of how many steps completed for each query
    @lru_cache(maxsize=None)
    def dp(state):
        # state is a tuple of completion counts for each query
        # Check if all queries are done
        all_done = True
        for q in range(j):
            if state[q] < len(queries[q]):
                all_done = False
                break
        if all_done:
            return 0
            
        # For current state, what's the earliest time something can happen?
        min_time = float('inf')
        
        # Try advancing each query by one step if possible
        for q in range(j):
            if state[q] < len(queries[q]):
                # Check if we can execute step state[q] of query q
                resource, duration = queries[q][state[q]]
                
                # Earliest this step can start:
                # 1. After this query's previous step finished
                # 2. After the resource is free
                prev_finish = 0 if state[q] == 0 else query_step_finish_times[q][state[q]-1]
                res_free = resources_free_time[resource]
                start_time = max(prev_finish, res_free)
                end_time = start_time + duration
                
                # Simulate doing this step
                new_state = list(state)
                new_state[q] = state[q] + 1
                new_state = tuple(new_state)
                
                # Update resource and query finish times for simulation
                old_res_free = resources_free_time[resource]
                old_query_finishes = query_step_finish_times[q][:] if hasattr(query_step_finish_times[q], '__getitem__') else []
                
                resources_free_time[resource] = end_time
                if not hasattr(query_step_finish_times[q], '__setitem__'):
                    query_step_finish_times[q] = [0] * len(queries[q])
                while len(query_step_finish_times[q]) <= state[q]:
                    query_step_finish_times[q].append(0)
                query_step_finish_times[q][state[q]] = end_time
                
                # Recursive call
                result = end_time + dp(new_state)
                min_time = min(min_time, result)
                
                # Restore state
                resources_free_time[resource] = old_res_free
                query_step_finish_times[q] = old_query_finishes
                
        return min_time if min_time != float('inf') else 0
    
    # Initialize tracking arrays properly
    global resources_free_time, query_step_finish_times
    resources_free_time = [0] * (m + 1)
    query_step_finish_times = [[] for _ in range(j)]
    
    # Let's re-implement with proper state tracking
    # Actually, let's just do a clean BFS implementation
    
    from heapq import heappush, heappop
    
    # State in priority queue: (current_time, resources_free_times, query_progress)
    initial_resources_free_time = tuple([0] * (m+1))
    initial_query_progress = tuple([0] * j)
    
    # (time, resources_free_time_tuple, query_progress_tuple)
    pq = [(0, initial_resources_free_time, initial_query_progress)]
    visited = set()
    
    while pq:
        time, res_free, query_prog = heappop(pq)
        state_key = (res_free, query_prog)
        
        if state_key in visited:
            continue
        visited.add(state_key)
        
        # Check if all queries are done
        done = True
        for q in range(j):
            if query_prog[q] < len(queries[q]):
                done = False
                break
        
        if done:
            print(time)
            return
            
        # Try to schedule next step of each query
        for q in range(j):
            if query_prog[q] < len(queries[q]):
                step_idx = query_prog[q]
                resource, duration = queries[q][step_idx]
                
                # When can this step start?
                # After previous step of same query finishes
                # After resource becomes free
                
                prev_finish_time = 0
                if step_idx > 0 and len(query_step_finish_times[q]) > step_idx - 1:
                    # This is complex to track without full simulation
                    
                    # Let's compute it based on current state
                    # We need to simulate forward from current state to see when things finish
                    
                    # Actually, let's simplify and reframe the whole approach
                    
                    # Since we're doing BFS, we should encode complete state correctly
                    
                    pass  # handled below in cleaner way
    
    # Cleaner DP approach:
    
    # Reset and do it right
    resources_free_time = [0] * (m + 1)
    query_positions = [0] * j
    query_last_finish = [0] * j
    
    # Actually, let's just implement a correct BFS
    
    # State: (current_time, resource_free_times, query_positions)
    # But this state is huge, let's think of a better way
    
    # Let's go back to the mathematical formulation
    
    # This is essentially a job shop scheduling problem J||C_max
    # For small instances, we can solve with branch and bound or complete search
    
    # Given the constraints are very small, let's do complete state exploration
    
    # Key insight: we only care about the order in which steps execute on each resource
    # For each resource, we have a sequence of steps that need to be scheduled on it
    # These sequences come from the queries
    
    # So for each query, we extract which steps use which resource
    resource_jobs = [[] for _ in range(m + 1)]  # resource_jobs[r] = list of (query_id, step_in_query, duration)
    
    for q in range(j):
        for step_idx, (resource, duration) in enumerate(queries[q]):
            resource_jobs[resource].append((q, step_idx, duration))
    
    # Now for each resource, the jobs in resource_jobs[r] must be ordered
    # But they also have dependencies within each query
    
    # This is getting complex. Let's try a different simulation approach.
    
    # Event-driven simulation:
    # Events: Step starts, Step ends
    # Track: Resource availability, Query progress
    
    # Actually, simplest correct solution for small input: 
    # Try all reasonable orderings with greedy scheduling
    
    # But even simpler for this constraint size: 
    # Just model it as finding shortest path in state space
    
    # State: (time, resource_free_times, query_positions)
    # But this has continuous time, so discretize by events
    
    # Let's just implement a working solution:
    
    def simulate_schedule(ordering):
        # ordering: for each resource, a list of which jobs use it in what order
        # This is still complex...
        
        # Let's just do a direct simulation with backtracking
        return 0
    
    # Brute force: try all timing decisions - impossible
    
    # Let's look at examples again:
    # Example 1: Two queries, each with steps (1,2), (2,2), (3,2)
    # Optimal schedule: Q1 and Q2 go in lockstep -> finish at 8
    
    # Example 3: One step (1,4) and one step (2,3) 
    # Can run in parallel -> finish at max(4,3) = 4
    
    # So we really need proper job-shop scheduling
    
    # For such small inputs, let's bit-mask DP or similar exhaustive method
    
    # But let's just implement a working solution for the given constraints:
    
    # Priority queue of events
    import heapq
    
    # (time, event_type, data)
    # event_type: 0=start, 1=end
    # For end events: which resource becomes free
    # For start events: which query-step starts  
    
    # Actually, let's think of the mathematical structure:
    # Each query is a chain of operations
    # Each resource can only do one thing at a time
    # Goal: minimize makespan
    
    # This is exactly what the problem asks for and it's solvable with 
    # critical path method + resource constrained scheduling for small cases
    
    # Let's hand-code the search:
    
    best_time = [float('inf')]
    
    def dfs(current_res_times, current_query_times, query_steps):
        # current_res_times[r]: when resource r becomes free
        # current_query_times[q]: when query q last step finished  
        # query_steps[q]: how many steps of query q completed
        
        # Check if done
        done = True
        for q in range(j):
            if query_steps[q] < len(queries[q]):
                done = False
                break
                
        max_time = max(current_res_times)
        if done:
            best_time[0] = min(best_time[0], max_time)
            return
            
        if max_time >= best_time[0]:
            return  # Pruning
            
        # Try to schedule next step of some query
        for q in range(j):
            if query_steps[q] < len(queries[q]):
                resource, duration = queries[q][query_steps[q]]
                
                # When can it start?
                # After previous step of this query
                # After resource is free
                prev_done_time = current_query_times[q]
                res_free_time = current_res_times[resource]
                start_time = max(prev_done_time, res_free_time)
                end_time = start_time + duration
                
                # Make new state
                new_res_times = list(current_res_times)
                new_query_times = list(current_query_times)  
                new_query_steps = list(query_steps)
                
                new_res_times[resource] = end_time
                new_query_times[q] = end_time
                new_query_steps[q] = query_steps[q] + 1
                
                dfs(tuple(new_res_times), tuple(new_query_times), tuple(new_query_steps))
    
    initial_res_times = tuple([0] * (m+1))
    initial_query_times = tuple([0] * j)
    initial_query_steps = tuple([0] * j)
    
    dfs(initial_res_times, initial_query_times, initial_query_steps)
    print(best_time[0])

solve()