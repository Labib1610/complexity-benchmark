import sys

def solve():
    data = sys.stdin.read().strip().split()
    if not data:
        return
    it = iter(data)
    q = int(next(it))
    t = int(next(it))
    
    # adjacency structure: node -> list of (triplet_id, neighbors)
    adj = {}
    triplets = []
    for triplet_id in range(t):
        a = int(next(it))
        b = int(next(it))
        c = int(next(it))
        triplets.append((a, b, c))
        for node in (a, b, c):
            if node not in adj:
                adj[node] = []
            adj[node].append((triplet_id, (a, b, c)))
    
    if t == 0:
        print("NO")
        return

    selected_indices = set()
    used_nodes = set()
    
    # Greedy phase: pick triplets that don't conflict
    for i in range(t):
        if i in selected_indices:
            continue
        a, b, c = triplets[i]
        if a not in used_nodes and b not in used_nodes and c not in used_nodes:
            selected_indices.add(i)
            used_nodes.update((a, b, c))
    
    if len(used_nodes) == 3 * q:
        print("YES")
        for i in selected_indices:
            print(f"{triplets[i][0]} {triplets[i][1]} {triplets[i][2]}")
        return

    # Backtracking with conflict resolution
    # Find triplets that conflict with current selection
    conflicts = []
    for i in range(t):
        if i in selected_indices:
            continue
        a, b, c = triplets[i]
        conflict_with = []
        for node in (a, b, c):
            if node in used_nodes:
                # Find which selected triplet uses this node
                for si in selected_indices:
                    sa, sb, sc = triplets[si]
                    if node == sa or node == sb or node == sc:
                        conflict_with.append(si)
        if len(conflict_with) == 1:
            conflicts.append((i, conflict_with[0]))
    
    # Use DFS/heuristic to resolve conflicts
    best_sol = None
    
    def dfs(remaining_conflicts, current_selected, current_used, current_coverage):
        nonlocal best_sol
        if best_sol is not None:
            return
        if len(current_used) == 3 * q:
            best_sol = list(current_selected)
            return
        if not remaining_conflicts:
            return
        
        # Filter and prioritize conflicts
        valid_conflicts = []
        for new_idx, old_idx in remaining_conflicts:
            a, b, c = triplets[new_idx]
            old_t = triplets[old_idx]
            # Check if old_idx is still in current_selected
            if old_idx not in current_selected:
                continue
            # Check if we can swap
            can_swap = True
            for node in (a, b, c):
                if node in current_used and node not in old_t:
                    can_swap = False
                    break
            if can_swap:
                valid_conflicts.append((new_idx, old_idx))
        
        if not valid_conflicts:
            return
        
        # Try swaps in order
        for new_idx, old_idx in valid_conflicts:
            old_t = triplets[old_idx]
            new_t = triplets[new_idx]
            
            new_selected = set(current_selected)
            new_used = set(current_used)
            new_coverage = set(current_coverage)
            
            new_selected.remove(old_idx)
            new_used.difference_update(old_t)
            new_coverage.difference_update(old_t)
            
            new_selected.add(new_idx)
            new_used.update(new_t)
            new_coverage.update(new_t)
            
            # Recalculate remaining conflicts
            next_remaining = []
            for n, o in remaining_conflicts:
                if n == new_idx and o == old_idx:
                    continue
                if o == old_idx:
                    # Old triplet is removed, might be valid now
                    # Need to check new conflicts
                    continue
                next_remaining.append((n, o))
            
            # Add new conflicts from new_idx
            a, b, c = new_t
            for node in (a, b, c):
                for ti, t_triplet in adj.get(node, []):
                    if ti == new_idx or ti in new_selected:
                        continue
                    # Check if this triplet conflicts with new_selected
                    ta, tb, tc = t_triplet
                    conflict_with = None
                    can_add = True
                    for tn in (ta, tb, tc):
                        if tn in new_used:
                            for si in new_selected:
                                st = triplets[si]
                                if tn in st:
                                    if conflict_with is None:
                                        conflict_with = si
                                    elif conflict_with != si:
                                        can_add = False
                                        break
                    if can_add and conflict_with is not None and len(new_used) - 3 + 3 <= 3 * q:
                        next_remaining.append((ti, conflict_with))
            
            dfs(next_remaining, new_selected, new_used, new_coverage)
            if best_sol is not None:
                return
    
    dfs(conflicts, set(selected_indices), set(used_nodes), set(used_nodes))
    
    if best_sol is not None:
        print("YES")
        for i in best_sol:
            print(f"{triplets[i][0]} {triplets[i][1]} {triplets[i][2]}")
        return
    
    # Final fallback: exact 3D matching with recursion
    graph = {}
    for i in range(t):
        a, b, c = triplets[i]
        graph[i] = (a, b, c)
    
    used = [False] * (3 * q + 1)
    triplet_used = [False] * t
    solution = []
    
    def backtrack():
        if len(solution) == q:
            return True
        start_node = -1
        for node in range(1, 3 * q + 1):
            if not used[node]:
                start_node = node
                break
        if start_node == -1:
            return False
        
        for ti, (a, b, c) in graph.items():
            if triplet_used[ti]:
                continue
            if a != start_node:
                continue
            if used[b] or used[c]:
                continue
            
            used[a] = used[b] = used[c] = True
            triplet_used[ti] = True
            solution.append(ti)
            
            if backtrack():
                return True
            
            solution.pop()
            triplet_used[ti] = False
            used[a] = used[b] = used[c] = False
        
        return False
    
    if backtrack():
        print("YES")
        for ti in solution:
            a, b, c = triplets[ti]
            print(f"{a} {b} {c}")
    else:
        print("NO")

solve()