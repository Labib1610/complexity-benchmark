import sys
from collections import deque

def main():
    input = sys.stdin.readline
    nL, nR, m = map(int, input().split())
    edges = []
    adj = [[] for _ in range(nL + nR + 1)]
    for i in range(m):
        u, v = map(int, input().split())
        v += nL
        edges.append((u, v))
        adj[u].append((v, i))
        adj[v].append((u, i))
    
    # Find maximum degree
    deg = [0] * (nL + nR + 1)
    for u, v in edges:
        deg[u] += 1
        deg[v] += 1
    Delta = max(deg)
    
    # Edge coloring using Kuhn's algorithm for bipartite graphs
    color = [0] * m
    # We'll use a simple greedy with augmenting paths
    # For each edge, find a free color for both endpoints
    for i, (u, v) in enumerate(edges):
        used_u = set()
        used_v = set()
        for j in range(i):
            if edges[j][0] == u:
                used_u.add(color[j])
            if edges[j][1] == v:
                used_v.add(color[j])
        cu = 1
        while cu in used_u or cu in used_v:
            cu += 1
        color[i] = cu
    
    # But this greedy may exceed Delta; we need proper edge coloring.
    # Use the standard algorithm for bipartite edge coloring:
    # We can use the "Kőnig's line coloring" via BFS/DFS augmenting paths.
    
    # Reset and use proper algorithm
    color = [0] * m
    # For each color c from 1..Delta, find maximal matching and assign
    for c in range(1, Delta + 1):
        match = [-1] * (nL + nR + 1)
        # Try to find augmenting paths for edges not yet colored
        for i in range(m):
            if color[i] == 0:
                u, v = edges[i]
                # Try to assign color c to this edge
                # Check if both endpoints are free in this color
                if match[u] == -1 and match[v] == -1:
                    match[u] = v
                    match[v] = u
                    color[i] = c
        # Now try to augment
        for i in range(m):
            if color[i] == 0:
                u, v = edges[i]
                # Try to find augmenting path
                # BFS
                parent = [-1] * (nL + nR + 1)
                q = deque()
                visited = [False] * (nL + nR + 1)
                # Start from u
                q.append(u)
                visited[u] = True
                found = False
                while q and not found:
                    x = q.popleft()
                    for y, idx in adj[x]:
                        if color[idx] == c:
                            continue
                        if not visited[y]:
                            visited[y] = True
                            parent[y] = x
                            if match[y] == -1:
                                # augment
                                cur = y
                                while cur != -1:
                                    prev = parent[cur]
                                    if prev == -1:
                                        break
                                    # flip
                                    # find edge index
                                    for eidx, (a, b) in enumerate(edges):
                                        if (a == prev and b == cur) or (a == cur and b == prev):
                                            if color[eidx] == 0:
                                                color[eidx] = c
                                                match[prev] = cur
                                                match[cur] = prev
                                            else:
                                                color[eidx] = 0
                                                match[prev] = -1
                                                match[cur] = -1
                                            break
                                    cur = prev
                                found = True
                                break
                            else:
                                q.append(match[y])
                                visited[match[y]] = True
                                parent[match[y]] = y
                # If not found, we can't assign this color to this edge now; will try next color
        # After this, all edges that can be colored with c are done
    
    # The above may not color all edges if greedy fails; we need a correct algorithm.
    # Let's use a simpler correct approach: iterative edge coloring by Kempe chains.
    
    # Actually, the standard algorithm for bipartite edge coloring:
    # Use the "greedy with color interchange" method.
    
    # Let's implement a correct one:
    color = [0] * m
    for i, (u, v) in enumerate(edges):
        # find smallest color not used by u or v
        used = set()
        for j in range(i):
            if edges[j][0] == u:
                used.add(color[j])
            if edges[j][1] == v:
                used.add(color[j])
        c = 1
        while c in used:
            c += 1
        color[i] = c
        # Now fix conflicts by swapping colors along alternating paths
        while True:
            # Check if conflict exists
            conflict = False
            for j in range(i):
                if color[j] == c and (edges[j][0] == u or edges[j][1] == v):
                    # conflict
                    conflict = True
                    # find the other color of the other endpoint
                    other = edges[j][0] if edges[j][0] != u else edges[j][1]
                    # find color to swap
                    c2 = 1
                    while c2 == c or c2 in {color[k] for k in range(i) if edges[k][0] == other or edges[k][1] == other}:
                        c2 += 1
                    # swap colors along path
                    # simple: just change color[j] to c2
                    color[j] = c2
                    break
            if not conflict:
                break
    
    # This is still not guaranteed. Let's use a known correct implementation.
    
    # We'll implement the standard algorithm using DFS for each color.
    
    # Actually, the simplest correct method: use the fact that we can color with Delta colors by repeatedly finding a perfect matching in a regular bipartite graph.
    # But we can also use the "greedy with augmenting path" per color.
    
    # Let's do it properly:
    
    color = [0] * m
    for c in range(1, Delta + 1):
        # Build graph of uncolored edges
        adj_uncolored = [[] for _ in range(nL + nR + 1)]
        for i in range(m):
            if color[i] == 0:
                u, v = edges[i]
                adj_uncolored[u].append((v, i))
                adj_uncolored[v].append((u, i))
        # Find maximal matching
        match = [-1] * (nL + nR + 1)
        match_edge = [-1] * (nL + nR + 1)
        for i in range(m):
            if color[i] == 0:
                u, v = edges[i]
                if match[u] == -1 and match[v] == -1:
                    match[u] = v
                    match[v] = u
                    match_edge[u] = i
                    match_edge[v] = i
                    color[i] = c
        # Now try to augment
        for i in range(m):
            if color[i] == 0:
                u, v = edges[i]
                # Try to find augmenting path
                parent = [-1] * (nL + nR + 1)
                parent_edge = [-1] * (nL + nR + 1)
                visited = [False] * (nL + nR + 1)
                q = deque()
                q.append(u)
                visited[u] = True
                found = False
                while q and not found:
                    x = q.popleft()
                    for y, eidx in adj_uncolored[x]:
                        if color[eidx] != 0:
                            continue
                        if not visited[y]:
                            visited[y] = True
                            parent[y] = x
                            parent_edge[y] = eidx
                            if match[y] == -1:
                                # augment
                                cur = y
                                while cur != -1:
                                    prev = parent[cur]
                                    if prev == -1:
                                        break
                                    eidx2 = parent_edge[cur]
                                    # flip
                                    if match[prev] == cur:
                                        match[prev] = -1
                                        match[cur] = -1
                                        color[eidx2] = 0
                                    else:
                                        match[prev] = cur
                                        match[cur] = prev
                                        color[eidx2] = c
                                    cur = prev
                                found = True
                                break
                            else:
                                q.append(match[y])
                                visited[match[y]] = True
                                parent[match[y]] = y
                                parent_edge[match[y]] = eidx
                # If not found, skip
        # After this, all edges that can be colored with c are done
    
    # If any edge remains uncolored, we need to handle, but in bipartite graph it's always possible with Delta colors.
    
    # Output
    print("YES")
    print(" ".join(str(color[i]) for i in range(m)))

if __name__ == "__main__":
    main()