import sys

def solve():
    data = sys.stdin.read().split()
    if not data:
        return
    it = iter(data)
    n = int(next(it))
    m = int(next(it))
    
    adj = [[] for _ in range(n)]
    for _ in range(m):
        u = int(next(it)) - 1
        v = int(next(it)) - 1
        adj[u].append(v)
        adj[v].append(u)
    
    # We want lexicographically smallest valid assignment.
    # Greedy approach: assign players 0 to n-1 sequentially.
    # For each player i, try team 1, then 2, then 3.
    # Pick the first valid team that allows completion for remaining players.
    # To check if remaining players can be assigned, we use 2-coloring on the
    # subgraph of unassigned players (since they have 2 teams available).
    
    teams = [0] * n
    # available[i] will be bitmask of available teams for player i
    # Initially all teams {1, 2, 3} available, represented as 0b111 (7)
    available = [7] * n
    
    def can_complete(start_idx):
        # Check if players from start_idx to n-1 can be validly assigned
        # using their currently available teams.
        # For unassigned players, we need to check if the subgraph is 2-colorable
        # with the available colors (which should be exactly 2 for unassigned).
        
        # Build subgraph of unassigned players
        unassigned = [i for i in range(start_idx, n) if teams[i] == 0]
        if not unassigned:
            return True
        
        # Map from original index to local index
        idx_map = {i: j for j, i in enumerate(unassigned)}
        k = len(unassigned)
        
        # For each unassigned player, check available teams
        local_avail = [available[i] for i in unassigned]
        
        # Check if any player has no available teams
        for av in local_avail:
            if av == 0:
                return False
        
        # For 2-coloring, we need to assign each player one of their available colors
        # This is a constraint satisfaction problem
        # Since each player has at most 2 colors, we can use bipartite matching
        # or simple DFS
        
        # Build adjacency for unassigned players
        local_adj = [[] for _ in range(k)]
        for i in range(k):
            orig_i = unassigned[i]
            for orig_j in adj[orig_i]:
                if orig_j in idx_map:
                    local_adj[i].append(idx_map[orig_j])
        
        # Try to 2-color the subgraph
        # We use DFS with backtracking
        color = [-1] * k  # -1: uncolored, 0 or 1: color
        
        def dfs(u):
            for v in local_adj[u]:
                if color[v] == -1:
                    # v must have different color from u
                    # Check if v can take the opposite color
                    color[v] = 1 - color[u]
                    if not dfs(v):
                        return False
                elif color[v] == color[u]:
                    return False
            return True
        
        for i in range(k):
            if color[i] == -1:
                # Try both colors if available
                # Determine which colors are available for this component
                # We need to check if the component can be colored
                
                # First, let's see what colors are available for player i
                av = local_avail[i]
                colors = []
                if av & 1: colors.append(0)  # team 1
                if av & 2: colors.append(1)  # team 2
                if av & 4: colors.append(2)  # team 3
                
                if len(colors) == 0:
                    return False
                elif len(colors) == 1:
                    color[i] = colors[0]
                    if not dfs(i):
                        return False
                else:
                    # Try first available color
                    # For lexicographically smallest, we want smaller team numbers
                    # But here we just need to check if ANY valid coloring exists
                    # So we try both
                    found = False
                    for c in colors:
                        # Reset colors for this component
                        # Actually, we need to be more careful
                        # Let's do a fresh DFS for each attempt
                        temp_color = color[:]
                        color[i] = c
                        # Reset colors for unvisited nodes in this component
                        # Actually, let's just do DFS and see
                        # We need to track which nodes are in this component
                        stack = [i]
                        comp_nodes = set()
                        while stack:
                            u = stack.pop()
                            if u in comp_nodes:
                                continue
                            comp_nodes.add(u)
                            for v in local_adj[u]:
                                if v not in comp_nodes and color[v] == -1:
                                    stack.append(v)
                        
                        # Reset colors for comp_nodes except i
                        for node in comp_nodes:
                            color[node] = -1
                        color[i] = c
                        
                        if dfs(i):
                            found = True
                            break
                    
                    if not found:
                        return False
        
        return True
    
    for i in range(n):
        # Try teams 1, 2, 3 in order
        found_team = False
        for t in range(1, 4):
            # Check if team t is available for player i
            if not (available[i] & (1 << (t - 1))):
                continue
            
            # Assign team t to player i
            teams[i] = t
            
            # Update available teams for neighbors
            old_available = []
            for j in adj[i]:
                if teams[j] == 0:  # unassigned neighbor
                    old_available.append((j, available[j]))
                    available[j] &= ~(1 << (t - 1))
            
            # Check if remaining players can be assigned
            if can_complete(i + 1):
                found_team = True
                break
            else:
                # Revert
                teams[i] = 0
                for j, old_av in old_available:
                    available[j] = old_av
        
        if not found_team:
            print("NO")
            return
    
    print("YES")
    print(" ".join(map(str, teams)))

solve()