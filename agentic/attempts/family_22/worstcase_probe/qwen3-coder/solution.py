from collections import defaultdict, deque

def solve():
    n, M, T, m = map(int, input().split())
    
    # Build graph
    graph = defaultdict(list)
    indegree = [0] * (n + 1)
    
    for _ in range(m):
        a, b = map(int, input().split())
        graph[a].append(b)
        indegree[b] += 1
    
    # Topological sort with slot assignment
    # We use Kahn's algorithm, but we need to be careful about slot assignments
    
    # Initialize queue with nodes having indegree 0
    queue = deque()
    for i in range(1, n + 1):
        if indegree[i] == 0:
            queue.append(i)
    
    # slot[i] represents the slot assigned to job i (1-indexed)
    slots = [0] * (n + 1)
    
    # For each slot, we track how many jobs are assigned to it
    slot_count = [0] * (T + 1)
    
    # pred_slot[i] is the earliest slot that job i can start based on its predecessors
    pred_slot = [1] * (n + 1)
    
    completed = 0
    
    while queue:
        # Process jobs in topological order
        current_jobs = list(queue)
        queue.clear()
        
        # Sort jobs to have deterministic behavior
        current_jobs.sort()
        
        # Assign slots to current jobs
        for job in current_jobs:
            # Find the first available slot >= pred_slot[job]
            slot_assigned = False
            for slot in range(pred_slot[job], T + 1):
                if slot_count[slot] < M:
                    slots[job] = slot
                    slot_count[slot] += 1
                    slot_assigned = True
                    break
            
            if not slot_assigned:
                print("NO")
                return
            
            completed += 1
            
            # Update successors
            for neighbor in graph[job]:
                indegree[neighbor] -= 1
                # The successor must start after this job finishes
                # If job finishes at slot, it's available from slot+1
                pred_slot[neighbor] = max(pred_slot[neighbor], slots[job] + 1)
                
                if indegree[neighbor] == 0:
                    queue.append(neighbor)
    
    if completed != n:
        print("NO")
        return
    
    print("YES")
    print(*slots[1:])

solve()