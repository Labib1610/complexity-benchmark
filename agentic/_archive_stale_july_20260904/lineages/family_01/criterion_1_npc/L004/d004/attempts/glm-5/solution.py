import sys

def solve():
    data = sys.stdin.read().split()
    if not data:
        return
    n = int(data[0]); m = int(data[1])
    adj = [set() for _ in range(n)]
    idx = 2
    for _ in range(m):
        u = int(data[idx]) - 1; v = int(data[idx+1]); idx += 2
        v -= 1
        if u != v:
            adj[u].add(v)
            adj[v].add(u)
    
    # For each vertex, forbidden modes = union of neighbors' assigned modes.
    # We want lexicographically smallest assignment.
    # Since modes are 1,2,3 and constraint is |f_u - f_v| >= 1, i.e., f_u != f_v.
    # This is exactly graph 3-coloring with colors 1,2,3, lexicographically smallest.
    
    # Use backtracking with pruning. n <= 40.
    # We can use a simple recursive backtracking with forward checking.
    
    color = [0] * n  # 0 means unassigned
    # forbidden[i] is a bitmask of colors (1..3) that are forbidden for vertex i
    forbidden = [0] * n
    
    # Order: we assign in order 0..n-1 to get lexicographically smallest.
    # But we can also use a heuristic. However for correctness of lexicographically smallest,
    # we must try colors in increasing order for vertex 0, then 1, etc.
    # So we assign in natural order.
    
    # Precompute neighbors
    neighbors = [list(adj[i]) for i in range(n)]
    
    def backtrack(pos):
        if pos == n:
            return True
        for c in (1, 2, 3):
            if forbidden[pos] & (1 << c):
                continue
            # assign
            color[pos] = c
            # update forbidden for neighbors
            added = []
            for nb in neighbors[pos]:
                if color[nb] == 0 and not (forbidden[nb] & (1 << c)):
                    forbidden[nb] |= (1 << c)
                    added.append(nb)
            # check if any unassigned neighbor has no available color
            ok = True
            for nb in added:
                # check if all colors forbidden
                if (forbidden[nb] & 0b1110) == 0b1110:
                    ok = False
                    break
            if ok:
                if backtrack(pos + 1):
                    return True
            # undo
            for nb in added:
                forbidden[nb] &= ~(1 << c)
            color[pos] = 0
        return False
    
    if backtrack(0):
        print("YES")
        print(" ".join(str(color[i]) for i in range(n)))
    else:
        print("NO")

solve()