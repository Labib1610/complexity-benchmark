from collections import defaultdict, deque

def solve():
    q, t = map(int, input().split())
    
    # Build graph for bipartite matching
    # Relics: 1 to q
    # Vitrines: q+1 to 2*q
    graph = defaultdict(list)
    for _ in range(t):
        a, b = map(int, input().split())
        graph[a].append(b)
    
    # Hungarian algorithm / Ford-Fulkerson for bipartite matching
    match_vitrine = {}  # vitrine -> relic
    match_relic = {}    # relic -> vitrine
    
    def bfs(start):
        visited = set()
        queue = deque([start])
        parent = {start: None}
        
        reachable_relics = {start}
        reachable_vitrines = set()
        
        while queue:
            relic = queue.popleft()
            for vitrine in graph[relic]:
                if vitrine in reachable_vitrines:
                    continue
                reachable_vitrines.add(vitrine)
                if vitrine in match_vitrine:  # matched vitrine
                    next_relic = match_vitrine[vitrine]
                    if next_relic not in reachable_relics:
                        reachable_relics.add(next_relic)
                        parent[next_relic] = relic
                        queue.append(next_relic)
                else:  # free vitrine - augmenting path found
                    # Reconstruct path
                    current_v = vitrine
                    current_r = relic
                    path = []
                    while current_r is not None:
                        path.append((current_r, current_v))
                        current_r, current_v = parent.get(current_r, (None, None)), current_r
                    
                    # Augment along this path
                    for i in range(len(path)-1, -1, -1):
                        r, v = path[i]
                        match_relic[r] = v
                        match_vitrine[v] = r
                    return True
        return False
    
    # Try to match each relic
    for relic in range(1, q+1):
        if relic not in match_relic:
            # Run BFS to find augmenting path
            visited_relics = set()
            visited_vitrines = set()
            
            queue = deque([relic])
            parent = {relic: None}
            visited_relics.add(relic)
            
            found = False
            while queue and not found:
                r = queue.popleft()
                for v in graph[r]:
                    if v in visited_vitrines:
                        continue
                    visited_vitrines.add(v)
                    if v not in match_vitrine:  # Free vitrine
                        # Found augmenting path
                        path_vit = [v]
                        path_rel = [r]
                        cur_r = r
                        while parent[cur_r] is not None:
                            cur_v = match_relic.get(cur_r)
                            path_vit.append(cur_v)
                            cur_r = parent[cur_r]
                            path_rel.append(cur_r)
                        
                        # Update matches along path
                        for i in range(len(path_rel)):
                            rr = path_rel[-1-i]
                            vv = path_vit[-1-i]
                            match_relic[rr] = vv
                            match_vitrine[vv] = rr
                        
                        found = True
                        break
                    else:
                        # Vitrine is matched to another relic
                        next_relic = match_vitrine[v]
                        if next_relic not in visited_relics:
                            visited_relics.add(next_relic)
                            parent[next_relic] = r
                            queue.append(next_relic)
            
            if not found:
                print("NO")
                return
    
    # Check if all relics are matched
    if len(match_relic) == q:
        print("YES")
        # Output matches in order of relics
        for relic in range(1, q+1):
            print(relic, match_relic[relic])
    else:
        print("NO")

solve()