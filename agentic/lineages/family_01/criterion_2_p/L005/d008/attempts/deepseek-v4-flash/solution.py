import sys
input = sys.stdin.readline

n, m = map(int, input().split())
adj = [[] for _ in range(n)]
edges = []
for _ in range(m):
    u, v = map(int, input().split())
    u -= 1
    v -= 1
    adj[u].append(v)
    adj[v].append(u)
    edges.append((u, v))

# Condition: for each i, sum of modes of neighbors + k_i * mode_i = 3*k_i
# Let mode_i = 1 or 2
# If mode_i = 1: sum_neighbors + k_i = 3*k_i => sum_neighbors = 2*k_i
# If mode_i = 2: sum_neighbors + 2*k_i = 3*k_i => sum_neighbors = k_i
# So each vertex has a constraint on the sum of neighbor modes.

# This is a 2-SAT style problem, but we can solve by trying both assignments
# for each connected component.

color = [-1] * n
possible = True

for start in range(n):
    if color[start] != -1:
        continue
    # BFS to assign colors, try both possibilities for start
    for initial in (1, 2):
        c = [-1] * n
        c[start] = initial
        queue = [start]
        ok = True
        while queue:
            u = queue.pop()
            k = len(adj[u])
            if c[u] == 1:
                need_sum = 2 * k
            else:
                need_sum = k
            # sum of neighbors must be need_sum
            # neighbors are 1 or 2, so sum = count1 + 2*count2 = count1 + 2*(k - count1) = 2k - count1
            # so need_sum = 2k - count1 => count1 = 2k - need_sum
            # if c[u] == 1: need_sum = 2k => count1 = 0 => all neighbors 2
            # if c[u] == 2: need_sum = k => count1 = k => all neighbors 1
            # So neighbors are forced!
            if c[u] == 1:
                forced = 2
            else:
                forced = 1
            for v in adj[u]:
                if c[v] == -1:
                    c[v] = forced
                    queue.append(v)
                elif c[v] != forced:
                    ok = False
                    break
            if not ok:
                break
        if ok:
            # check all constraints
            for u in range(n):
                if c[u] == -1:
                    continue
                k = len(adj[u])
                s = sum(c[v] for v in adj[u])
                if c[u] == 1:
                    if s != 2 * k:
                        ok = False
                        break
                else:
                    if s != k:
                        ok = False
                        break
            if ok:
                # assign to global color
                for u in range(n):
                    if c[u] != -1:
                        color[u] = c[u]
                break
        # if not ok, try other initial
    if color[start] == -1:
        possible = False
        break

if not possible:
    print("NO")
else:
    # check if all assigned
    for i in range(n):
        if color[i] == -1:
            # isolated vertex: any mode works, choose 1 for lexicographically smallest
            color[i] = 1
    # verify
    for u, v in edges:
        pass
    for u in range(n):
        k = len(adj[u])
        s = sum(color[v] for v in adj[u])
        if color[u] == 1:
            if s != 2 * k:
                possible = False
                break
        else:
            if s != k:
                possible = False
                break
    if not possible:
        print("NO")
    else:
        print("YES")
        print(" ".join(map(str, color)))