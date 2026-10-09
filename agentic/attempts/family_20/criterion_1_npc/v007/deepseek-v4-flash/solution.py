import sys
from collections import deque

def solve():
    input = sys.stdin.readline
    n, m = map(int, input().split())
    edges = []
    adj = [[] for _ in range(n)]
    for i in range(m):
        u, v = map(int, input().split())
        u -= 1
        v -= 1
        edges.append((u, v))
        adj[u].append((v, i))
        adj[v].append((u, i))
    
    # Find a perfect matching using simple augmenting path algorithm
    match = [-1] * n  # matched edge index
    # We'll use a simple greedy + augmenting path
    # Since graph is cubic and bridgeless, perfect matching exists.
    # Use standard algorithm: repeatedly find augmenting paths.
    
    def has_augmenting_path(start, match, adj):
        parent = [-1] * n
        parent_edge = [-1] * n
        visited = [False] * n
        q = deque([start])
        visited[start] = True
        while q:
            u = q.popleft()
            for v, ei in adj[u]:
                if visited[v]:
                    continue
                visited[v] = True
                parent[v] = u
                parent_edge[v] = ei
                if match[v] == -1:
                    # found augmenting path
                    return v, parent, parent_edge
                w = edges[match[v]][0] ^ edges[match[v]][1] ^ v
                visited[w] = True
                parent[w] = v
                parent_edge[w] = match[v]
                q.append(w)
        return None, parent, parent_edge
    
    # Greedy initial matching
    for u in range(n):
        if match[u] == -1:
            for v, ei in adj[u]:
                if match[v] == -1:
                    match[u] = ei
                    match[v] = ei
                    break
    
    # Augment until perfect
    while True:
        # find unmatched vertex
        start = -1
        for i in range(n):
            if match[i] == -1:
                start = i
                break
        if start == -1:
            break
        end, parent, parent_edge = has_augmenting_path(start, match, adj)
        if end is None:
            # Should not happen for bridgeless cubic
            print("NO")
            return
        # flip along path
        v = end
        while v != start:
            ei = parent_edge[v]
            u = parent[v]
            # remove old match if any
            if match[u] != -1:
                old_v = edges[match[u]][0] ^ edges[match[u]][1] ^ u
                match[old_v] = -1
            match[u] = ei
            match[v] = ei
            v = u
    
    # Now match[] contains edge index for each vertex
    color = [0] * m
    # Color matching edges with 1
    for u in range(n):
        ei = match[u]
        color[ei] = 1
    
    # Remaining edges form even cycles
    # Build adjacency for remaining edges
    rem_adj = [[] for _ in range(n)]
    for i, (u, v) in enumerate(edges):
        if color[i] == 0:
            rem_adj[u].append((v, i))
            rem_adj[v].append((u, i))
    
    # Color cycles with 2 and 3
    visited = [False] * n
    for i in range(n):
        if not visited[i] and rem_adj[i]:
            # start BFS/DFS
            stack = [(i, -1, 2)]  # node, parent edge, color to assign
            visited[i] = True
            while stack:
                u, pe, c = stack.pop()
                for v, ei in rem_adj[u]:
                    if ei == pe:
                        continue
                    if color[ei] == 0:
                        color[ei] = c
                        if not visited[v]:
                            visited[v] = True
                            stack.append((v, ei, 5 - c))  # 2<->3
                    else:
                        # already colored, just continue
                        pass
    
    # Check counts
    cnt = [0,0,0]
    for c in color:
        cnt[c-1] += 1
    if cnt[0] != n//2 or cnt[1] != n//2 or cnt[2] != n//2:
        print("NO")
        return
    
    print("YES")
    print(" ".join(str(c) for c in color))

if __name__ == "__main__":
    solve()