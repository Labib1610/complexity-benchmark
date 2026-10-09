from collections import defaultdict, deque

def solve():
    import sys
    input = sys.stdin.read
    data = input().split()
    
    k = int(data[0])
    t = int(data[1])
    
    index = 2
    # Build a graph where each specialist is connected to available time slots
    # Since each specialist is qualified on exactly one machine, and no two specialists 
    # share the same machine, we can represent the problem as a bipartite matching
    # between specialists and time slots.
    
    # For each specialist, store the machine they're qualified on and the time slots available
    spec_machine = {}  # spec -> machine
    spec_times = defaultdict(list)  # spec -> [times]
    combinations = []  # store all combinations for output
    
    for _ in range(t):
        x = int(data[index])
        y = int(data[index+1])
        z = int(data[index+2])
        index += 3
        combinations.append((x, y, z))
        if x not in spec_machine:
            spec_machine[x] = y
        spec_times[x].append(z)
    
    # Check if we have k specialists
    if len(spec_machine) != k:
        print("NO")
        return
    
    # Now build a bipartite graph for matching specialists to time slots
    # Left side: specialists (1 to k)
    # Right side: time slots (1 to k)
    # Edges exist if there's a combination with that specialist and time slot
    
    # Build adjacency list for graph: spec -> [time slots]
    graph = defaultdict(list)
    for spec in range(1, k+1):
        if spec in spec_times:
            graph[spec] = spec_times[spec]
        else:
            # Specialist has no available time slot
            print("NO")
            return
    
    # Use Hopcroft-Karp or simpler Ford-Fulkerson for maximum bipartite matching
    # Implementing a simple DFS-based augmenting path algorithm
    
    match_time_to_spec = {}  # time_slot -> specialist
    match_spec_to_time = {}  # specialist -> time_slot
    
    def dfs(spec, visited):
        for time in graph[spec]:
            if time in visited:
                continue
            visited.add(time)
            
            # If time slot is free or we can find augmenting path
            if time not in match_time_to_spec:
                match_time_to_spec[time] = spec
                match_spec_to_time[spec] = time
                return True
            else:
                # Try to rematch the current occupant of 'time'
                spec_prev = match_time_to_spec[time]
                if dfs(spec_prev, visited):
                    match_time_to_spec[time] = spec
                    match_spec_to_time[spec] = time
                    return True
        return False
    
    # Try to match each specialist
    matched = 0
    for spec in range(1, k+1):
        visited = set()
        if dfs(spec, visited):
            matched += 1
    
    if matched != k:
        print("NO")
        return
    
    # Reconstruct the solution
    print("YES")
    result = []
    # Create mapping from (spec, machine, time) to check existence
    combo_set = set((x, y, z) for x, y, z in combinations)
    
    for spec in range(1, k+1):
        time = match_spec_to_time[spec]
        machine = spec_machine[spec]
        result.append(f"{spec} {machine} {time}")
    
    print("\n".join(result))

solve()