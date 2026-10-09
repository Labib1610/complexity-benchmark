import sys
sys.setrecursionlimit(1000000)

def solve():
    input = sys.stdin.readline
    n, m = map(int, input().split())
    edges = []
    adj = [[] for _ in range(n)]
    for idx in range(m):
        u, v = map(int, input().split())
        u -= 1
        v -= 1
        edges.append((u, v))
        adj[u].append((v, idx))
        adj[v].append((u, idx))
    
    color = [-1] * m
    
    # We'll find a 3-edge-coloring using a known constructive method:
    # Since graph is cubic, we can find a perfect matching, remove it,
    # then the remaining graph is 2-regular (disjoint cycles), which is 2-edge-colorable.
    
    # Step 1: Find a perfect matching using greedy + augmenting paths
    match = [-1] * n  # matched edge index for each vertex
    used = [False] * m
    
    def augment(u, visited):
        for v, eidx in adj[u]:
            if used[eidx] or visited[v]:
                continue
            visited[v] = True
            if match[v] == -1 or augment(match[v], visited):
                match[v] = u
                match[u] = v
                used[eidx] = True
                return True
        return False
    
    for u in range(n):
        if match[u] == -1:
            visited = [False] * n
            augment(u, visited)
    
    # Now match[] gives a perfect matching (since n even and cubic graph has perfect matching)
    # Color those edges with color 1
    for u in range(n):
        if match[u] != -1 and u < match[u]:
            # find edge index
            for v, eidx in adj[u]:
                if v == match[u]:
                    color[eidx] = 1
                    break
    
    # Remove matched edges from adjacency
    remaining_adj = [[] for _ in range(n)]
    for u in range(n):
        for v, eidx in adj[u]:
            if color[eidx] == -1:
                remaining_adj[u].append((v, eidx))
    
    # Remaining graph is 2-regular -> cycles. Color each cycle alternately with 2 and 3.
    visited_vertex = [False] * n
    for start in range(n):
        if not visited_vertex[start] and remaining_adj[start]:
            # traverse cycle
            cycle_edges = []
            cur = start
            prev = -1
            while True:
                visited_vertex[cur] = True
                # pick next edge not going back to prev
                nxt = None
                for v, eidx in remaining_adj[cur]:
                    if v != prev:
                        nxt = (v, eidx)
                        break
                if nxt is None:
                    break
                cycle_edges.append(nxt[1])
                prev, cur = cur, nxt[0]
                if cur == start:
                    break
            # color alternately
            for i, eidx in enumerate(cycle_edges):
                color[eidx] = 2 if i % 2 == 0 else 3
    
    # Check if all colored
    if -1 in color:
        print("NO")
        return
    
    print("YES")
    print(" ".join(str(c) for c in color))

if __name__ == "__main__":
    solve()