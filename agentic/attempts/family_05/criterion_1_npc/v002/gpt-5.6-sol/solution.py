import sys

sys.setrecursionlimit(1_000_000)

data = list(map(int, sys.stdin.buffer.read().split()))
if not data:
    raise SystemExit

k, t = data[0], data[1]
full = (1 << k) - 1

rows = []
by_vertex = [[] for _ in range(3 * k)]

class DSU:
    def __init__(self, n):
        self.p = list(range(n))
        self.sz = [1] * n

    def find(self, x):
        while self.p[x] != x:
            self.p[x] = self.p[self.p[x]]
            x = self.p[x]
        return x

    def union(self, a, b):
        a = self.find(a)
        b = self.find(b)
        if a == b:
            return
        if self.sz[a] < self.sz[b]:
            a, b = b, a
        self.p[b] = a
        self.sz[a] += self.sz[b]

dsu = DSU(3 * k)

pos = 2
for i in range(t):
    x = data[pos] - 1
    y = data[pos + 1] - 1
    z = data[pos + 2] - 1
    pos += 3

    vx, vy, vz = x, k + y, 2 * k + z
    mask = (1 << vx) | (1 << vy) | (1 << vz)
    rows.append((mask, x, y, z))
    by_vertex[vx].append(i)
    by_vertex[vy].append(i)
    by_vertex[vz].append(i)
    dsu.union(vx, vy)
    dsu.union(vx, vz)

components_vertices = {}
for v in range(3 * k):
    root = dsu.find(v)
    components_vertices.setdefault(root, []).append(v)

components_rows = {root: [] for root in components_vertices}
for i, (_, x, y, z) in enumerate(rows):
    root = dsu.find(x)
    components_rows[root].append(i)

components = []
for root, vertices in components_vertices.items():
    cx = cy = cz = 0
    target = 0
    tx = ty = tz = 0

    for v in vertices:
        target |= 1 << v
        if v < k:
            cx += 1
            tx |= 1 << v
        elif v < 2 * k:
            cy += 1
            ty |= 1 << (v - k)
        else:
            cz += 1
            tz |= 1 << (v - 2 * k)

    if cx != cy or cy != cz:
        print("NO")
        raise SystemExit

    component_row_ids = components_rows[root]
    if cx > 0 and not component_row_ids:
        print("NO")
        raise SystemExit

    components.append(
        (len(component_row_ids) / max(1, cx), target, tx, ty, tz,
         vertices, component_row_ids)
    )

degrees = [len(lst) for lst in by_vertex]

def row_priority(rid):
    _, x, y, z = rows[rid]
    return degrees[x] + degrees[k + y] + degrees[2 * k + z]

for lst in by_vertex:
    lst.sort(key=row_priority)

components.sort(key=lambda c: c[0])

answer = []

def solve_component(target, tx, ty, tz, vertices, component_row_ids):
    failed = set()
    path = []
    ordered_vertices = sorted(vertices, key=lambda v: degrees[v])

    def has_perfect_matching(left_mask, right_mask, adjacency):
        left = []
        bits = left_mask
        while bits:
            b = bits & -bits
            u = b.bit_length() - 1
            if adjacency[u] & right_mask == 0:
                return False
            left.append(u)
            bits ^= b

        left.sort(key=lambda u: (adjacency[u] & right_mask).bit_count())
        match_right = [-1] * k
        seen = [0] * k
        token = 0

        def augment(u):
            nonlocal token
            options = adjacency[u] & right_mask
            while options:
                b = options & -options
                v = b.bit_length() - 1
                options ^= b
                if seen[v] == token:
                    continue
                seen[v] = token
                old = match_right[v]
                if old == -1 or augment(old):
                    match_right[v] = u
                    return True
            return False

        for u in left:
            token += 1
            if not augment(u):
                return False
        return True

    def projection_feasible(used):
        ux = used & full
        uy = (used >> k) & full
        uz = (used >> (2 * k)) & full

        ax = tx & ~ux
        ay = ty & ~uy
        az = tz & ~uz

        adj_xy = [0] * k
        adj_xz = [0] * k
        adj_yz = [0] * k

        for rid in component_row_ids:
            mask, x, y, z = rows[rid]
            if mask & used == 0:
                adj_xy[x] |= 1 << y
                adj_xz[x] |= 1 << z
                adj_yz[y] |= 1 << z

        return (
            has_perfect_matching(ax, ay, adj_xy)
            and has_perfect_matching(ax, az, adj_xz)
            and has_perfect_matching(ay, az, adj_yz)
        )

    def dfs(used):
        if used == target:
            return True
        if used in failed:
            return False

        best_candidates = None
        best_count = 10**9

        for v in ordered_vertices:
            if used & (1 << v):
                continue

            candidates = []
            limit = best_count
            for rid in by_vertex[v]:
                if rows[rid][0] & used == 0:
                    candidates.append(rid)
                    if len(candidates) >= limit:
                        break

            count = len(candidates)
            if count == 0:
                if len(failed) < 700_000:
                    failed.add(used)
                return False

            if count < best_count:
                best_count = count
                best_candidates = candidates

        if best_count > 1 and not projection_feasible(used):
            if len(failed) < 700_000:
                failed.add(used)
            return False

        for rid in best_candidates:
            mask = rows[rid][0]
            path.append(rid)
            if dfs(used | mask):
                return True
            path.pop()

        if len(failed) < 700_000:
            failed.add(used)
        return False

    if dfs(0):
        return path
    return None

for _, target, tx, ty, tz, vertices, component_row_ids in components:
    result = solve_component(target, tx, ty, tz, vertices, component_row_ids)
    if result is None:
        print("NO")
        raise SystemExit
    answer.extend(result)

if len(answer) != k:
    print("NO")
else:
    out = ["YES"]
    for rid in answer:
        _, x, y, z = rows[rid]
        out.append(f"{x + 1} {y + 1} {z + 1}")
    sys.stdout.write("\n".join(out))