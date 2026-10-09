from collections import defaultdict
import sys

def find_maximum_matching(graph, left_set, right_set):
    # Hopcroft-Karp implementation for maximum bipartite matching
    pair_left = {}
    pair_right = {}
    dist = {}
    
    def bfs():
        queue = []
        for u in left_set:
            if u not in pair_left:
                dist[u] = 0
                queue.append(u)
            else:
                dist[u] = float('inf')
        dist[None] = float('inf')
        
        while queue:
            u = queue.pop(0)
            if dist[u] < dist[None]:
                for v in graph[u]:
                    if v not in pair_right:
                        pair_right[v] = None
                    if pair_right[v] is None or pair_right[v] not in dist or dist[pair_right[v]] == float('inf'):
                        if pair_right[v] is None:
                            dist[None] = dist[u] + 1
                        elif pair_right[v] not in dist:
                            dist[pair_right[v]] = dist[u] + 1
                            queue.append(pair_right[v])
        return dist[None] != float('inf')
    
    def dfs(u):
        if u is not None:
            for v in graph[u]:
                if v not in pair_right:
                    pair_right[v] = None
                if pair_right[v] is None or (pair_right[v] in dist and dist[pair_right[v]] == dist[u] + 1):
                    if pair_right[v] is None or dfs(pair_right[v]):
                        pair_right[v] = u
                        if u not in pair_left:
                            pair_left[u] = None
                        pair_left[u] = v
                        return True
            dist[u] = float('inf')
            return False
        return True
    
    matching = 0
    while bfs():
        for u in left_set:
            if u not in pair_left:
                if dfs(u):
                    matching += 1
    return matching, pair_left

def solve():
    input = sys.stdin.read
    data = input().split()
    
    q = int(data[0])
    t = int(data[1])
    
    if t == 0:
        if q == 0:
            print("YES")
        else:
            print("NO")
        return
    
    blueprints = []
    idx = 2
    for i in range(t):
        a = int(data[idx])
        b = int(data[idx+1])
        c = int(data[idx+2])
        blueprints.append((a, b, c))
        idx += 3
    
    # For small q, we can try backtracking
    if q <= 20:
        # Use backtracking approach
        used_blueprints = [False] * t
        used_relics = [False] * (3*q + 1)
        result = []
        
        def backtrack(installation_idx):
            if installation_idx == q:
                return True
            
            for i in range(t):
                if used_blueprints[i]:
                    continue
                a, b, c = blueprints[i]
                if used_relics[a] or used_relics[b] or used_relics[c]:
                    continue
                
                used_blueprints[i] = True
                used_relics[a] = True
                used_relics[b] = True
                used_relics[c] = True
                result.append(blueprints[i])
                
                if backtrack(installation_idx + 1):
                    return True
                
                used_blueprints[i] = False
                used_relics[a] = False
                used_relics[b] = False
                used_relics[c] = False
                result.pop()
            
            return False
        
        if backtrack(0):
            print("YES")
            for blueprint in result:
                print(blueprint[0], blueprint[1], blueprint[2])
        else:
            print("NO")
        return
    
    # For larger q, use bipartite matching approach
    # Create a graph where left side is blueprints and right side is relic positions
    # This is more complex; let's use a simpler approach for larger inputs
    
    # Try greedy approach with backtracking optimization
    used_blueprints = [False] * t
    used_relics = [False] * (3*q + 1)
    result = []
    
    def count_available_relics():
        count = 0
        for i in range(1, 3*q + 1):
            if not used_relics[i]:
                count += 1
        return count
    
    def is_valid_choice(bp_idx):
        a, b, c = blueprints[bp_idx]
        return not used_relics[a] and not used_relics[b] and not used_relics[c]
    
    def backtrack_optimized(installation_idx):
        if installation_idx == q:
            return True
        
        # Pruning: if remaining relics don't fit evenly, prune
        remaining_relics = count_available_relics()
        if remaining_relics != 3 * (q - installation_idx):
            return False
            
        # Try all available blueprints
        for i in range(t):
            if used_blueprints[i]:
                continue
            if not is_valid_choice(i):
                continue
            
            a, b, c = blueprints[i]
            used_blueprints[i] = True
            used_relics[a] = True
            used_relics[b] = True
            used_relics[c] = True
            result.append(blueprints[i])
            
            if backtrack_optimized(installation_idx + 1):
                return True
            
            used_blueprints[i] = False
            used_relics[a] = False
            used_relics[b] = False
            used_relics[c] = False
            result.pop()
        
        return False
    
    if backtrack_optimized(0):
        print("YES")
        for blueprint in result:
            print(blueprint[0], blueprint[1], blueprint[2])
    else:
        print("NO")

solve()