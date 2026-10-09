from collections import defaultdict

def solve():
    import sys
    input = sys.stdin.read
    data = input().split()
    
    k = int(data[0])
    t = int(data[1])
    
    # Each specialist has exactly one machine
    # We can represent this as a bipartite matching problem:
    # Left side: specialists (1..k)
    # Right side: time slots (1..k)
    # Edges: feasible assignments (x, y, z) where x=spec, y=machine, z=time
    
    # Since each spec has exactly one machine, we can ignore machines
    # and just match specs to time slots
    
    # Build adjacency list: spec -> list of time slots
    adj = defaultdict(list)
    assignments = []
    
    idx = 2
    for _ in range(t):
        x = int(data[idx])
        y = int(data[idx+1])
        z = int(data[idx+2])
        idx += 3
        assignments.append((x, y, z))
        adj[x].append(z)
    
    # Try to find a perfect matching from specialists to time slots
    # This is equivalent to finding a system of distinct representatives
    # We can model this as a max flow problem or use Hall's theorem
    
    # But since we have exactly k specialists and k time slots,
    # and each assignment is (spec, its_machine, time),
    # we need to select exactly one assignment per specialist,
    # such that all time slots are used exactly once.
    
    # This is a maximum bipartite matching problem:
    # L = specialists, R = time slots, edges = feasible assignments
    
    # Let's build the graph properly
    # Nodes: specialists 1..k, time slots 1..k
    # Edges: an edge from spec x to time z if there exists a feasible assignment (x, *, z)
    
    from collections import deque
    
    # Build graph
    graph = [[] for _ in range(k+1)]  # 1-indexed
    edge_map = {}  # (x,z) -> (x,y,z)
    
    for x, y, z in assignments:
        graph[x].append(z)
        edge_map[(x, z)] = (x, y, z)
    
    # Maximum bipartite matching using Hungarian algorithm / Ford-Fulkerson
    def bpm(u, matchR, seen):
        for v in graph[u]:
            if not seen[v]:
                seen[v] = True
                if matchR[v] == -1 or bpm(matchR[v], matchR, seen):
                    matchR[v] = u
                    return True
        return False
    
    def max_bipartite_matching():
        matchR = [-1] * (k + 1)  # time slot j is matched to specialist matchR[j]
        result = 0
        for i in range(1, k + 1):
            seen = [False] * (k + 1)
            if bpm(i, matchR, seen):
                result += 1
        return result, matchR
    
    # Find maximum matching
    num_matched, matchR = max_bipartite_matching()
    
    if num_matched < k:
        print("NO")
        return
    
    print("YES")
    # Reconstruct solution
    for z in range(1, k + 1):
        x = matchR[z]
        if x != -1:
            # Find the machine for specialist x
            # Since each specialist has exactly one machine in all their assignments
            # We can pick any assignment with this spec and time
            x_y_z = edge_map[(x, z)]
            print(x_y_z[0], x_y_z[1], x_y_z[2])

solve()