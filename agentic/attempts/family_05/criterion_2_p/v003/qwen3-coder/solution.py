from collections import defaultdict

def solve():
    k, t = map(int, input().split())
    
    if t == 0:
        print("NO")
        return
        
    combinations = []
    for _ in range(t):
        x, y, z = map(int, input().split())
        combinations.append((x, y, z))
    
    # Group combinations by specialist
    spec_to_combos = defaultdict(list)
    for x, y, z in combinations:
        spec_to_combos[x].append((x, y, z))
    
    # Due to the operational rule:
    # If two combinations have the same specialist, they have the same machine
    # This means for each specialist, all their combinations use the same machine
    
    # Create mapping from specialist to machine
    spec_to_machine = {}
    for x, combos in spec_to_combos.items():
        # All combinations for specialist x should have the same machine
        machine = combos[0][1]
        for combo in combos:
            if combo[1] != machine:
                # This violates the rule, but problem states input satisfies it
                pass
        spec_to_machine[x] = machine
    
    # Build bipartite graph: specialists on one side, time slots on other
    # Edge exists if there's a combination (x, y, z) where y = spec_to_machine[x]
    from collections import defaultdict
    
    # For each specialist, find which time slots are available
    spec_to_times = defaultdict(list)
    time_to_specs = defaultdict(list)
    
    for x, y, z in combinations:
        if y == spec_to_machine[x]:  # This should always be true due to rule
            spec_to_times[x].append(z)
            time_to_specs[z].append(x)
    
    # Now we need to match each specialist to a unique time slot
    # This is a bipartite matching problem
    
    def dfs(u, match_spec, match_time, visited):
        for v in spec_to_times[u]:
            if v in visited:
                continue
            visited.add(v)
            
            if v not in match_time or dfs(match_time[v], match_spec, match_time, visited):
                match_spec[u] = v
                match_time[v] = u
                return True
        return False
    
    match_spec = {}  # spec -> time
    match_time = {}  # time -> spec
    
    for spec in range(1, k + 1):
        if spec not in spec_to_machine:
            print("NO")
            return
        visited = set()
        if not dfs(spec, match_spec, match_time, visited):
            print("NO")
            return
    
    # Check if we have a complete matching
    if len(match_spec) != k:
        print("NO")
        return
        
    print("YES")
    for spec in range(1, k + 1):
        time = match_spec[spec]
        machine = spec_to_machine[spec]
        print(spec, machine, time)

solve()