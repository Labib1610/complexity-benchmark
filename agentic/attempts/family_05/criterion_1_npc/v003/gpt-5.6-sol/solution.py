import sys

sys.setrecursionlimit(1000000)

data = list(map(int, sys.stdin.buffer.read().split()))
if len(data) < 2:
    sys.exit()

k, t = data[0], data[1]
rows = []
incidence = [0] * (3 * k)

xy_z = [0] * (k * k)
xz_y = [0] * (k * k)
yz_x = [0] * (k * k)

pos = 2
for i in range(t):
    x = data[pos] - 1
    y = data[pos + 1] - 1
    z = data[pos + 2] - 1
    pos += 3

    rows.append((x, y, z))
    bit = 1 << i
    incidence[x] |= bit
    incidence[k + y] |= bit
    incidence[2 * k + z] |= bit

    xy_z[x * k + y] |= 1 << z
    xz_y[x * k + z] |= 1 << y
    yz_x[y * k + z] |= 1 << x

if t == 0:
    print("NO")
    sys.exit()

for mask in incidence:
    if mask == 0:
        print("NO")
        sys.exit()

row_columns = [0] * t
conflicts = [0] * t
for i, (x, y, z) in enumerate(rows):
    row_columns[i] = (1 << x) | (1 << (k + y)) | (1 << (2 * k + z))
    conflicts[i] = incidence[x] | incidence[k + y] | incidence[2 * k + z]

full_values = (1 << k) - 1
full_columns = (1 << (3 * k)) - 1
all_rows = (1 << t) - 1

def linear_possible(active, target):
    basis = [0] * (3 * k)
    rank = 0
    needed_rank = target.bit_count()

    bits = active
    while bits:
        low = bits & -bits
        idx = low.bit_length() - 1
        bits ^= low

        v = row_columns[idx]
        while v:
            p = v.bit_length() - 1
            b = basis[p]
            if b:
                v ^= b
            else:
                basis[p] = v
                rank += 1
                break

        if rank >= needed_rank:
            return True

    v = target
    while v:
        p = v.bit_length() - 1
        b = basis[p]
        if not b:
            return False
        v ^= b
    return True

def has_perfect_matching(adj, left_vertices):
    left_vertices.sort(key=lambda u: adj[u].bit_count())
    match = [-1] * k

    def augment(u):
        nonlocal seen
        choices = adj[u] & ~seen
        while choices:
            bit = choices & -choices
            choices ^= bit
            v = bit.bit_length() - 1
            seen |= bit
            previous = match[v]
            if previous == -1 or augment(previous):
                match[v] = u
                return True
        return False

    for u in left_vertices:
        seen = 0
        if not augment(u):
            return False
    return True

def projection_possible(covered):
    used_x = covered & full_values
    used_y = (covered >> k) & full_values
    used_z = (covered >> (2 * k)) & full_values

    rem_x = full_values ^ used_x
    rem_y = full_values ^ used_y
    rem_z = full_values ^ used_z

    xs = []
    bits = rem_x
    while bits:
        bit = bits & -bits
        bits ^= bit
        xs.append(bit.bit_length() - 1)

    ys = []
    bits = rem_y
    while bits:
        bit = bits & -bits
        bits ^= bit
        ys.append(bit.bit_length() - 1)

    adj = [0] * k
    for x in xs:
        ybits = rem_y
        mask = 0
        base = x * k
        while ybits:
            bit = ybits & -ybits
            ybits ^= bit
            y = bit.bit_length() - 1
            if xy_z[base + y] & rem_z:
                mask |= bit
        adj[x] = mask
        if mask == 0:
            return False
    if not has_perfect_matching(adj, xs[:]):
        return False

    adj = [0] * k
    for x in xs:
        zbits = rem_z
        mask = 0
        base = x * k
        while zbits:
            bit = zbits & -zbits
            zbits ^= bit
            z = bit.bit_length() - 1
            if xz_y[base + z] & rem_y:
                mask |= bit
        adj[x] = mask
        if mask == 0:
            return False
    if not has_perfect_matching(adj, xs[:]):
        return False

    adj = [0] * k
    for y in ys:
        zbits = rem_z
        mask = 0
        base = y * k
        while zbits:
            bit = zbits & -zbits
            zbits ^= bit
            z = bit.bit_length() - 1
            if yz_x[base + z] & rem_x:
                mask |= bit
        adj[y] = mask
        if mask == 0:
            return False
    return has_perfect_matching(adj, ys[:])

path = []
dead = set()
dead_limit = 1_000_000

def dfs(active, covered, depth):
    if depth == k:
        return covered == full_columns

    if covered in dead:
        return False

    uncovered = full_columns ^ covered
    best_candidates = 0
    best_count = t + 1
    degrees = [0] * (3 * k)

    bits = uncovered
    while bits:
        bit = bits & -bits
        bits ^= bit
        c = bit.bit_length() - 1
        candidates = active & incidence[c]
        count = candidates.bit_count()
        degrees[c] = count
        if count == 0:
            if len(dead) < dead_limit:
                dead.add(covered)
            return False
        if count < best_count:
            best_count = count
            best_candidates = candidates
            if count == 1:
                break

    if best_count > 1:
        target = uncovered
        if depth == 0 or depth % 3 == 0 or best_count >= 8:
            if not linear_possible(active, target):
                if len(dead) < dead_limit:
                    dead.add(covered)
                return False

        if depth == 0 or depth % 4 == 0:
            if not projection_possible(covered):
                if len(dead) < dead_limit:
                    dead.add(covered)
                return False

    candidates_list = []
    bits = best_candidates
    while bits:
        bit = bits & -bits
        bits ^= bit
        r = bit.bit_length() - 1
        x, y, z = rows[r]
        score = degrees[x] + degrees[k + y] + degrees[2 * k + z]
        candidates_list.append((score, r))

    if len(candidates_list) > 1:
        candidates_list.sort()

    for _, r in candidates_list:
        path.append(r)
        new_covered = covered | row_columns[r]
        new_active = active & ~conflicts[r]
        if dfs(new_active, new_covered, depth + 1):
            return True
        path.pop()

    if len(dead) < dead_limit:
        dead.add(covered)
    return False

if dfs(all_rows, 0, 0):
    out = ["YES"]
    for idx in path:
        x, y, z = rows[idx]
        out.append(f"{x + 1} {y + 1} {z + 1}")
    sys.stdout.write("\n".join(out))
else:
    print("NO")