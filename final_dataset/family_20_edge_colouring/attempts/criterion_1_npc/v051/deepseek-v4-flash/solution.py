import sys
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

color = [-1] * m

# Find a perfect matching using greedy + augmenting paths
def find_perfect_matching(adj, used_edges):
    match_to = [-1] * n
    for start in range(n):
        if match_to[start] != -1:
            continue
        # BFS to find augmenting path
        parent = [-1] * n
        parent_edge = [-1] * n
        visited = [False] * n
        queue = [start]
        visited[start] = True
        found = False
        while queue and not found:
            u = queue.pop(0)
            for v, ei in adj[u]:
                if used_edges[ei]:
                    continue
                if not visited[v]:
                    visited[v] = True
                    parent[v] = u
                    parent_edge[v] = ei
                    if match_to[v] == -1:
                        # augment
                        cur = v
                        while cur != -1:
                            p = parent[cur]
                            if p == -1:
                                break
                            ei = parent_edge[cur]
                            used_edges[ei] = True
                            match_to[cur] = p
                            match_to[p] = cur
                            cur = p
                        found = True
                        break
                    else:
                        queue.append(v)
        if not found:
            return False
    return True

used_edges = [False] * m
for color_id in range(3):
    if not find_perfect_matching(adj, used_edges):
        print("NO")
        sys.exit()
    # mark edges of this matching with color_id
    for i in range(m):
        if used_edges[i] and color[i] == -1:
            color[i] = color_id + 1
    # reset used_edges for next matching
    used_edges = [False] * m

# Check all edges colored
if -1 in color:
    print("NO")
else:
    print("YES")
    print(" ".join(map(str, color)))