import sys

def solve():
    input_data = sys.stdin.read().split()
    if not input_data:
        return
    
    j = int(input_data[0])
    m = int(input_data[1])
    
    queries = []
    idx = 2
    for _ in range(j):
        o = int(input_data[idx])
        idx += 1
        steps = []
        for _ in range(o):
            res = int(input_data[idx]) - 1
            dur = int(input_data[idx+1])
            steps.append((res, dur))
            idx += 2
        queries.append(steps)
        
    # Each state is a tuple of (current_step_index, start_time) for each query
    # start_time is the earliest time the current step is ready to start
    initial_state = tuple((0, 0) for _ in range(j))
    
    # Priority queue for Dijkstra: (finish_time, state)
    pq = [(0, initial_state)]
    visited = {initial_state: 0}
    
    while pq:
        finish_time, state = pq.pop(0) # Using list as priority queue (sufficient for small state space)
        
        # Check if all queries are finished
        if all(step_idx == len(queries[q]) for q, (step_idx, _) in enumerate(state)):
            print(finish_time)
            return
            
        # Find all queries that are ready to execute their next step
        ready_queries = []
        for q, (step_idx, start_time) in enumerate(state):
            if step_idx < len(queries[q]):
                ready_queries.append((q, step_idx, start_time))
                
        # Generate all valid subsets of ready queries (no two queries using the same resource)
        # We use a bitmask approach to find maximal independent sets
        for mask in range(1, 1 << len(ready_queries)):
            used_resources = set()
            valid = True
            subset = []
            
            for i in range(len(ready_queries)):
                if mask & (1 << i):
                    q, step_idx, start_time = ready_queries[i]
                    res, dur = queries[q][step_idx]
                    if res in used_resources:
                        valid = False
                        break
                    used_resources.add(res)
                    subset.append((q, step_idx, start_time, res, dur))
            
            if not valid:
                continue
                
            # Check if this subset is maximal (cannot add any more ready queries without resource conflict)
            is_maximal = True
            for i in range(len(ready_queries)):
                if not (mask & (1 << i)):
                    q, step_idx, start_time = ready_queries[i]
                    res, _ = queries[q][step_idx]
                    if res not in used_resources:
                        is_maximal = False
                        break
            
            if not is_maximal:
                continue
                
            # Calculate the finish time for this subset
            max_finish = finish_time
            for q, step_idx, start_time, res, dur in subset:
                actual_start = max(start_time, finish_time)
                max_finish = max(max_finish, actual_start + dur)
                
            # Generate the next state
            next_state_list = list(state)
            for q, step_idx, start_time, res, dur in subset:
                actual_start = max(start_time, finish_time)
                next_state_list[q] = (step_idx + 1, actual_start + dur)
                
            next_state = tuple(next_state_list)
            
            if next_state not in visited or visited[next_state] > max_finish:
                visited[next_state] = max_finish
                pq.append((max_finish, next_state))
                pq.sort() # Re-sort to act as a priority queue

if __name__ == '__main__':
    solve()