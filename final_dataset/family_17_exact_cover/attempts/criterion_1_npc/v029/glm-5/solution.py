import sys

def main():
    data = sys.stdin.buffer.read().split()
    if not data:
        return
    q = int(data[0])
    t = int(data[1])
    n = 3 * q
    groups = []
    idx = 2
    for _ in range(t):
        a = int(data[idx]); b = int(data[idx+1]); c = int(data[idx+2])
        idx += 3
        groups.append((a, b, c))
    
    # Build adjacency: for each pair, list of groups containing that pair
    pair_to_groups = {}
    for gi, (a, b, c) in enumerate(groups):
        for x, y in ((a, b), (a, c), (b, c)):
            key = (x, y) if x < y else (y, x)
            pair_to_groups.setdefault(key, []).append(gi)
    
    # For each group, find conflicting groups (share at least one pair)
    conflict = [set() for _ in range(t)]
    for glist in pair_to_groups.values():
        L = len(glist)
        for i in range(L):
            gi = glist[i]
            for j in range(i+1, L):
                gj = glist[j]
                conflict[gi].add(gj)
                conflict[gj].add(gi)
    
    # Build vertex cover: select groups so that every conflicting pair has at least one selected
    # Then the non-selected groups form an independent set (valid partition candidate)
    # We need exactly q non-selected groups covering all n elements
    
    # Greedy + backtracking for vertex cover
    # State: which groups are still "free" (not selected, not excluded)
    # We want to select a vertex cover; non-selected must be independent and cover all elements
    
    # Let's think differently: we want an independent set of size q that partitions [1..n]
    # Independent set = no two share a pair (but they can share single elements... wait no)
    # Actually if two groups share even one element, they can't both be in partition
    # But sharing a pair is a stronger condition. Two groups sharing one element but no pair:
    # e.g., (1,2,3) and (1,4,5) share element 1 but no pair. They can't both be in partition.
    # So conflict should be: share at least one element, not just a pair!
    
    # Rebuild conflicts based on shared elements
    elem_to_groups = {}
    for gi, (a, b, c) in enumerate(groups):
        for x in (a, b, c):
            elem_to_groups.setdefault(x, []).append(gi)
    
    conflict = [set() for _ in range(t)]
    for glist in elem_to_groups.values():
        L = len(glist)
        for i in range(L):
            gi = glist[i]
            for j in range(i+1, L):
                gj = glist[j]
                conflict[gi].add(gj)
                conflict[gj].add(gi)
    
    # Now find independent set of size q that covers all elements exactly once
    # This is exact cover by independent set
    
    # Use DLX-like approach or simple backtracking with element coverage
    # Since n <= 600 and t <= 20000, need efficient approach
    
    # Build for each element, list of groups containing it
    # Backtrack: pick uncovered element with fewest groups, try each group
    
    # First check: each element must appear in at least one group
    for x in range(1, n+1):
        if x not in elem_to_groups:
            print("NO")
            return
    
    # Check total elements: sum of group sizes = 3q = n, and we need q groups, each covers 3 -> exact
    # So if we find q non-conflicting groups, they automatically cover exactly n elements (if all distinct)
    # Non-conflicting = independent set, and if size q and all elements distinct, covers n elements
    
    # But independent set of size q might not cover all elements. Need exact cover.
    
    # Backtracking with MRV (minimum remaining values)
    chosen = []
    chosen_set = set()
    covered = [False] * (n + 1)
    covered_count = [0]
    available = [True] * t  # group can still be chosen
    elem_groups = [elem_to_groups[x] for x in range(n + 1)]  # 1-indexed, elem_groups[0] unused
    
    def backtrack():
        if len(chosen) == q:
            return covered_count[0] == n
        # Find uncovered element with fewest available groups
        best_elem = -1
        best_count = float('inf')
        best_groups = None
        for x in range(1, n + 1):
            if covered[x]:
                continue
            cnt = 0
            glist = []
            for gi in elem_groups[x]:
                if available[gi]:
                    cnt += 1
                    glist.append(gi)
            if cnt == 0:
                return False
            if cnt < best_count:
                best_count = cnt
                best_elem = x
                best_groups = glist
                if cnt == 1:
                    break
        
        for gi in best_groups:
            a, b, c = groups[gi]
            # Check no conflict with chosen
            ok = True
            for cj in chosen:
                if cj in conflict[gi]:
                    ok = False
                    break
            if not ok:
                continue
            # Check elements not already covered
            if covered[a] or covered[b] or covered[c]:
                continue
            
            # Choose gi
            chosen.append(gi)
            chosen_set.add(gi)
            covered[a] = covered[b] = covered[c] = True
            covered_count[0] += 3
            # Mark conflicting groups unavailable
            newly_unavail = []
            for gj in conflict[gi]:
                if available[gj]:
                    available[gj] = False
                    newly_unavail.append(gj)
            available[gi] = False
            
            if backtrack():
                return True
            
            # Undo
            chosen.pop()
            chosen_set.discard(gi)
            covered[a] = covered[b] = covered[c] = False
            covered_count[0] -= 3
            for gj in newly_unavail:
                available[gj] = True
            available[gi] = True
        
        return False
    
    if backtrack():
        print("YES")
        for gi in chosen:
            a, b, c = groups[gi]
            print(f"{a} {b} {c}")
    else:
        print("NO")

main()