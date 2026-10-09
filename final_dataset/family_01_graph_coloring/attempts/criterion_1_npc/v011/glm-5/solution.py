import sys

def solve():
    data = sys.stdin.read().split()
    if not data:
        return
    it = iter(data)
    n = int(next(it))
    m = int(next(it))
    
    adj = [0] * n
    for _ in range(m):
        u = int(next(it)) - 1
        v = int(next(it)) - 1
        adj[u] |= 1 << v
        adj[v] |= 1 << u
    
    # Constraint Earliest Failure: if any vertex has degree >= 3, impossible
    for i in range(n):
        if bin(adj[i]).count('1') >= 3:
            print("NO")
            return
    
    # Create list of unique independent sets
    unique_sets = set()
    unique_sets.add(0) # Empty set
    masks = []
    for u in range(n):
        # neighbors of u within 0..u-1
        neighbors_low = adj[u] & ((1 << u) - 1)
        # non-neighbors of u within 0..u-1
        non_neighbors_low = ((1 << u) - 1) ^ neighbors_low
        
        new_masks = []
        # All current masks in `masks` are independent sets in 0..u-1
        for mask in masks:
            # If mask is subset of neighbors, we can add u
            if (mask & neighbors_low) == mask:
                new_masks.append(mask | (1 << u))
        masks.extend(new_masks)
        
        # Filter masks to keep only maximal sets
        removed = set()
        dominated_by = set()
        for k in range(len(masks)):
            mk = masks[k]
            if mk in dominated_by:
                continue
            for l in range(len(masks)):
                if k == l: continue
                ml = masks[l]
                if (mk | ml) == ml: # mk subset of ml
                    dominated_by.add(mk)
                    break
        
        new_list = []
        for mk in masks:
            if mk not in dominated_by:
                if mk not in unique_sets:
                    unique_sets.add(mk)
                    new_list.append(mk)
                elif mk == 0: # Keep 0 if not dominated
                    new_list.append(mk)
                    unique_sets.remove(0) # Prevent duplicates from re-adding
        # Ensure 0 is preserved if it survived (possible if n=0, but n>=1)
        if 0 not in dominated_by and 0 not in unique_sets:
            unique_sets.add(0)
            new_list.append(0)
            
        masks = new_list

    # Convert sets to list
    sets = list(unique_sets)
    
    # Interference Graph Coloring Check
    # Color 0 = mask for set 1, Color 1 = mask for set 2, Color 3 = mask for set 3
    # We iterate all pairs for colors 0 and 1.
    
    n_sets = len(sets)
    found = False
    ans0, ans1, ans3 = -1, -1, -1
    
    for i in range(n_sets):
        s0 = sets[i]
        # s1 must be independent of s0
        allowed_for_s1 = []
        for k in range(n_sets):
            if s0 & sets[k] == 0:
                allowed_for_s1.append(k)
        
        for j in allowed_for_s1:
            s1 = sets[j]
            
            # Check if s0 U s1 is a valid assignment to colors 0 and 1
            # This requires that every vertex in s0 U s1 has edges to the other set.
            # Vertices in color 0 (s0):
            ok = True
            for u in range(n):
                if (s0 >> u) & 1:
                    # u must have all its neighbors in s1 (minus neighbors in full graph)
                    # Neighbors in graph
                    deg_u = bin(adj[u]).count('1')
                    # Neighbors in s1
                    neigh_in_s1 = adj[u] & s1
                    cnt = bin(neigh_in_s1).count('1')
                    if cnt < deg_u:
                        ok = False
                        break
            if not ok:
                continue
            
            for u in range(n):
                if (s1 >> u) & 1:
                    deg_u = bin(adj[u]).count('1')
                    neigh_in_s0 = adj[u] & s0
                    cnt = bin(neigh_in_s0).count('1')
                    if cnt < deg_u:
                        ok = False
                        break
            if not ok:
                continue
            
            # If we are here, s0 and s1 are valid.
            found = True
            ans0 = s0
            ans1 = s1
            break
        if found:
            break
            
    if not found:
        print("NO")
        return
    
    print("YES")
    ans = [0] * n
    for u in range(n):
        if (ans0 >> u) & 1:
            ans[u] = 1
        elif (ans1 >> u) & 1:
            ans[u] = 2
        else:
            ans[u] = 3
            
    print(*(ans[i] for i in range(n)))

if __name__ == '__main__':
    solve()