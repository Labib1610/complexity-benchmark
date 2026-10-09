import sys
from collections import deque

input = sys.stdin.readline

n, m = map(int, input().split())
adj = [[] for _ in range(n)]
for _ in range(m):
    u, v = map(int, input().split())
    adj[u-1].append(v-1)
    adj[v-1].append(u-1)

color = [-1] * n
possible = True

for i in range(n):
    if color[i] == -1:
        color[i] = 0
        q = deque([i])
        while q:
            u = q.popleft()
            for v in adj[u]:
                if color[v] == -1:
                    color[v] = color[u] ^ 1
                    q.append(v)
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
    # Lexicographically smallest: assign 1 to color 0, 2 to color 1 normally.
    # But if doing this makes index 0 -> 2 and a vertex with 1 earlier impossible,
    # actually starting from 0 with color 0 gives 1 for the first node, so fine.
    # However, we must ensure the component containing node 0 is fixed as color 0 = 1.
    # For other components, to be lexicographically smallest, we assign 1 to
    # the smallest index in the component.

    # We need to orient components to make overall sequence lexicographically smallest.
    # For each component, find the smallest index and check if giving it color 0
    # (value 1) yields a smaller vector than giving it color 1 (value 2 at that node).

    comp_id = [-1] * n
    comps = []
    comp_num = 0
    for i in range(n):
        if color[i] != -1 and comp_id[i] == -1:
            nodes = []
            q = deque([i])
            comp_id[i] = comp_num
            while q:
                u = q.popleft()
                nodes.append(u)
                for v in adj[u]:
                    if comp_id[v] == -1:
                        comp_id[v] = comp_num
                        q.append(v)
            comps.append(nodes)
            comp_num += 1

    assignment = [0] * n
    for nodes in comps:
        nodes.sort()
        root = nodes[0]
        # Try root color = 0 => assignment = 1
        # Compare with root color = 1 => assignment = 2
        # We see which gives lexicographically smaller for that component.
        # We need actual colors as they are relative; we'll compute both options.

        # First option: root is 0
        # Compute mapping
        base_color0 = color[root]
        # If base color of root is 0, then assignment for n: 1 if color == base, else 2
        # If base color of root is 1, then we invert
        if color[root] == 0:
            option1 = [1 if color[x] == 0 else 2 for x in nodes]
        else:
            option1 = [1 if color[x] == 1 else 2 for x in nodes]

        # Second option: root gets the other value (2)
        if color[root] == 0:
            option2 = [2 if color[x] == 0 else 1 for x in nodes]
        else:
            option2 = [2 if color[x] == 1 else 1 for x in nodes]

        # Choose lexicographically smaller
        if option1 < option2:
            for idx, x in enumerate(nodes):
                assignment[x] = option1[idx]
        else:
            for idx, x in enumerate(nodes):
                assignment[x] = option2[idx]

    print("YES")
    print(" ".join(map(str, assignment)))