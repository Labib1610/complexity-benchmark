from collections import defaultdict, deque

def solve():
    import sys
    input = sys.stdin.read
    data = input().split()
    
    k = int(data[0])
    t = int(data[1])
    
    index = 2
    triples = []
    control_to_sensor = {}
    sensor_to_control = {}
    power_modules = set()
    
    # To store which triples are available for each control board
    control_triples = defaultdict(list)
    # To store which triples use each power module
    power_triples = defaultdict(list)
    
    for _ in range(t):
        x = int(data[index])
        y = int(data[index+1])
        z = int(data[index+2])
        index += 3
        triples.append((x, y, z))
        control_triples[x].append((x, y, z))
        power_triples[z].append((x, y, z))
        power_modules.add(z)
        # Since firmware lock guarantees unique mapping
        if x not in control_to_sensor:
            control_to_sensor[x] = y
        if y not in sensor_to_control:
            sensor_to_control[y] = x
            
    # Check if we have exactly k control boards and k sensor arrays
    if len(control_to_sensor) != k or len(sensor_to_control) != k:
        print("NO")
        return
        
    # Build bipartite graph: left side is control boards (1..k), right side is power modules (1..k)
    # Edge exists if there's a certified triple with that control board and power module
    # Since each control board is tied to exactly one sensor array, we just need to match 
    # control boards to power modules
    
    # For each control board x, find all possible power modules z it can use
    control_power_options = defaultdict(set)
    triple_list = []
    
    for i in range(t):
        x, y, z = triples[i]
        control_power_options[x].add(z)
        triple_list.append((x, y, z))
        
    # Now we model this as a maximum matching problem:
    # We want to assign each control board (1..k) to a unique power module (1..k) 
    # such that the assignment is allowed by the certified triples
    
    # Build adjacency list for control boards to allowable power modules
    adj = defaultdict(list)
    for x in range(1, k+1):
        if x in control_power_options:
            for z in control_power_options[x]:
                adj[x].append(z)
                
    # Maximum bipartite matching using BFS (Hopcroft-Karp like approach)
    def bfs():
        queue = deque()
        for u in range(1, k+1):
            if pair_u[u] == 0:
                dist[u] = 0
                queue.append(u)
            else:
                dist[u] = float('inf')
        dist[0] = float('inf')
        
        while queue:
            u = queue.popleft()
            if dist[u] < dist[0]:
                for v in adj[u]:
                    if dist[pair_v[v]] == float('inf'):
                        dist[pair_v[v]] = dist[u] + 1
                        queue.append(pair_v[v])
        return dist[0] != float('inf')
    
    def dfs(u):
        if u != 0:
            for v in adj[u]:
                if dist[pair_v[v]] == dist[u] + 1:
                    if dfs(pair_v[v]):
                        pair_v[v] = u
                        pair_u[u] = v
                        return True
            dist[u] = float('inf')
            return False
        return True
    
    # Initialize
    pair_u = [0] * (k+1)  # pair_u[control] = power
    pair_v = [0] * (k+1)  # pair_v[power] = control
    dist = [float('inf')] * (k+1)
    
    # Find maximum matching
    matching = 0
    while bfs():
        for u in range(1, k+1):
            if pair_u[u] == 0:
                if dfs(u):
                    matching += 1
                    
    if matching != k:
        print("NO")
        return
        
    # Reconstruct the solution
    # For each matched control -> power, find the corresponding triple
    result = []
    used_powers = set()
    
    # Create reverse mapping from (x,z) to triple
    triple_map = {}
    for x, y, z in triples:
        triple_map[(x,z)] = (x,y,z)
        
    for x in range(1, k+1):
        z = pair_u[x]
        if z == 0:
            print("NO")
            return
        if (x,z) not in triple_map:
            print("NO")
            return
        result.append(triple_map[(x,z)])
        
    print("YES")
    for triple in result:
        print(triple[0], triple[1], triple[2])

solve()