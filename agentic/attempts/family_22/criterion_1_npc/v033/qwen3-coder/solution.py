from collections import defaultdict, deque

def main():
    import sys
    input = sys.stdin.read
    data = input().split()
    
    n, M, T, m = map(int, data[:4])
    edges = []
    for i in range(m):
        a = int(data[4 + 2*i])
        b = int(data[4 + 2*i + 1])
        edges.append((a, b))
    
    # Build graph
    graph = defaultdict(list)
    indegree = [0] * (n + 1)
    for a, b in edges:
        graph[a].append(b)
        indegree[b] += 1
    
    # Topological sort with slot assignment
    # We use a greedy approach: assign the earliest possible slot
    slot = [0] * (n + 1)
    queue = deque()
    
    # Find all nodes with indegree 0
    for i in range(1, n + 1):
        if indegree[i] == 0:
            queue.append(i)
    
    # For each time slot, we track how many tasks are scheduled
    # We'll simulate the scheduling process
    # slot_count[t] = number of tasks in slot t (1-based)
    slot_count = [0] * (T + 1)  # index 0 unused
    
    # We'll do a topological sort while respecting slot constraints
    # For each node, we track the earliest slot it can start based on its dependencies
    earliest_start = [1] * (n + 1)
    
    # Process nodes in topological order
    temp_queue = deque(queue)
    while temp_queue:
        u = temp_queue.popleft()
        # For each neighbor v of u
        for v in graph[u]:
            # v must come after u, so earliest start of v is at least slot[u] + 1
            earliest_start[v] = max(earliest_start[v], slot[u] + 1)
            indegree[v] -= 1
            if indegree[v] == 0:
                temp_queue.append(v)
    
    # Now we try to assign slots respecting both topological order and capacity constraints
    # Reset indegree for actual scheduling
    indegree = [0] * (n + 1)
    for a, b in edges:
        indegree[b] += 1
        
    queue = deque()
    for i in range(1, n + 1):
        if indegree[i] == 0:
            queue.append(i)
            
    # Try to schedule tasks respecting both precedence and capacity
    scheduled = [False] * (n + 1)
    slot = [0] * (n + 1)
    
    # We'll process in rounds up to T time slots
    current_slot = 1
    tasks_scheduled_in_current_slot = 0
    
    # Keep a list of ready tasks (indegree == 0 and not yet scheduled)
    ready = []
    
    # Initially populate ready list
    for i in range(1, n + 1):
        if indegree[i] == 0:
            ready.append(i)
    
    while ready or current_slot <= T:
        # Sort ready tasks to have consistent behavior
        ready.sort()
        
        # Try to schedule as many as possible in current slot without exceeding M
        scheduled_now = 0
        new_ready = []
        
        for task in ready:
            if scheduled_now >= M:
                new_ready.append(task)
                continue
            # Schedule this task in current_slot
            slot[task] = current_slot
            scheduled[task] = True
            scheduled_now += 1
            
            # Update neighbors
            for v in graph[task]:
                indegree[v] -= 1
                if indegree[v] == 0:
                    new_ready.append(v)
        
        # Move to next slot if current is full or no more tasks can be scheduled now
        current_slot += 1
        ready = new_ready
        
        if current_slot > T and ready:
            print("NO")
            return
            
        if all(scheduled[i] for i in range(1, n+1)):
            break
    
    # Check if all tasks were scheduled
    if not all(scheduled[i] for i in range(1, n+1)):
        print("NO")
        return
        
    print("YES")
    print(' '.join(map(str, slot[1:])))

if __name__ == "__main__":
    main()