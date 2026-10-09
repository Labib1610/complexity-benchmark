import sys
input = sys.stdin.readline

def solve():
    nL, nR, m = map(int, input().split())
    edges = []
    adj = [[] for _ in range(nL + nR + 1)]  # vertices: 1..nL left, nL+1..nL+nR right
    for i in range(m):
        u, v = map(int, input().split())
        v += nL  # shift right side
        edges.append((u, v))
        adj[u].append((v, i))
        adj[v].append((u, i))
    
    # Find maximum degree
    deg = [0] * (nL + nR + 1)
    for u, v in edges:
        deg[u] += 1
        deg[v] += 1
    Delta = max(deg)
    
    # color of each edge
    color = [-1] * m
    # For each vertex, store which colors are used by incident edges
    used = [set() for _ in range(nL + nR + 1)]
    
    # We'll implement the standard greedy with color interchange
    # For each edge in input order
    for idx, (u, v) in enumerate(edges):
        # find smallest free color for u and v
        cu = 1
        while cu in used[u]:
            cu += 1
        cv = 1
        while cv in used[v]:
            cv += 1
        
        if cu == cv:
            c = cu
        else:
            # Need to recolor along Kempe chain
            # We want to assign cu to edge (u,v), but v already has cu used?
            # Actually cu is free for u, cv is free for v.
            # If cu != cv, we can swap colors along alternating path starting from v with color cu
            # to free cu for v.
            # Standard: find path starting at v, color cu, alternating cu/cv
            # We'll do BFS/DFS to find alternating path
            # We'll use iterative stack
            stack = [(v, cu)]  # start at v, looking for color cu
            parent = {}
            visited = set()
            visited.add(v)
            found = False
            while stack:
                node, col = stack.pop()
                # find an edge from node with color col that is not yet visited
                for nb, eidx in adj[node]:
                    if color[eidx] == col and nb not in visited:
                        visited.add(nb)
                        parent[nb] = (node, col, eidx)
                        # next color to look for is the other one
                        ncol = cv if col == cu else cu
                        stack.append((nb, ncol))
                        # check if nb has color cv free? Actually we want to stop when we find a vertex where cv is free
                        if cv not in used[nb]:
                            found = True
                            # Recolor path
                            cur = nb
                            while cur in parent:
                                pnode, pcol, peidx = parent[cur]
                                # swap colors
                                color[peidx] = pcol
                                # update used sets
                                used[pnode].discard(pcol)
                                used[cur].discard(pcol)
                                # Actually we need to be careful: we are swapping colors along path
                                # Let's do proper Kempe chain: we want to free cu for v.
                                # We'll implement differently below.
                                break
                            break
                        break
                if found:
                    break
            # If not found, we can just assign cu to edge and recolor the path
            # But simpler: we can do a standard Kempe chain recolor
            # Let's implement a clean version:
            # We'll find alternating path starting from v with color cu, ending at a vertex where cu is free.
            # Then swap colors along path.
            # We'll do BFS.
            from collections import deque
            q = deque()
            q.append(v)
            parent = {v: None}
            end = None
            while q:
                node = q.popleft()
                # if cu is free at node (and node != v), we can end
                if node != v and cu not in used[node]:
                    end = node
                    break
                for nb, eidx in adj[node]:
                    if color[eidx] == cu and nb not in parent:
                        parent[nb] = (node, eidx)
                        q.append(nb)
            # Now swap colors along path from end back to v
            cur = end
            while cur != v:
                pnode, eidx = parent[cur]
                # edge between pnode and cur currently has color cu
                # we change it to cv
                color[eidx] = cv
                used[pnode].discard(cu)
                used[cur].discard(cu)
                used[pnode].add(cv)
                used[cur].add(cv)
                # swap cu and cv for next step
                cu, cv = cv, cu
                cur = pnode
            # Now cu is free for v, assign
            c = cu
        
        # assign color c to edge idx
        color[idx] = c
        used[u].add(c)
        used[v].add(c)
    
    # Output
    print("YES")
    print(" ".join(str(c) for c in color))

if __name__ == "__main__":
    solve()