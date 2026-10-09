import sys
from collections import deque

input = sys.stdin.readline

n_in, n_out, m = map(int, input().split())
edges = []
adj_in = [[] for _ in range(n_in + 1)]
adj_out = [[] for _ in range(n_out + 1)]

for i in range(m):
    u, v = map(int, input().split())
    edges.append((u, v))
    adj_in[u].append((v, i))
    adj_out[v].append((u, i))

# Find Δ
delta = 0
for u in range(1, n_in + 1):
    delta = max(delta, len(adj_in[u]))
for v in range(1, n_out + 1):
    delta = max(delta, len(adj_out[v]))

color = [0] * m  # 1..delta

# color_in[u][c] = edge index colored c at ingress u
# color_out[v][c] = edge index colored c at egress v
color_in = [[-1] * (delta + 1) for _ in range(n_in + 1)]
color_out = [[-1] * (delta + 1) for _ in range(n_out + 1)]

for idx, (u, v) in enumerate(edges):
    # find smallest free color at u and v
    cu = 1
    while color_in[u][cu] != -1:
        cu += 1
    cv = 1
    while color_out[v][cv] != -1:
        cv += 1

    if cu == cv:
        # assign directly
        color[idx] = cu
        color_in[u][cu] = idx
        color_out[v][cu] = idx
    else:
        # need to recolor alternating path
        # start from v with color cu
        current_color = cu
        current_vertex = ('out', v)
        path_edges = []
        visited_in = [False] * (n_in + 1)
        visited_out = [False] * (n_out + 1)

        while True:
            if current_vertex[0] == 'out':
                vv = current_vertex[1]
                if visited_out[vv]:
                    break
                visited_out[vv] = True
                eidx = color_out[vv][current_color]
                if eidx == -1:
                    break
                path_edges.append(eidx)
                uu = edges[eidx][0]
                current_vertex = ('in', uu)
                current_color = cv if current_color == cu else cu
            else:
                uu = current_vertex[1]
                if visited_in[uu]:
                    break
                visited_in[uu] = True
                eidx = color_in[uu][current_color]
                if eidx == -1:
                    break
                path_edges.append(eidx)
                vv = edges[eidx][1]
                current_vertex = ('out', vv)
                current_color = cv if current_color == cu else cu

        # Recolor path
        for i, eidx in enumerate(path_edges):
            new_c = cv if i % 2 == 0 else cu
            old_c = color[eidx]
            uu, vv = edges[eidx]
            color_in[uu][old_c] = -1
            color_out[vv][old_c] = -1
            color[eidx] = new_c
            color_in[uu][new_c] = eidx
            color_out[vv][new_c] = eidx

        # Now assign the new edge
        color[idx] = cu
        color_in[u][cu] = idx
        color_out[v][cu] = idx

print("YES")
print(" ".join(map(str, color)))