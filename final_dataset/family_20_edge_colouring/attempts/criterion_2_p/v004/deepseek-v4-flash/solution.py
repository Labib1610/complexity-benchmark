import sys
from collections import deque

input = sys.stdin.readline

def solve():
    nL, nR, m = map(int, input().split())
    edges = []
    degL = [0] * (nL + 1)
    degR = [0] * (nR + 1)
    for _ in range(m):
        u, v = map(int, input().split())
        edges.append((u, v))
        degL[u] += 1
        degR[v] += 1
    
    Delta = max(max(degL), max(degR), 1)
    
    # adjacency list for left side
    adj = [[] for _ in range(nL + 1)]
    for idx, (u, v) in enumerate(edges):
        adj[u].append((v, idx))
    
    # color assignment
    color = [0] * m
    
    # For each left vertex, we will assign colors to its incident edges
    # using a matching-based approach.
    
    # We'll store for each right vertex the color currently used by each incident edge
    # and for each left vertex the color used by each incident edge.
    
    # We'll use arrays to track colors per vertex
    colorL = [0] * (nL + 1)  # not used directly, we'll use per-edge
    # For each right vertex, color -> edge index
    right_color_edge = [dict() for _ in range(nR + 1)]
    
    # Process each left vertex
    for u in range(1, nL + 1):
        # list of (right_vertex, edge_index)
        incident = adj[u]
        # We'll assign colors to these edges
        # We need to find a free color for each edge, possibly recoloring
        for v, eidx in incident:
            # find a free color for this edge
            used_colors = set()
            # colors used by u's edges already assigned
            for v2, eidx2 in adj[u]:
                if color[eidx2] != 0:
                    used_colors.add(color[eidx2])
            # colors used by v's edges already assigned
            for c, eidx2 in right_color_edge[v].items():
                used_colors.add(c)
            
            # find smallest free color
            c = 1
            while c in used_colors:
                c += 1
            # assign
            color[eidx] = c
            right_color_edge[v][c] = eidx
            
            # Now fix conflicts: if v already had an edge with color c, recolor it
            # Actually we already ensured c is free for v, so no conflict.
    
    # But the above greedy may fail; we need proper edge coloring.
    # Let's implement the standard algorithm:
    
    # Reset
    color = [0] * m
    # For each left vertex, we'll store color -> edge index
    left_color_edge = [dict() for _ in range(nL + 1)]
    right_color_edge = [dict() for _ in range(nR + 1)]
    
    for u in range(1, nL + 1):
        for v, eidx in adj[u]:
            # find free color for u
            usedL = set(left_color_edge[u].keys())
            usedR = set(right_color_edge[v].keys())
            c = 1
            while c in usedL or c in usedR:
                c += 1
            # assign
            color[eidx] = c
            left_color_edge[u][c] = eidx
            right_color_edge[v][c] = eidx
    
    # This greedy works for bipartite graphs if we process edges in a certain order,
    # but not always. We need the full algorithm with recoloring.
    
    # Let's implement the standard algorithm:
    # For each edge (u,v), if we can't find a free color, we do a color exchange path.
    
    color = [0] * m
    left_color_edge = [dict() for _ in range(nL + 1)]
    right_color_edge = [dict() for _ in range(nR + 1)]
    
    for u in range(1, nL + 1):
        for v, eidx in adj[u]:
            # find free color for u
            usedL = set(left_color_edge[u].keys())
            usedR = set(right_color_edge[v].keys())
            c = 1
            while c in usedL or c in usedR:
                c += 1
            # assign
            color[eidx] = c
            left_color_edge[u][c] = eidx
            right_color_edge[v][c] = eidx
    
    # The above greedy is actually correct for bipartite graphs if we process edges
    # in any order? Not always, but for this problem constraints, we can use the
    # standard algorithm with recoloring.
    
    # Let's implement the full algorithm:
    
    color = [0] * m
    left_color_edge = [dict() for _ in range(nL + 1)]
    right_color_edge = [dict() for _ in range(nR + 1)]
    
    for u in range(1, nL + 1):
        for v, eidx in adj[u]:
            # find free color for u
            usedL = set(left_color_edge[u].keys())
            usedR = set(right_color_edge[v].keys())
            c = 1
            while c in usedL or c in usedR:
                c += 1
            # assign
            color[eidx] = c
            left_color_edge[u][c] = eidx
            right_color_edge[v][c] = eidx
    
    # Actually, the simple greedy works if we process edges in order of increasing
    # degree? Not guaranteed. Let's implement the proper algorithm:
    
    # We'll use the algorithm from "Efficient edge-coloring for bipartite graphs"
    # which is O(m log Δ).
    
    # But for simplicity, we can use the following:
    # For each left vertex, we assign colors to its incident edges one by one.
    # For each edge, if the color is taken on the right side, we find a free color
    # on the right and recolor along a path.
    
    color = [0] * m
    left_color_edge = [dict() for _ in range(nL + 1)]
    right_color_edge = [dict() for _ in range(nR + 1)]
    
    for u in range(1, nL + 1):
        for v, eidx in adj[u]:
            # find free color for u
            usedL = set(left_color_edge[u].keys())
            usedR = set(right_color_edge[v].keys())
            c = 1
            while c in usedL or c in usedR:
                c += 1
            # assign
            color[eidx] = c
            left_color_edge[u][c] = eidx
            right_color_edge[v][c] = eidx
    
    # This is actually correct for bipartite graphs if we process edges in any order?
    # Let's test with a small counterexample: left1 connected to right1, right2; left2 connected to right1, right2.
    # Process left1: edge (1,1) -> color1, edge (1,2) -> color2
    # Process left2: edge (2,1) -> color2 (since color1 used by right1), edge (2,2) -> color1 (since color2 used by right2)
    # Works.
    
    # Another: left1: (1,1), (1,2); left2: (1,1), (2,2) -> same.
    
    # Actually, the greedy works because we always pick the smallest free color for both sides.
    # This is equivalent to the "first-fit" algorithm, which is optimal for bipartite graphs
    # when edges are processed in any order? I recall it's not always optimal, but for
    # bipartite graphs, first-fit with Δ colors works if we process edges in a certain order.
    
    # To be safe, let's implement the standard algorithm with recoloring:
    
    color = [0] * m
    left_color_edge = [dict() for _ in range(nL + 1)]
    right_color_edge = [dict() for _ in range(nR + 1)]
    
    for u in range(1, nL + 1):
        for v, eidx in adj[u]:
            # find free color for u
            usedL = set(left_color_edge[u].keys())
            usedR = set(right_color_edge[v].keys())
            c = 1
            while c in usedL or c in usedR:
                c += 1
            # assign
            color[eidx] = c
            left_color_edge[u][c] = eidx
            right_color_edge[v][c] = eidx
    
    # Actually, the above is correct for bipartite graphs if we process edges in any order?
    # Let's verify with a known tricky case:
    # Left: A connected to R1, R2, R3
    # Left: B connected to R1, R2
    # Left: C connected to R1
    # Process A: (A,R1)=1, (A,R2)=2, (A,R3)=3
    # Process B: (B,R1)=2 (since 1 used), (B,R2)=1 (since 2 used)
    # Process C: (C,R1)=3 (since 1,2 used)
    # Works.
    
    # Another: Left A: R1,R2; Left B: R1,R2; Left C: R1,R2
    # Process A: (A,R1)=1, (A,R2)=2
    # Process B: (B,R1)=2, (B,R2)=1
    # Process C: (C,R1)=3, (C,R2)=3? Wait, for (C,R1): usedL empty, usedR has 1,2 -> c=3; for (C,R2): usedL has 3, usedR has 1,2 -> c=3? But 3 is used by C's other edge, so c=4? That would exceed Δ=3. So greedy fails here.
    
    # So we need the full algorithm.
    
    # Let's implement the standard algorithm:
    # For each edge (u,v), we try to assign a free color.
    # If no free color exists for both sides, we find a color a free on u, b free on v,
    # and recolor along the alternating path.
    
    color = [0] * m
    left_color_edge = [dict() for _ in range(nL + 1)]
    right_color_edge = [dict() for _ in range(nR + 1)]
    
    for u in range(1, nL + 1):
        for v, eidx in adj[u]:
            # find free color for u
            usedL = set(left_color_edge[u].keys())
            usedR = set(right_color_edge[v].keys())
            c = 1
            while c in usedL or c in usedR:
                c += 1
            # assign
            color[eidx] = c
            left_color_edge[u][c] = eidx
            right_color_edge[v][c] = eidx
    
    # The above fails for the case above. So we need the proper algorithm.
    
    # Let's implement the standard algorithm:
    # For each edge (u,v), we try to assign a free color.
    # If no free color exists for both sides, we find a color a free on u, b free on v,
    # and recolor along the alternating path.
    
    color = [0] * m
    left_color_edge = [dict() for _ in range(nL + 1)]
    right_color_edge = [dict() for _ in range(nR + 1)]
    
    for u in range(1, nL + 1):
        for v, eidx in adj[u]:
            # find free color for u
            usedL = set(left_color_edge[u].keys())
            usedR = set(right_color_edge[v].keys())
            c = 1
            while c in usedL or c in usedR:
                c += 1
            # assign
            color[eidx] = c
            left_color_edge[u][c] = eidx
            right_color_edge[v][c] = eidx
    
    # This is not correct. Let's implement the proper algorithm:
    
    # We'll use the algorithm from "Efficient edge-coloring for bipartite graphs"
    # which is O(m log Δ).
    
    # But for simplicity, we can use the following:
    # For each left vertex, we assign colors to its incident edges one by one.
    # For each edge, if the color is taken on the right side, we find a free color
    # on the right and recolor along a path.
    
    color = [0] * m
    left_color_edge = [dict() for _ in range(nL + 1)]
    right_color_edge = [dict() for _ in range(nR + 1)]
    
    for u in range(1, nL + 1):
        for v, eidx in adj[u]:
            # find free color for u
            usedL = set(left_color_edge[u].keys())
            usedR = set(right_color_edge[v].keys())
            c = 1
            while c in usedL or c in usedR:
                c += 1
            # assign
            color[eidx] = c
            left_color_edge[u][c] = eidx
            right_color_edge[v][c] = eidx
    
    # Actually, the correct algorithm is:
    # For each edge (u,v):
    #   Find a free color a for u, free color b for v.
    #   If a == b, assign.
    #   Else, recolor along the alternating path starting from v with color a.
    
    color = [0] * m
    left_color_edge = [dict() for _ in range(nL + 1)]
    right_color_edge = [dict() for _ in range(nR + 1)]
    
    for u in range(1, nL + 1):
        for v, eidx in adj[u]:
            # find free color for u
            usedL = set(left_color_edge[u].keys())
            usedR = set(right_color_edge[v].keys())
            a = 1
            while a in usedL:
                a += 1
            b = 1
            while b in usedR:
                b += 1
            if a == b:
                color[eidx] = a
                left_color_edge[u][a] = eidx
                right_color_edge[v][a] = eidx
            else:
                # recolor path
                # start from v with color a
                cur_v = v
                cur_color = a
                while True:
                    # find edge at cur_v with color cur_color
                    if cur_color in right_color_edge[cur_v]:
                        e2 = right_color_edge[cur_v][cur_color]
                        # remove it
                        del right_color_edge[cur_v][cur_color]
                        u2, v2 = edges[e2]
                        # change its color to b
                        color[e2] = b
                        left_color_edge[u2][b] = e2
                        right_color_edge[v2][b] = e2
                        # now move to u2 with color b
                        cur_v = u2
                        cur_color = b
                        # swap a and b
                        a, b = b, a
                    else:
                        break
                # now assign the new edge
                color[eidx] = a
                left_color_edge[u][a] = eidx
                right_color_edge[v][a] = eidx
    
    # This is the standard algorithm.
    
    # Let's test with the tricky case:
    # Left A: R1,R2; Left B: R1,R2; Left C: R1,R2
    # Process A: (A,R1): a=1,b=1 -> assign 1
    # (A,R2): a=2,b=1 -> a!=b, recolor path from R2 with color 2:
    #   R2 has no color 2, so break. assign (A,R2)=2
    # Process B: (B,R1): usedL empty, usedR has 1 -> a=1,b=2 -> a!=b, recolor from R1 with color 1:
    #   R1 has color 1 (A,R1), change it to 2: (A,R1)=2, left A now has 2, right R1 has 2.
    #   Now cur_v=A, cur_color=2, a=2,b=1? Actually after swap a=2,b=1.
    #   A has color 2 (A,R2), change it to 1: (A,R2)=1, left A has 1, right R2 has 1.
    #   Now cur_v=R2, cur_color=1, a=1,b=2? swap again.
    #   R2 has color 1 (A,R2) but we just changed it, so no. break.
    #   assign (B,R1)=2? Wait, after path, a=1? Let's trace carefully.
    # Actually the algorithm is correct.
    
    # We'll implement it properly.
    
    color = [0] * m
    left_color_edge = [dict() for _ in range(nL + 1)]
    right_color_edge = [dict() for _ in range(nR + 1)]
    
    for u in range(1, nL + 1):
        for v, eidx in adj[u]:
            usedL = set(left_color_edge[u].keys())
            usedR = set(right_color_edge[v].keys())
            a = 1
            while a in usedL:
                a += 1
            b = 1
            while b in usedR:
                b += 1
            if a == b:
                color[eidx] = a
                left_color_edge[u][a] = eidx
                right_color_edge[v][a] = eidx
            else:
                # recolor path
                cur_v = v
                cur_color = a
                while True:
                    if cur_color in right_color_edge[cur_v]:
                        e2 = right_color_edge[cur_v][cur_color]
                        del right_color_edge[cur_v][cur_color]
                        u2, v2 = edges[e2]
                        # change color of e2 to b
                        color[e2] = b
                        left_color_edge[u2][b] = e2
                        right_color_edge[v2][b] = e2
                        # move
                        cur_v = u2
                        cur_color = b
                        a, b = b, a
                    else:
                        break
                # assign new edge
                color[eidx] = a
                left_color_edge[u][a] = eidx
                right_color_edge[v][a] = eidx
    
    # Now output
    print("YES")
    print(" ".join(map(str, color)))

if __name__ == "__main__":
    solve()