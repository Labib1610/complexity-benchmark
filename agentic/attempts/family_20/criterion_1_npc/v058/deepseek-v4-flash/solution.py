import sys
sys.setrecursionlimit(10000)

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
    
    # Find a perfect matching using greedy + augmenting paths
    match_edge = [-1] * n  # which edge index is used to match this vertex
    match_to = [-1] * n    # matched partner vertex
    
    def augment(u, visited):
        for v, ei in adj[u]:
            if visited[v]:
                continue
            visited[v] = True
            if match_to[v] == -1 or augment(match_to[v], visited):
                match_to[u] = v
                match_to[v] = u
                match_edge[u] = ei
                match_edge[v] = ei
                return True
        return False
    
    for u in range(n):
        if match_to[u] == -1:
            visited = [False] * n
            visited[u] = True
            augment(u, visited)
    
    # Check if perfect matching found
    if any(match_to[i] == -1 for i in range(n)):
        print("NO")
        return
    
    color = [0] * m
    # Color matching edges with 1
    for i in range(n):
        if match_edge[i] != -1:
            color[match_edge[i]] = 1
    
    # Build graph of remaining edges (degree 2)
    rem_adj = [[] for _ in range(n)]
    for i, (u, v) in enumerate(edges):
        if color[i] == 0:
            rem_adj[u].append((v, i))
            rem_adj[v].append((u, i))
    
    # 2-color the cycles
    visited = [False] * n
    for start in range(n):
        if not visited[start] and rem_adj[start]:
            # traverse cycle
            u = start
            prev = -1
            while True:
                visited[u] = True
                # pick next edge not going back to prev
                for v, ei in rem_adj[u]:
                    if v != prev:
                        break
                # assign color 2 or 3 alternating
                if color[ei] == 0:
                    # determine color based on previous edge color
                    if prev != -1:
                        # find previous edge color
                        for vv, eprev in rem_adj[prev]:
                            if vv == u:
                                color[ei] = 2 if color[eprev] == 3 else 3
                                break
                    else:
                        color[ei] = 2
                prev = u
                u = v
                if u == start:
                    break
    
    # Verify
    for u in range(n):
        cols = set()
        for v, ei in adj[u]:
            cols.add(color[ei])
        if len(cols) != 3:
            print("NO")
            return
    
    print("YES")
    print(" ".join(str(c) for c in color))

if __name__ == "__main__":
    solve()