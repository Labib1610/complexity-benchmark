import sys
from collections import deque

input = sys.stdin.readline

n, m = map(int, input().split())
adj = [[] for _ in range(n)]
for _ in range(m):
    u, v = map(int, input().split())
    u -= 1
    v -= 1
    adj[u].append(v)
    adj[v].append(u)

color = [-1] * n
visited = [False] * n

def bfs(start, start_color):
    # returns coloring list for this component or None if conflict
    q = deque()
    q.append(start)
    color[start] = start_color
    comp_nodes = [start]
    while q:
        u = q.popleft()
        for v in adj[u]:
            if color[v] == -1:
                color[v] = 1 - color[u]
                q.append(v)
                comp_nodes.append(v)
            elif color[v] == color[u]:
                return None
    return comp_nodes

# We'll collect components
components = []
temp_color = [-1] * n
for i in range(n):
    if temp_color[i] == -1:
        # try both colorings
        comp_nodes = []
        # first try with 0
        color = [-1] * n
        res = bfs(i, 0)
        if res is None:
            print("NO")
            sys.exit()
        comp_nodes = res
        # store both possible colorings for this component
        coloring0 = [color[node] for node in comp_nodes]
        # reset and try with 1
        color = [-1] * n
        res = bfs(i, 1)
        if res is None:
            print("NO")
            sys.exit()
        coloring1 = [color[node] for node in comp_nodes]
        components.append((comp_nodes, coloring0, coloring1))
        # mark visited
        for node in comp_nodes:
            temp_color[node] = 0

# Now choose lexicographically smallest overall
final_x = [0] * n
for comp_nodes, col0, col1 in components:
    # Build two possible s sequences for this component
    s0 = [col0[idx] + 1 for idx in range(len(comp_nodes))]
    s1 = [col1[idx] + 1 for idx in range(len(comp_nodes))]
    # Compare lexicographically by node index order
    # We need to compare based on actual node indices
    # So create mapping from node -> value for both options
    map0 = {comp_nodes[i]: s0[i] for i in range(len(comp_nodes))}
    map1 = {comp_nodes[i]: s1[i] for i in range(len(comp_nodes))}
    # Compare by sorted node indices
    sorted_nodes = sorted(comp_nodes)
    for node in sorted_nodes:
        if map0[node] < map1[node]:
            for nd in comp_nodes:
                final_x[nd] = map0[nd] - 1
            break
        elif map0[node] > map1[node]:
            for nd in comp_nodes:
                final_x[nd] = map1[nd] - 1
            break
    else:
        # equal, pick either (0)
        for nd in comp_nodes:
            final_x[nd] = map0[nd] - 1

# Output
print("YES")
print(' '.join(str(x + 1) for x in final_x))