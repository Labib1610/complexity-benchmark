from collections import defaultdict, deque

def solve():
    import sys
    input = sys.stdin.read
    data = input().split()
    
    k = int(data[0])
    t = int(data[1])
    
    index = 2
    allowed = []
    spec_machine = {}
    
    for _ in range(t):
        x = int(data[index])
        y = int(data[index+1])
        z = int(data[index+2])
        allowed.append((x, y, z))
        if x not in spec_machine:
            spec_machine[x] = y
        index += 3
    
    # Build a graph for matching: specialists <-> time slots
    # Each specialist is associated with exactly one machine
    # So we can represent each allowed combo as (spec, time)
    
    # Map each specialist to its machine
    # We'll build a bipartite graph: specialists on one side, time slots on the other
    # Edge exists if (spec, machine, time) is allowed
    
    # But since each spec has exactly one machine, we just need to track which (spec,time) pairs are allowed
    adj = defaultdict(list)
    time_to_specs = defaultdict(list)
    
    for x, y, z in allowed:
        adj[x].append(z)
        time_to_specs[z].append(x)
    
    # Now we want a perfect matching in this bipartite graph (spec <--> time)
    # Number of nodes on spec side = number of unique specs
    # Number of nodes on time side = number of unique times
    # We want a matching of size k
    
    # Since each spec appears in at most k combos, and there are k specs,
    # and k time slots, we look for a maximum matching of size k
    
    # Use Hopcroft-Karp or similar. But since k <= 1200, we can use a simpler augmenting path method
    
    # Let's implement a simple version of Hungarian / augmenting paths
    
    def find_matching():
        # Try to match each spec to some time
        match_spec = {}      # spec -> time
        match_time = {}      # time -> spec
        
        def dfs(u, visited):
            for v in adj[u]:
                if v in visited:
                    continue
                visited.add(v)
                if v not in match_time or dfs(match_time[v], visited):
                    match_spec[u] = v
                    match_time[v] = u
                    return True
            return False
        
        matched = 0
        for spec in spec_machine:
            visited = set()
            if dfs(spec, visited):
                matched += 1
                
        return matched, match_spec
    
    matched_count, matching = find_matching()
    
    if matched_count != k:
        print("NO")
        return
    
    print("YES")
    # Reconstruct the solution
    # For each spec, we have a matched time
    for spec, time in matching.items():
        machine = spec_machine[spec]
        print(spec, machine, time)

solve()