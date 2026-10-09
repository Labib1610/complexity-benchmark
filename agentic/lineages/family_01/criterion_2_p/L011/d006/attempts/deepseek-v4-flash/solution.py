import sys
sys.setrecursionlimit(1 << 20)
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
possible = True

# First, check bipartiteness and assign initial colors
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
                    possible = False
                    break
            if not possible:
                break
    if not possible:
        break

if not possible:
    print("NO")
else:
    # Now we have a valid 2-coloring (0/1). We want lexicographically smallest
    # assignment of 1/2, where 1 corresponds to color 0 and 2 to color 1,
    # but we can flip colors per connected component.
    comp = [-1] * n
    comp_id = 0
    for i in range(n):
        if comp[i] == -1:
            stack = [i]
            comp[i] = comp_id
            while stack:
                u = stack.pop()
                for v in adj[u]:
                    if comp[v] == -1:
                        comp[v] = comp_id
                        stack.append(v)
            comp_id += 1

    # For each component, decide whether to flip to make lexicographically smallest
    flip = [0] * comp_id
    for c in range(comp_id):
        # Count how many vertices in this component have color 0 vs 1
        # We want the smallest index in the component to be 1 if possible
        # So if the smallest index has color 1, we flip the component
        min_idx = None
        for i in range(n):
            if comp[i] == c:
                if min_idx is None or i < min_idx:
                    min_idx = i
        if color[min_idx] == 1:
            flip[c] = 1

    ans = []
    for i in range(n):
        val = color[i] ^ flip[comp[i]]
        ans.append(1 if val == 0 else 2)

    print("YES")
    print(" ".join(map(str, ans)))