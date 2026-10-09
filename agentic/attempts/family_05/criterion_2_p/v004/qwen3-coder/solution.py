from collections import defaultdict

def solve():
    import sys
    input = sys.stdin.read
    data = input().split()
    
    k = int(data[0])
    t = int(data[1])
    
    index = 2
    combinations = []
    spec_machine = {}  # specialist -> machine they are qualified for
    
    # Read combinations and build spec->machine mapping
    for _ in range(t):
        x = int(data[index])
        y = int(data[index+1])
        z = int(data[index+2])
        combinations.append((x, y, z))
        if x not in spec_machine:
            spec_machine[x] = y
        index += 3
    
    # Build bipartite graph: specialists <-> time slots
    # Edge exists if (spec, spec_machine[spec], time_slot) is allowed
    allowed_time_slots = defaultdict(list)  # spec -> list of allowed time slots
    time_to_combinations = {}  # (spec, time_slot) -> combination index
    
    for i, (x, y, z) in enumerate(combinations):
        if x in spec_machine and spec_machine[x] == y:
            allowed_time_slots[x].append(z)
            time_to_combinations[(x, z)] = (x, y, z)
    
    # Create adjacency list for matching: spec -> list of time slots
    adj = defaultdict(list)
    for spec in range(1, k+1):
        if spec in allowed_time_slots:
            adj[spec] = allowed_time_slots[spec]
        else:
            adj[spec] = []
    
    # Implement Hopcroft-Karp for maximum bipartite matching
    match_spec = {}  # spec -> matched time slot
    match_slot = {}  # time slot -> matched spec
    
    def dfs(spec, visited):
        for slot in adj[spec]:
            if slot in visited:
                continue
            visited.add(slot)
            if slot not in match_slot or dfs(match_slot[slot], visited):
                match_spec[spec] = slot
                match_slot[slot] = spec
                return True
        return False
    
    # Find maximum matching
    matching = 0
    for spec in range(1, k+1):
        if spec in adj:  # Specialist exists
            visited = set()
            if dfs(spec, visited):
                matching += 1
    
    if matching < k:
        print("NO")
        return
    
    print("YES")
    for spec in range(1, k+1):
        if spec in match_spec:
            slot = match_spec[spec]
            machine = spec_machine[spec]
            print(spec, machine, slot)

solve()