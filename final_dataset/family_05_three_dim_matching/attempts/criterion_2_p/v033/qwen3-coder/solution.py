from collections import defaultdict

def solve():
    import sys
    input = sys.stdin.read
    data = input().split()
    
    k = int(data[0])
    t = int(data[1])
    
    index = 2
    combinations = []
    spec_to_mach = {}
    mach_to_spec = {}
    
    for _ in range(t):
        x = int(data[index])
        y = int(data[index+1])
        z = int(data[index+2])
        combinations.append((x, y, z))
        index += 3
        
        # Check consistency
        if x in spec_to_mach:
            if spec_to_mach[x] != y:
                print("NO")
                return
        else:
            spec_to_mach[x] = y
            
        if y in mach_to_spec:
            if mach_to_spec[y] != x:
                print("NO")
                return
        else:
            mach_to_spec[y] = x
    
    # Build bipartite graph between specialists/machines and time slots
    # Since specialists and machines are paired uniquely, we can treat them as one entity
    # For each specialist-machine pair, we have a set of allowed time slots
    
    spec_mach_pairs = {}
    for x, y, z in combinations:
        if (x, y) not in spec_mach_pairs:
            spec_mach_pairs[(x, y)] = []
        spec_mach_pairs[(x, y)].append(z)
    
    # Check if we have exactly k pairs
    if len(spec_mach_pairs) < k:
        print("NO")
        return
    
    # Create mapping for pairs to indices for Hungarian algorithm
    pairs = list(spec_mach_pairs.keys())
    time_slots = set()
    for times in spec_mach_pairs.values():
        time_slots.update(times)
    
    if len(time_slots) < k:
        print("NO")
        return
    
    time_list = sorted(time_slots)
    time_index = {time: i for i, time in enumerate(time_list)}
    
    # Build bipartite matching graph
    # Left side: pairs (specialist-machine), Right side: time slots
    graph = [[] for _ in range(len(pairs))]
    for i, pair in enumerate(pairs):
        for time in spec_mach_pairs[pair]:
            if time in time_index:
                graph[i].append(time_index[time])
    
    # Implement Hungarian algorithm for maximum matching
    def dfs(u, match_right, match_left, visited):
        for v in graph[u]:
            if visited[v]:
                continue
            visited[v] = True
            if match_right[v] == -1 or dfs(match_right[v], match_right, match_left, visited):
                match_right[v] = u
                match_left[u] = v
                return True
        return False
    
    match_left = [-1] * len(pairs)
    match_right = [-1] * len(time_list)
    
    matching = 0
    for u in range(len(pairs)):
        visited = [False] * len(time_list)
        if dfs(u, match_right, match_left, visited):
            matching += 1
    
    if matching < k:
        print("NO")
        return
    
    print("YES")
    # Output the matching
    for i in range(len(pairs)):
        if match_left[i] != -1:
            x, y = pairs[i]
            z = time_list[match_left[i]]
            print(x, y, z)

solve()