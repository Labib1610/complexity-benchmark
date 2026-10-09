from collections import defaultdict, deque

def solve():
    k, t = map(int, input().split())
    
    if t < k:
        print("NO")
        return
        
    # Since each specialist is paired with exactly one machine,
    # and no two specialists share the same machine,
    # we can think of this as a bipartite matching problem
    # between specialists (or machines) and time slots.
    
    # For each specialist x, we know their machine y_x
    # So each allowed combination (x, y, z) actually means
    # specialist x can work at time z (on their dedicated machine y)
    
    # Build a graph: specialist x can go to time slot z
    adj = defaultdict(list)  # adjacency list for the bipartite graph
    edges = []  # store all edges for reference
    
    for _ in range(t):
        x, y, z = map(int, input().split())
        adj[x].append(z)
        edges.append((x, y, z))
    
    # We need to match each specialist (1 to k) with a unique time slot (1 to k)
    # This is a maximum bipartite matching problem
    
    # Use Hungarian algorithm / Ford-Fulkerson style approach
    # match[time_slot] = specialist assigned to it (-1 if none)
    match = [-1] * (k + 1)  # index 0 unused
    result_pairs = []
    
    def bfs():
        # Try to find an augmenting path for each unmatched specialist
        parent = [-1] * (k + 1)  # parent[z] = x means time slot z was reached from specialist x
        visited = [False] * (k + 1)
        queue = deque()
        
        # Find all unmatched specialists and start BFS from them
        unmatched = []
        for x in range(1, k + 1):
            if x not in matched_specialist:
                unmatched.append(x)
                
        for x in unmatched:
            for z in adj[x]:
                if not visited[z]:
                    visited[z] = True
                    parent[z] = x
                    if match[z] == -1:
                        # Found an augmenting path
                        while z != -1:
                            prev_x = parent[z]
                            old_match = match[z]
                            match[z] = prev_x
                            matched_specialist.add(prev_x)
                            # Backtrack
                            if old_match == -1:
                                break
                            # Find which time slot the old match was using
                            found = False
                            for old_z in adj[old_match]:
                                if match[old_z] == old_match:
                                    z = old_z
                                    break
                            else:
                                z = -1
                        return True
                    queue.append(z)
                    
        while queue:
            z = queue.popleft()
            x = match[z]  # specialist currently matched to z
            for next_z in adj[x]:
                if not visited[next_z]:
                    visited[next_z] = True
                    parent[next_z] = x
                    if match[next_z] == -1:
                        # Augment along the path
                        current_z = next_z
                        while current_z != -1:
                            prev_x = parent[current_z]
                            old_match = match[current_z]
                            match[current_z] = prev_x
                            # Backtrack to find next edge in path
                            if old_match == -1:
                                break
                            # Find which time slot the old match was using
                            for old_z in adj[old_match]:
                                if match[old_z] == old_match:
                                    current_z = old_z
                                    break
                            else:
                                current_z = -1
                        return True
                    else:
                        queue.append(next_z)
        return False
    
    # Simpler implementation using DFS-based approach for bipartite matching
    def dfs(x, visited):
        for z in adj[x]:
            if visited[z]:
                continue
            visited[z] = True
            
            # If time slot z is free or we can find an alternative for its current user
            if match[z] == -1 or dfs(match[z], visited):
                match[z] = x
                return True
        return False
    
    matched_specialist = set()
    match_count = 0
    
    # Try to match each specialist
    for x in range(1, k + 1):
        visited = [False] * (k + 1)
        if dfs(x, visited):
            match_count += 1
    
    if match_count < k:
        print("NO")
        return
    
    print("YES")
    
    # Reconstruct the solution
    # match[z] = x means specialist x is assigned to time slot z
    # We also need to know the machine for each specialist
    specialist_machine = {}  # specialist -> machine
    for x, y, z in edges:
        specialist_machine[x] = y
    
    for z in range(1, k + 1):
        if match[z] != -1:
            x = match[z]
            y = specialist_machine[x]
            print(x, y, z)

solve()