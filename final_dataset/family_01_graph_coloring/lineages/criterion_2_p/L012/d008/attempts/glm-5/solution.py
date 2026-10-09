import sys
from collections import deque

def solve():
    input = sys.stdin.read().split()
    ptr = 0
    n = int(input[ptr]); ptr += 1
    m = int(input[ptr]); ptr += 1
    
    adj = [[] for _ in range(n + 1)]
    for _ in range(m):
        u = int(input[ptr]); ptr += 1
        v = int(input[ptr]); ptr += 1
        adj[u].append(v)
        adj[v].append(u)
    
    # Precompute valid pairs (h_u, h_v) such that checksum is 9
    # valid_pairs[h_u] = list of h_v that work
    valid_pairs = {1: [], 2: []}
    for hu in [1, 2]:
        for hv in [1, 2]:
            C = hu + 4
            if hv == 1:
                C = C * 2 - 1
            else:
                C = C + 3
            final = C ^ hu
            if final == 9:
                valid_pairs[hu].append(hv)
    
    # For each node, we need to find a valid assignment
    # This is a 2-SAT like problem but simpler: each edge forces a constraint
    # We use BFS/DFS to propagate constraints
    
    height = [0] * (n + 1)
    possible = True
    
    for start in range(1, n + 1):
        if height[start] != 0:
            continue
        
        # Try to assign height 1 to start, then propagate
        # If fails, try height 2
        # We need to find the lexicographically smallest valid assignment
        
        # BFS approach: try both possibilities for start node
        # and pick the one that gives smaller lexicographic result
        
        # First attempt: assign 1 to start
        height_attempt = [0] * (n + 1)
        queue = deque()
        height_attempt[start] = 1
        queue.append(start)
        valid = True
        component = [start]
        
        while queue and valid:
            u = queue.popleft()
            hu = height_attempt[u]
            for v in adj[u]:
                if height_attempt[v] == 0:
                    # v is unassigned, find valid hv
                    valid_hv = valid_pairs[hu]
                    if len(valid_hv) == 0:
                        valid = False
                        break
                    elif len(valid_hv) == 1:
                        height_attempt[v] = valid_hv[0]
                        queue.append(v)
                        component.append(v)
                    else:
                        # Both values are valid, we can choose freely
                        # Choose 1 for lexicographically smallest
                        height_attempt[v] = 1
                        queue.append(v)
                        component.append(v)
                else:
                    # v is already assigned, check if current hu is compatible
                    hv = height_attempt[v]
                    if hv not in valid_pairs[hu]:
                        valid = False
                        break
        
        if valid:
            for node in component:
                height[node] = height_attempt[node]
        else:
            # Try assigning 2 to start
            height_attempt = [0] * (n + 1)
            queue = deque()
            height_attempt[start] = 2
            queue.append(start)
            valid = True
            component = [start]
            
            while queue and valid:
                u = queue.popleft()
                hu = height_attempt[u]
                for v in adj[u]:
                    if height_attempt[v] == 0:
                        valid_hv = valid_pairs[hu]
                        if len(valid_hv) == 0:
                            valid = False
                            break
                        elif len(valid_hv) == 1:
                            height_attempt[v] = valid_hv[0]
                            queue.append(v)
                            component.append(v)
                        else:
                            height_attempt[v] = 1
                            queue.append(v)
                            component.append(v)
                    else:
                        hv = height_attempt[v]
                        if hv not in valid_pairs[hu]:
                            valid = False
                            break
            
            if valid:
                for node in component:
                    height[node] = height_attempt[node]
            else:
                possible = False
                break
    
    if not possible:
        print("NO")
    else:
        # Verify all edges
        for u in range(1, n + 1):
            for v in adj[u]:
                hu = height[u]
                hv = height[v]
                C = hu + 4
                if hv == 1:
                    C = C * 2 - 1
                else:
                    C = C + 3
                final = C ^ hu
                if final != 9:
                    possible = False
                    break
            if not possible:
                break
        
        if not possible:
            print("NO")
        else:
            print("YES")
            print(' '.join(map(str, height[1:])))

solve()