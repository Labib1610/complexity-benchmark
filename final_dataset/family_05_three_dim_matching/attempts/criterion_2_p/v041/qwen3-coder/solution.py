from collections import defaultdict

def solve():
    k, t = map(int, input().split())
    
    if t < k:
        print("NO")
        return
    
    # Group triplets by captain
    captain_to_jet = {}
    captain_to_destinations = defaultdict(list)
    
    for _ in range(t):
        c, j, d = map(int, input().split())
        if c not in captain_to_jet:
            captain_to_jet[c] = j
        captain_to_destinations[c].append(d)
    
    # Check if we have exactly k captains
    if len(captain_to_jet) != k:
        print("NO")
        return
    
    # Create a bipartite graph: captains on one side, destinations on other
    # We need to find a perfect matching
    
    # Build adjacency list for captains -> their available destinations
    adj = defaultdict(list)
    for c in captain_to_jet:
        adj[c] = captain_to_destinations[c]
    
    # Hungarian algorithm / DFS approach for maximum bipartite matching
    match_destination_to_captain = [-1] * (k + 1)  # 1-indexed
    match_captain_to_destination = [-1] * (k + 1)   # 1-indexed
    
    def dfs(captain, visited):
        for destination in adj[captain]:
            if visited[destination]:
                continue
            visited[destination] = True
            
            # If destination is unmatched or we can find augmenting path
            if match_destination_to_captain[destination] == -1 or dfs(match_destination_to_captain[destination], visited):
                match_destination_to_captain[destination] = captain
                match_captain_to_destination[captain] = destination
                return True
        return False
    
    # Try to find maximum matching
    matching = 0
    for captain in range(1, k + 1):
        if captain not in captain_to_jet:
            continue
        visited = [False] * (k + 1)
        if dfs(captain, visited):
            matching += 1
    
    if matching != k:
        print("NO")
        return
    
    print("YES")
    for captain in range(1, k + 1):
        if captain not in captain_to_jet:
            continue
        jet = captain_to_jet[captain]
        destination = match_captain_to_destination[captain]
        print(captain, jet, destination)

solve()