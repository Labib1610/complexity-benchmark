k, t = map(int, input().split())
edges = []
for _ in range(t):
    x, y, z = map(int, input().split())
    edges.append((x - 1, y - 1, z - 1))

# Build bipartite graph between (tech, rig) and window? 
# We need perfect matching between technicians and (rig, window) pairs? Let's think.

# We need to choose exactly k triples with distinct x, y, z. This is 3D matching, which is NP-hard in general.
# But k <= 22, so we can try randomized / backtracking with bitmasks.

# Use DFS + pruning, matching over technicians and rigs/windows using bitmask of used windows.

used_window = 0  # bitmask of used windows
used_rig = 0
# We assign technicians one by one.
# We'll preprocess lists for each technician.
adj = [[] for _ in range(k)]
for x, y, z in edges:
    adj[x].append((y, z))

# Sort edges for each technician by maybe window/rig for pruning (optional)
for i in range(k):
    adj[i].sort(key=lambda p: (p[0], p[1]))

answer = []
found = False

# For speed, we can recursion with memo? Since k small but t up to k^3 = 10648.
# Backtracking with prune: each technician must be assigned exactly once.
# We'll iterate technicians in order that has fewest options (but we can just try 0..k-1)
# Use bitmask for rig and window.

def dfs(idx, rig_mask, win_mask, path):
    global found
    if found:
        return
    if idx == k:
        if rig_mask == (1 << k) - 1 and win_mask == (1 << k) - 1:
            found = True
            for item in path:
                answer.append(item)
        return
    # prune: if impossible to cover all remaining, skip
    # (simple check: popcount)
    if bin(rig_mask).count("1") != idx or bin(win_mask).count("1") != idx:
        # careful: mechanics
        return
    # try options for this technician
    for y, z, _ in adj[idx]:
        if not (rig_mask >> y) & 1 and not (win_mask >> z) & 1:
            path.append((idx + 1, y + 1, z + 1))
            dfs(idx + 1, rig_mask | (1 << y), win_mask | (1 << z), path)
            path.pop()
            if found:
                return

# Ordering by degree might help:
order = sorted(range(k), key=lambda i: len(adj[i]))

# But our recursion assigns by order[i] technician index

def dfs_order(idx, rig_mask, win_mask, path):
    global found
    if found:
        return
    if idx == k:
        # final check
        if rig_mask == (1 << k) - 1 and win_mask == (1 << k) - 1:
            found = True
            answer.extend(path[:])
        return
    tech = order[idx]
    # evaluate all edges of this tech
    for y, z, _ in adj[tech]:
        if (rig_mask >> y) & 1 or (win_mask >> z) & 1:
            continue
        path.append((tech + 1, y + 1, z + 1))
        dfs(idx + 1, rig_mask | (1 << y), win_mask | (1 << z), path)
        path.pop()
        if found:
            return

dfs(0, 0, 0, [])

if found:
    print("YES")
    for x, y, z in answer:
        print(x, y, z)
else:
    print("NO")