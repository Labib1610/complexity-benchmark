import sys
input = sys.stdin.readline

n, m, k = map(int, input().split())
adj = [[] for _ in range(n + 1)]
for _ in range(m):
    u, v = map(int, input().split())
    adj[u].append(v)
    adj[v].append(u)

color = [-1] * (n + 1)
components = []  # (list of nodes in comp, color0_count, color1_count)

for i in range(1, n + 1):
    if color[i] == -1:
        stack = [i]
        color[i] = 0
        nodes = []
        cnt = [0, 0]
        while stack:
            u = stack.pop()
            nodes.append(u)
            cnt[color[u]] += 1
            for v in adj[u]:
                if color[v] == -1:
                    color[v] = color[u] ^ 1
                    stack.append(v)
        components.append((nodes, cnt[0], cnt[1]))

# dp over components: possible sums of one color from each component
possible = [False] * (n + 1)
possible[0] = True
parent = [-1] * (n + 1)
choice = [-1] * (n + 1)

for idx, (nodes, c0, c1) in enumerate(components):
    new_possible = [False] * (n + 1)
    for s in range(n + 1):
        if possible[s]:
            if s + c0 <= n and not new_possible[s + c0]:
                new_possible[s + c0] = True
                parent[s + c0] = s
                choice[s + c0] = 0
            if s + c1 <= n and not new_possible[s + c1]:
                new_possible[s + c1] = True
                parent[s + c1] = s
                choice[s + c1] = 1
    possible = new_possible

if not possible[k]:
    print("NO")
else:
    print("YES")
    selected = []
    s = k
    comp_idx = len(components) - 1
    while comp_idx >= 0:
        nodes, c0, c1 = components[comp_idx]
        ch = choice[s]
        if ch == 0:
            selected.extend([u for u in nodes if color[u] == 0])
        else:
            selected.extend([u for u in nodes if color[u] == 1])
        s = parent[s]
        comp_idx -= 1
    print(" ".join(map(str, selected)))