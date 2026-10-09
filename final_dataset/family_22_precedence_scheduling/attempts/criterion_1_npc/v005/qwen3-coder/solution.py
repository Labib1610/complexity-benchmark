from collections import defaultdict, deque

def solve():
    n, M, T, m = map(int, input().split())
    
    # Build graph and in-degree count
    graph = defaultdict(list)
    in_degree = [0] * (n + 1)
    
    for _ in range(m):
        a, b = map(int, input().split())
        graph[a].append(b)
        in_degree[b] += 1
    
    # Topological sort with slot assignment
    # We use a greedy approach: assign each task to the earliest possible slot
    # considering both precedence and station capacity constraints
    
    # Find all nodes with in-degree 0
    queue = deque()
    for i in range(1, n + 1):
        if in_degree[i] == 0:
            queue.append(i)
    
    # slot[i] represents the slot assigned to task i
    slot = [0] * (n + 1)
    
    # For each slot, keep track of how many tasks are assigned
    slot_count = [0] * (T + 1)
    
    # Process tasks in topological order
    while queue:
        # For current slot, determine which tasks can be scheduled
        next_queue = deque()
        
        # Try to assign tasks to slots in a greedy manner
        temp_queue = list(queue)
        queue.clear()
        
        for node in temp_queue:
            # Find the earliest slot where this task can be placed
            # It must be after all its predecessors
            earliest_slot = 1
            for pred in graph:
                if node in graph[pred]:
                    earliest_slot = max(earliest_slot, slot[pred] + 1)
            
            # Place in the earliest available slot
            placed = False
            for s in range(earliest_slot, T + 1):
                if slot_count[s] < M:
                    slot[node] = s
                    slot_count[s] += 1
                    placed = True
                    break
            
            if not placed:
                print("NO")
                return
        
        # Rebuild queue with nodes whose predecessors are all processed
        temp_queue = list(queue) if queue else list(next_queue)
        queue = deque()
        
        # We need to be more careful with topological sorting
        # Let's restart with a proper topological approach
        
    # Let's re-implement with a cleaner approach
    # Re-read and re-process
    
def solve_correct():
    import sys
    from collections import defaultdict, deque
    
    n, M, T, m = map(int, input().split())
    
    # Build graph
    graph = defaultdict(list)
    in_degree = [0] * (n + 1)
    
    for _ in range(m):
        a, b = map(int, input().split())
        graph[a].append(b)
        in_degree[b] += 1
    
    # Kahn's algorithm for topological sorting
    queue = deque()
    for i in range(1, n + 1):
        if in_degree[i] == 0:
            queue.append(i)
    
    top_order = []
    while queue:
        node = queue.popleft()
        top_order.append(node)
        for neighbor in graph[node]:
            in_degree[neighbor] -= 1
            if in_degree[neighbor] == 0:
                queue.append(neighbor)
    
    if len(top_order) != n:
        print("NO")
        return
    
    # Now assign slots greedily
    slot = [0] * (n + 1)
    slot_count = [0] * (T + 1)
    
    for node in top_order:
        # Earliest slot is max(1, max of predecessors + 1)
        earliest = 1
        for pred in range(1, n + 1):
            if node in graph[pred]:
                earliest = max(earliest, slot[pred] + 1)
        
        # Assign to first available slot
        assigned = False
        for s in range(earliest, T + 1):
            if slot_count[s] < M:
                slot[node] = s
                slot_count[s] += 1
                assigned = True
                break
        
        if not assigned:
            print("NO")
            return
    
    print("YES")
    print(*[slot[i] for i in range(1, n + 1)])

# There's still an issue with finding predecessors efficiently
def solve_final():
    from collections import defaultdict, deque
    
    n, M, T, m = map(int, input().split())
    
    # Build graph
    graph = defaultdict(list)
    in_degree = [0] * (n + 1)
    reverse_graph = defaultdict(list)
    
    for _ in range(m):
        a, b = map(int, input().split())
        graph[a].append(b)
        in_degree[b] += 1
        reverse_graph[b].append(a)
    
    # Kahn's algorithm for topological sorting
    queue = deque()
    for i in range(1, n + 1):
        if in_degree[i] == 0:
            queue.append(i)
    
    top_order = []
    while queue:
        node = queue.popleft()
        top_order.append(node)
        for neighbor in graph[node]:
            in_degree[neighbor] -= 1
            if in_degree[neighbor] == 0:
                queue.append(neighbor)
    
    if len(top_order) != n:
        print("NO")
        return
    
    # Now assign slots greedily
    slot = [0] * (n + 1)
    
    for node in top_order:
        # Earliest slot is max(1, max of predecessors + 1)
        earliest = 1
        for pred in reverse_graph[node]:
            earliest = max(earliest, slot[pred] + 1)
        
        # Count tasks in each slot to respect capacity
        slot_count = [0] * (T + 1)
        for i in range(1, n + 1):
            if slot[i] > 0:
                slot_count[slot[i]] += 1
        
        # Assign to first available slot
        assigned = False
        for s in range(earliest, T + 1):
            if slot_count[s] < M:
                slot[node] = s
                assigned = True
                break
        
        if not assigned:
            print("NO")
            return
    
    print("YES")
    print(*[slot[i] for i in range(1, n + 1)])

solve_final()