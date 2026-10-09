from collections import defaultdict, deque

def solve():
    k, t = map(int, input().split())
    
    if t < k:
        print("NO")
        return
        
    proposals = []
    crew_to_proposals = defaultdict(list)
    airframe_to_proposals = defaultdict(list)
    route_to_proposals = defaultdict(list)
    
    for i in range(t):
        x, y, z = map(int, input().split())
        proposals.append((x, y, z))
        crew_to_proposals[x].append(i)
        airframe_to_proposals[y].append(i)
        route_to_proposals[z].append(i)
    
    # Build bipartite graph for matching
    # Left side: crews (1 to k), Right side: routes (1 to k)
    # Edge exists if there's a proposal connecting crew to route
    
    # Create adjacency list for graph where crew connects to routes
    graph = defaultdict(list)
    for i, (x, y, z) in enumerate(proposals):
        graph[x].append(z)  # crew x can do route z
    
    # Now we need to find a perfect matching in this bipartite graph
    # Using Hungarian algorithm / Ford-Fulkerson style approach
    
    match_route_to_crew = {}  # route -> crew
    match_crew_to_route = {}  # crew -> route
    
    def dfs(crew, visited):
        for route in graph[crew]:
            if route in visited:
                continue
            visited.add(route)
            
            # If route is unmatched or we can find augmenting path
            if route not in match_route_to_crew or dfs(match_route_to_crew[route], visited):
                match_route_to_crew[route] = crew
                match_crew_to_route[crew] = route
                return True
        return False
    
    # Try to match each crew
    matched = 0
    for crew in range(1, k + 1):
        if dfs(crew, set()):
            matched += 1
    
    if matched != k:
        print("NO")
        return
    
    # Verify that the matching corresponds to actual proposals
    # For each crew-route pair in matching, check if there exists a proposal
    proposal_exists = {}
    for i, (x, y, z) in enumerate(proposals):
        proposal_exists[(x, z)] = i
    
    result = []
    for route in range(1, k + 1):
        crew = match_route_to_crew[route]
        if (crew, route) not in proposal_exists:
            print("NO")
            return
        idx = proposal_exists[(crew, route)]
        x, y, z = proposals[idx]
        result.append((x, y, z))
    
    print("YES")
    for x, y, z in result:
        print(x, y, z)

solve()