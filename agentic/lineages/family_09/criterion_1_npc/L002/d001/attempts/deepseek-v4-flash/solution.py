n, m, k = map(int, input().split())
edges = []
adj = [0] * n
for _ in range(m):
    u, v = map(int, input().split())
    u -= 1
    v -= 1
    adj[u] |= 1 << v
    adj[v] |= 1 << u

# Split vertices into two halves
mid = n // 2
left_size = mid
right_size = n - mid

# Enumerate independent sets for left half
left_sets = []  # list of (mask, size)
for mask in range(1 << left_size):
    ok = True
    for i in range(left_size):
        if mask >> i & 1:
            if adj[i] & mask:
                ok = False
                break
    if ok:
        left_sets.append((mask, bin(mask).count('1')))

# Enumerate independent sets for right half
right_sets = []
for mask in range(1 << right_size):
    ok = True
    for i in range(right_size):
        if mask >> i & 1:
            if adj[left_size + i] & (mask << left_size):
                ok = False
                break
    if ok:
        right_sets.append((mask, bin(mask).count('1')))

# For each left set, find compatible right sets
# Precompute for each right mask the set of left vertices it conflicts with
right_conflict = []
for rmask, _ in right_sets:
    conflict = 0
    for i in range(right_size):
        if rmask >> i & 1:
            conflict |= adj[left_size + i] & ((1 << left_size) - 1)
    right_conflict.append(conflict)

# Group right sets by size for quick lookup
from collections import defaultdict
right_by_size = defaultdict(list)
for idx, (rmask, rsize) in enumerate(right_sets):
    right_by_size[rsize].append((rmask, right_conflict[idx]))

# Try to find a combination
for lmask, lsize in left_sets:
    need = k - lsize
    if need < 0 or need > right_size:
        continue
    for rmask, rconflict in right_by_size.get(need, []):
        if lmask & rconflict == 0:
            # Found solution
            selected = []
            for i in range(left_size):
                if lmask >> i & 1:
                    selected.append(i + 1)
            for i in range(right_size):
                if rmask >> i & 1:
                    selected.append(left_size + i + 1)
            print("YES")
            print(" ".join(map(str, selected)))
            exit()

print("NO")