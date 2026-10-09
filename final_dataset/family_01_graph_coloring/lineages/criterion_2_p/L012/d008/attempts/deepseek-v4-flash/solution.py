import sys

input = sys.stdin.readline

n, m = map(int, input().split())
edges = []
adj = [[] for _ in range(n)]

for _ in range(m):
    u, v = map(int, input().split())
    u -= 1
    v -= 1
    edges.append((u, v))
    adj[u].append(v)
    adj[v].append(u)

# Check if graph is bipartite
color = [-1] * n
ok = True

for i in range(n):
    if color[i] == -1:
        color[i] = 0
        stack = [i]
        while stack:
            u = stack.pop()
            for v in adj[u]:
                if color[v] == -1:
                    color[v] = color[u] ^ 1
                    stack.append(v)
                elif color[v] == color[u]:
                    ok = False
                    break
            if not ok:
                break
    if not ok:
        break

if not ok:
    print("NO")
    sys.exit()

# Now determine assignment minimizing base-3 value:
# We have two possible colorings: fix color[0] = 0 or fix color[0] = 1
# In both cases, assign height=1 for one color and height=2 for the other.
# We need to check that all constraints (edges) pass checksum.

def check(assign):
    for u, v in edges:
        hu = assign[u]
        hv = assign[v]
        C = hu + 4
        if hv == 1:
            C = C * 2 - 1
        else:  # hv == 2
            C = C + 3
        if (C ^ hu) != 9:
            return False
    return True

heights = [0] * n

# Try both assignments for bipartite coloring
for base in (0, 1):
    assign = [0] * n
    for i in range(n):
        assign[i] = 1 if color[i] == base else 2
    if check(assign):
        # compare lexicographically as base-3 number
        if heights[0] == 0:
            heights = assign[:]
        else:
            # compare base-3 sequence
            for i in range(n):
                if assign[i] < heights[i]:
                    heights = assign[:]
                    break
                elif assign[i] > heights[i]:
                    break

if heights[0] == 0:
    print("NO")
else:
    print("YES")
    print(' '.join(map(str, heights)))