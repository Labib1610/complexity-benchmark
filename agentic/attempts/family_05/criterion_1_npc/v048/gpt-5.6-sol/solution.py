import sys

sys.setrecursionlimit(10000)

data = list(map(int, sys.stdin.buffer.read().split()))
if len(data) < 2:
    sys.exit()

k, t = data[0], data[1]

cs = [0] * t
es = [0] * t
gs = [0] * t
row_vertex_mask = [0] * t
incidence = [0] * (3 * k)

p = 2
for i in range(t):
    c = data[p] - 1
    e = data[p + 1] - 1
    g = data[p + 2] - 1
    p += 3

    cs[i] = c
    es[i] = e
    gs[i] = g

    vm = (1 << c) | (1 << (k + e)) | (1 << (2 * k + g))
    row_vertex_mask[i] = vm

    rb = 1 << i
    incidence[c] |= rb
    incidence[k + e] |= rb
    incidence[2 * k + g] |= rb

if t < k:
    print("NO")
    sys.exit()

full_component_mask = (1 << k) - 1
for part in range(3):
    for i in range(k):
        if incidence[part * k + i] == 0:
            print("NO")
            sys.exit()

def has_perfect_matching(adj, left_mask, right_mask):
    left = []
    x = left_mask
    while x:
        b = x & -x
        i = b.bit_length() - 1
        options = adj[i] & right_mask
        if options == 0:
            return False
        left.append((options.bit_count(), i))
        x ^= b

    left.sort()
    match = [-1] * k

    def augment(u, seen):
        options = adj[u] & right_mask & ~seen[0]
        while options:
            b = options & -options
            options ^= b
            v = b.bit_length() - 1
            seen[0] |= b
            old = match[v]
            if old == -1 or augment(old, seen):
                match[v] = u
                return True
        return False

    for _, u in left:
        if not augment(u, [0]):
            return False
    return True

def projection_feasible(active, uncovered):
    cm = uncovered & full_component_mask
    em = (uncovered >> k) & full_component_mask
    gm = (uncovered >> (2 * k)) & full_component_mask

    ce = [0] * k
    cg = [0] * k
    eg = [0] * k

    x = active
    while x:
        b = x & -x
        idx = b.bit_length() - 1
        x ^= b

        c = cs[idx]
        e = es[idx]
        g = gs[idx]
        ce[c] |= 1 << e
        cg[c] |= 1 << g
        eg[e] |= 1 << g

    return (
        has_perfect_matching(ce, cm, em)
        and has_perfect_matching(cg, cm, gm)
        and has_perfect_matching(eg, em, gm)
    )

all_rows = (1 << t) - 1
all_vertices = (1 << (3 * k)) - 1
solution = []
failed = set()
CACHE_LIMIT = 500000

def search(active, uncovered):
    if uncovered == 0:
        return True
    if uncovered in failed:
        return False

    best_candidates = 0
    best_count = t + 1

    vertices = uncovered
    while vertices:
        vb = vertices & -vertices
        vertices ^= vb
        v = vb.bit_length() - 1
        candidates = active & incidence[v]
        count = candidates.bit_count()

        if count == 0:
            if len(failed) < CACHE_LIMIT:
                failed.add(uncovered)
            return False

        if count < best_count:
            best_count = count
            best_candidates = candidates
            if count == 1:
                break

    remaining = (uncovered & full_component_mask).bit_count()
    if best_count > 1 and remaining >= 4:
        if not projection_feasible(active, uncovered):
            if len(failed) < CACHE_LIMIT:
                failed.add(uncovered)
            return False

    candidates_ordered = []
    x = best_candidates
    while x:
        b = x & -x
        idx = b.bit_length() - 1
        x ^= b

        conflict = (
            incidence[cs[idx]]
            | incidence[k + es[idx]]
            | incidence[2 * k + gs[idx]]
        )
        score = (active & conflict).bit_count()
        candidates_ordered.append((score, idx, conflict))

    candidates_ordered.sort(key=lambda item: item[0])

    for _, idx, conflict in candidates_ordered:
        solution.append(idx)
        if search(
            active & ~conflict,
            uncovered ^ row_vertex_mask[idx]
        ):
            return True
        solution.pop()

    if len(failed) < CACHE_LIMIT:
        failed.add(uncovered)
    return False

if search(all_rows, all_vertices):
    out = ["YES"]
    for idx in solution:
        out.append(f"{cs[idx] + 1} {es[idx] + 1} {gs[idx] + 1}")
    sys.stdout.write("\n".join(out))
else:
    print("NO")