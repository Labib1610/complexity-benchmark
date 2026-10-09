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
    
    delta = max(max(degL), max(degR), 1)
    
    # adjacency list for left vertices: list of (right_vertex, edge_index)
    adjL = [[] for _ in range(nL + 1)]
    adjR = [[] for _ in range(nR + 1)]
    
    for idx, (u, v) in enumerate(edges):
        adjL[u].append((v, idx))
        adjR[v].append((u, idx))
    
    color = [0] * m
    
    # We'll use a simple greedy with recoloring (Kőnig's line coloring)
    # For each edge, find a free color for both endpoints, if conflict, do a recoloring path.
    
    # color_usedL[u][c] = True if color c used at left u
    # color_usedR[v][c] = True if color c used at right v
    # We'll store as sets for simplicity, but for performance use arrays of sets.
    
    usedL = [set() for _ in range(nL + 1)]
    usedR = [set() for _ in range(nR + 1)]
    
    for idx, (u, v) in enumerate(edges):
        # find smallest color not used at u and v
        c = 1
        while c in usedL[u] or c in usedR[v]:
            c += 1
        # assign
        color[idx] = c
        usedL[u].add(c)
        usedR[v].add(c)
        
        # Now fix conflicts: if c was already used at u or v, we need to recolor
        # But since we picked smallest free for both, no conflict initially.
        # However, recoloring may be needed if we later assign same color to another edge sharing a vertex.
        # We'll do a proper algorithm: for each edge, if conflict, find augmenting path.
        
        # Actually, the simple greedy above may fail. We need a proper algorithm.
        # Let's implement the standard algorithm for bipartite edge coloring with Δ colors.
    
    # We'll implement the algorithm from scratch:
    # For each edge (u,v), find a free color for u and v.
    # If they differ, assign.
    # If same, find a color free at u but used at v, and recolor along alternating path.
    
    # Reset
    color = [0] * m
    usedL = [set() for _ in range(nL + 1)]
    usedR = [set() for _ in range(nR + 1)]
    
    for idx, (u, v) in enumerate(edges):
        # find free color for u
        cu = 1
        while cu in usedL[u]:
            cu += 1
        # find free color for v
        cv = 1
        while cv in usedR[v]:
            cv += 1
        
        if cu != cv:
            color[idx] = cu
            usedL[u].add(cu)
            usedR[v].add(cu)
        else:
            # need to recolor
            # find a color c2 free at u but used at v (or vice versa)
            c2 = 1
            while c2 in usedL[u] or c2 not in usedR[v]:
                c2 += 1
            # Now c2 is free at u, used at v
            # We'll do alternating path from v using color cu and c2
            # Standard algorithm:
            # Start at v, find edge colored cu, recolor it to c2, then move to other endpoint, etc.
            
            # We'll implement the path recoloring
            # We need to know which edge has which color at each vertex.
            # We'll store edge index per color per vertex.
            
            # For simplicity, we'll store color -> edge index for each vertex
            edgeL = [dict() for _ in range(nL + 1)]
            edgeR = [dict() for _ in range(nR + 1)]
            
            # But we haven't built these yet. Let's build them as we go.
            # Actually, we can rebuild from color[] each time, but that's O(m) per edge -> too slow.
            # Better: maintain edgeL and edgeR as we assign.
            
            # Let's redo with proper structures.
    
    # Given time, we'll implement a known efficient method:
    # Use the algorithm from "Bipartite edge coloring" using BFS to find augmenting paths.
    
    # We'll store for each vertex and color the edge index.
    edgeL = [{} for _ in range(nL + 1)]
    edgeR = [{} for _ in range(nR + 1)]
    
    for idx, (u, v) in enumerate(edges):
        # find free color for u
        cu = 1
        while cu in edgeL[u]:
            cu += 1
        # find free color for v
        cv = 1
        while cv in edgeR[v]:
            cv += 1
        
        if cu != cv:
            color[idx] = cu
            edgeL[u][cu] = idx
            edgeR[v][cu] = idx
        else:
            # find color c2 free at u but used at v
            c2 = 1
            while c2 in edgeL[u] or c2 not in edgeR[v]:
                c2 += 1
            # Now c2 is free at u, used at v
            # We'll do alternating path from v using colors cu and c2
            # Start at v, find edge colored cu, recolor to c2, then move to other endpoint, etc.
            
            # We'll implement BFS/DFS to find path
            # Path alternates: v --(cu)--> u' --(c2)--> v' --(cu)--> ...
            # until we reach a vertex where cu is free.
            
            # We'll do iterative:
            current_vertex = v
            current_side = 'R'
            current_color = cu
            path_edges = []
            
            while True:
                if current_side == 'R':
                    # find edge at current_vertex with color current_color
                    if current_color in edgeR[current_vertex]:
                        eidx = edgeR[current_vertex][current_color]
                        path_edges.append(eidx)
                        # move to left endpoint
                        u2, v2 = edges[eidx]
                        current_vertex = u2
                        current_side = 'L'
                        # switch color
                        current_color = c2 if current_color == cu else cu
                    else:
                        # cu is free at this right vertex
                        break
                else:
                    # left side
                    if current_color in edgeL[current_vertex]:
                        eidx = edgeL[current_vertex][current_color]
                        path_edges.append(eidx)
                        u2, v2 = edges[eidx]
                        current_vertex = v2
                        current_side = 'R'
                        current_color = c2 if current_color == cu else cu
                    else:
                        break
            
            # Now recolor path_edges: swap cu and c2 along the path
            for eidx in path_edges:
                old = color[eidx]
                new = c2 if old == cu else cu
                u2, v2 = edges[eidx]
                # remove old
                del edgeL[u2][old]
                del edgeR[v2][old]
                # add new
                color[eidx] = new
                edgeL[u2][new] = eidx
                edgeR[v2][new] = eidx
            
            # Now assign current edge with cu
            color[idx] = cu
            edgeL[u][cu] = idx
            edgeR[v][cu] = idx
    
    # Output
    print("YES")
    print(" ".join(map(str, color)))

if __name__ == "__main__":
    solve()