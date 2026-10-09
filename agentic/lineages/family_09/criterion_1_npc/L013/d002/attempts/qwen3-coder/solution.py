from itertools import combinations

def solve():
    n, m, k = map(int, input().split())
    
    # Read edges and build adjacency list
    edges = []
    adj = [set() for _ in range(n + 1)]
    for _ in range(m):
        u, v = map(int, input().split())
        edges.append((u, v))
        adj[u].add(v)
        adj[v].add(u)
    
    # If no edges, any combination works
    if m == 0:
        print("YES")
        print(' '.join(map(str, range(1, k + 1))))
        return
    
    # For small n, try all combinations
    if n <= 20:
        for combo in combinations(range(1, n + 1), k):
            valid = True
            selected = set(combo)
            for u, v in edges:
                if u in selected and v in selected:
                    valid = False
                    break
            if valid:
                print("YES")
                print(' '.join(map(str, combo)))
                return
        print("NO")
        return
    
    # For larger n, use a different approach - greedy + backtracking
    # But given constraints, we'll use meet-in-the-middle for n up to 46
    
    # Split vertices into two halves
    mid = n // 2
    left_vertices = list(range(1, mid + 1))
    right_vertices = list(range(mid + 1, n + 1))
    
    # Generate all valid subsets for left side
    left_valid = {}
    for i in range(min(len(left_vertices), k) + 1):
        for left_combo in combinations(left_vertices, i):
            # Check if this subset is valid internally
            valid = True
            for u, v in edges:
                if u in left_combo and v in left_combo:
                    valid = False
                    break
            if valid:
                # Get neighbors of this set in right side
                nbrs = set()
                for u in left_combo:
                    nbrs.update(adj[u])
                key = frozenset(nbrs.intersection(right_vertices))
                if key not in left_valid:
                    left_valid[key] = []
                left_valid[key].append(set(left_combo))
    
    # Now check all valid subsets of right side
    for j in range(min(len(right_vertices), k) + 1):
        for right_combo in combinations(right_vertices, j):
            # Check if this subset is valid internally
            valid = True
            for u, v in edges:
                if u in right_combo and v in right_combo:
                    valid = False
                    break
            if not valid:
                continue
                
            # Get neighbors of this set in left side
            nbrs = set()
            for u in right_combo:
                nbrs.update(adj[u])
            forbidden = frozenset(nbrs.intersection(left_vertices))
            
            # Look for compatible left sets
            for forbidden_left, left_sets in left_valid.items():
                # They conflict if they share an edge
                # This is complex; let's simplify
                
                # Actually, let's just check if forbidden and forbidden_left intersect
                if forbidden.isdisjoint(forbidden_left):
                    needed = k - len(right_combo)
                    if needed < 0:
                        continue
                    for left_set in left_sets:
                        if len(left_set) == needed:
                            # Final validation
                            total = list(left_set) + list(right_combo)
                            final_valid = True
                            total_set = set(total)
                            for u, v in edges:
                                if u in total_set and v in total_set:
                                    final_valid = False
                                    break
                            if final_valid:
                                print("YES")
                                print(' '.join(map(str, sorted(total))))
                                return
    
    # Fallback brute force for remaining cases
    for combo in combinations(range(1, n + 1), k):
        valid = True
        selected = set(combo)
        for u, v in edges:
            if u in selected and v in selected:
                valid = False
                break
        if valid:
            print("YES")
            print(' '.join(map(str, combo)))
            return
            
    print("NO")

solve()