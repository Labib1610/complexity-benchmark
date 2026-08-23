import sys

# Increase recursion depth to be safe
sys.setrecursionlimit(5000)

def solve():
    # Read all input from stdin
    input_data = sys.stdin.read().split()
    if not input_data:
        return
    
    iterator = iter(input_data)
    try:
        n = int(next(iterator))
        m = int(next(iterator))
    except StopIteration:
        return

    # Adjacency masks and lists
    # Using 1-based indexing for nodes
    adj_mask = [0] * (n + 1)
    adj_list = [[] for _ in range(n + 1)]
    
    for _ in range(m):
        u = int(next(iterator))
        v = int(next(iterator))
        adj_list[u].append(v)
        adj_list[v].append(u)
        adj_mask[u] |= (1 << v)
        adj_mask[v] |= (1 << u)

    # Check for K4 subgraph (clique of size 4)
    # If a K4 exists, 3-coloring is impossible.
    # We iterate over each edge (u, v) and check if there are two common neighbors connected to each other.
    # This is an optimization to quickly reject impossible cases.
    for u in range(1, n + 1):
        for v in adj_list[u]:
            if v > u:
                # u and v are connected
                # Find common neighbors
                common = adj_mask[u] & adj_mask[v]
                # Remove u and v from common (though they shouldn't be there due to no self loops)
                common &= ~(1 << u)
                common &= ~(1 << v)
                
                if common != 0:
                    # Check if any pair in common is connected
                    # Pick the lowest bit set in common as w
                    # (common & -common) isolates the lowest set bit
                    lowest_bit = common & -common
                    w_idx = lowest_bit.bit_length() - 1
                    
                    # Check if there exists another node z in common such that z is connected to w
                    # We remove w from common before checking intersection with adj_mask[w]
                    if (common & ~ (1 << w_idx)) & adj_mask[w_idx]:
                        print("NO")
                        return

    # Backtracking to find lexicographically smallest 3-coloring
    assignment = [0] * (n + 1)
    # forbidden[v] is a bitmask where bit c is set if color (c+1) is forbidden for v
    # Colors are 1, 2, 3 corresponding to bits 0, 1, 2.
    # So forbidden mask 7 (111) means all colors forbidden.
    forbidden = [0] * (n + 1)
    
    # Global count of dead nodes (unassigned nodes with all 3 colors forbidden)
    dead_count = 0
    
    def backtrack(u):
        nonlocal dead_count
        
        # If we have assigned all nodes, we found a solution
        if u > n:
            return True
        
        # Pruning: if any unassigned node is dead, this branch is invalid
        if dead_count > 0:
            return False
        
        # Try colors 1, 2, 3 in order to ensure lexicographically smallest
        for color in [1, 2, 3]:
            # Check conflict with already assigned neighbors (neighbors v < u)
            conflict = False
            for v in adj_list[u]:
                if v < u:
                    if assignment[v] == color:
                        conflict = True
                        break
            
            if conflict:
                continue
            
            # If valid, assign color to u
            assignment[u] = color
            
            # Update forbidden for unassigned neighbors (neighbors v > u)
            # Keep track of changes to backtrack
            modified_nodes = []
            added_dead = 0
            
            for v in adj_list[u]:
                if v > u:
                    old_f = forbidden[v]
                    new_f = old_f | (1 << (color - 1))
                    forbidden[v] = new_f
                    # If v was not dead and becomes dead
                    if old_f != 7 and new_f == 7:
                        added_dead += 1
                        modified_nodes.append((v, old_f))
            
            dead_count += added_dead
            
            if dead_count == 0:
                if backtrack(u + 1):
                    return True
            
            # Backtrack: restore state
            dead_count -= added_dead
            for v, old_f in modified_nodes:
                forbidden[v] = old_f
            assignment[u] = 0
            
        return False

    if backtrack(1):
        print("YES")
        print(*(assignment[1:]))
    else:
        print("NO")

if __name__ == '__main__':
    solve()