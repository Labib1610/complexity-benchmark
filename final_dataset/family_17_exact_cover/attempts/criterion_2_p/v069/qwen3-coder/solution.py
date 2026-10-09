from collections import defaultdict, deque

def find_matching(q, pairs):
    # Build adjacency list for artifacts to cabinets
    graph = defaultdict(list)
    for a, b in pairs:
        graph[a].append(b)
    
    # Try to find a maximum matching using BFS (Hopcroft-Karp like approach)
    # But we'll use a simpler approach: try to find augmenting paths
    
    match_artifact = {}  # artifact -> cabinet
    match_cabinet = {}   # cabinet -> artifact
    
    def bfs():
        # Find shortest augmenting paths
        queue = deque()
        dist = {}
        
        for artifact in range(1, q + 1):
            if artifact not in match_artifact:
                dist[artifact] = 0
                queue.append(artifact)
            else:
                dist[artifact] = float('inf')
        dist[None] = float('inf')
        
        while queue:
            artifact = queue.popleft()
            if dist[artifact] < dist[None]:
                for cabinet in graph[artifact]:
                    # If cabinet is matched to some artifact
                    if cabinet in match_cabinet:
                        next_artifact = match_cabinet[cabinet]
                        if dist[next_artifact] == float('inf'):
                            dist[next_artifact] = dist[artifact] + 1
                            queue.append(next_artifact)
                    else:
                        dist[None] = dist[artifact] + 1
                        return True
        return False
    
    def dfs(artifact):
        if artifact is not None:
            for cabinet in graph[artifact]:
                if cabinet in match_cabinet:
                    next_artifact = match_cabinet[cabinet]
                    if dist[next_artifact] == dist[artifact] + 1:
                        if dfs(next_artifact):
                            match_artifact[artifact] = cabinet
                            match_cabinet[cabinet] = artifact
                            return True
                else:
                    match_artifact[artifact] = cabinet
                    match_cabinet[cabinet] = artifact
                    return True
            dist[artifact] = float('inf')
            return False
        return True
    
    # Main matching algorithm
    while bfs():
        for artifact in range(1, q + 1):
            if artifact not in match_artifact:
                dfs(artifact)
    
    # Check if we have a perfect matching
    if len(match_artifact) == q:
        return [(a, match_artifact[a]) for a in range(1, q + 1)]
    else:
        return None

# Simpler implementation using a greedy approach with backtracking capability
def solve():
    q, t = map(int, input().split())
    pairs = []
    for _ in range(t):
        a, b = map(int, input().split())
        pairs.append((a, b))
    
    # Build graph
    graph = defaultdict(list)
    for a, b in pairs:
        graph[a].append(b)
    
    # Try to find a matching using a DFS approach
    match = [-1] * (2*q + 1)  # match[cabinet] = artifact
    matched_artifact = [-1] * (q + 1)  # matched_artifact[artifact] = cabinet
    
    def dfs(u, visited):
        for v in graph[u]:  # For each cabinet v that artifact u can go to
            if visited[v]:
                continue
            visited[v] = True
            
            # If cabinet v is unmatched or we can find an augmenting path
            if match[v] == -1 or dfs(match[v], visited):
                match[v] = u
                matched_artifact[u] = v
                return True
        return False
    
    # Try to match each artifact
    matching_count = 0
    for artifact in range(1, q + 1):
        visited = [False] * (2*q + 1)
        if dfs(artifact, visited):
            matching_count += 1
    
    if matching_count == q:
        print("YES")
        for artifact in range(1, q + 1):
            print(artifact, matched_artifact[artifact])
    else:
        print("NO")

solve()