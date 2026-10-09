import sys

sys.setrecursionlimit(1_000_000)

data = list(map(int, sys.stdin.buffer.read().split()))
if not data:
    sys.exit()

k, t = data[0], data[1]
triples = []
row_keys = []

shift_y = k
shift_z = 2 * k

p = 2
for _ in range(t):
    x = data[p] - 1
    y = data[p + 1] - 1
    z = data[p + 2] - 1
    p += 3
    triples.append((x, y, z))
    row_keys.append((1 << x) | (1 << (shift_y + y)) | (1 << (shift_z + z)))

column_count = 3 * k
root = column_count

L = [0] * (column_count + 1)
R = [0] * (column_count + 1)
U = [0] * (column_count + 1)
D = [0] * (column_count + 1)
C = list(range(column_count + 1))
ROW = [-1] * (column_count + 1)
S = [0] * (column_count + 1)

for i in range(column_count):
    L[i] = i - 1 if i > 0 else root
    R[i] = i + 1 if i + 1 < column_count else root
    U[i] = D[i] = i

L[root] = column_count - 1
R[root] = 0
U[root] = D[root] = root

for rid, (x, y, z) in enumerate(triples):
    cols = (x, k + y, 2 * k + z)
    first = -1
    previous = -1

    for col in cols:
        node = len(L)
        L.append(node)
        R.append(node)
        U.append(U[col])
        D.append(col)
        C.append(col)
        ROW.append(rid)
        S.append(0)

        D[U[col]] = node
        U[col] = node
        S[col] += 1

        if first == -1:
            first = node
        else:
            L[node] = previous
            R[previous] = node
        previous = node

    L[first] = previous
    R[previous] = first


def cover(col):
    R[L[col]] = R[col]
    L[R[col]] = L[col]

    i = D[col]
    while i != col:
        j = R[i]
        while j != i:
            D[U[j]] = D[j]
            U[D[j]] = U[j]
            S[C[j]] -= 1
            j = R[j]
        i = D[i]


def uncover(col):
    i = U[col]
    while i != col:
        j = L[i]
        while j != i:
            S[C[j]] += 1
            D[U[j]] = j
            U[D[j]] = j
            j = L[j]
        i = U[i]

    R[L[col]] = col
    L[R[col]] = col


def has_perfect_matching(adj, available_a_mask, available_b_mask):
    vertices = []
    bits = available_a_mask
    while bits:
        lb = bits & -bits
        a = lb.bit_length() - 1
        options = adj[a] & available_b_mask
        if options == 0:
            return False
        vertices.append((options.bit_count(), a))
        bits ^= lb

    vertices.sort()
    matched = [-1] * k
    seen = [0] * k
    stamp = 0

    def augment(a):
        nonlocal stamp
        options = adj[a] & available_b_mask
        while options:
            lb = options & -options
            b = lb.bit_length() - 1
            options ^= lb
            if seen[b] == stamp:
                continue
            seen[b] = stamp
            old = matched[b]
            if old == -1 or augment(old):
                matched[b] = a
                return True
        return False

    for _, a in vertices:
        stamp += 1
        if not augment(a):
            return False
    return True


full_mask = (1 << k) - 1


def projection_prune(state):
    used_x = state & full_mask
    used_y = (state >> shift_y) & full_mask
    used_z = (state >> shift_z) & full_mask

    free_x = full_mask ^ used_x
    free_y = full_mask ^ used_y
    free_z = full_mask ^ used_z

    xy = [0] * k
    xz = [0] * k
    yz = [0] * k

    for rid, (x, y, z) in enumerate(triples):
        if state & row_keys[rid]:
            continue
        xy[x] |= 1 << y
        xz[x] |= 1 << z
        yz[y] |= 1 << z

    if not has_perfect_matching(xy, free_x, free_y):
        return False
    if not has_perfect_matching(xz, free_x, free_z):
        return False
    if not has_perfect_matching(yz, free_y, free_z):
        return False
    return True


solution = []
failed = set()
MEMO_LIMIT = 1_500_000


def search(depth, state):
    if R[root] == root:
        return True

    if state in failed:
        return False

    col = R[root]
    best = col
    best_size = S[col]
    col = R[col]

    while col != root:
        if S[col] < best_size:
            best = col
            best_size = S[col]
            if best_size == 0:
                break
        col = R[col]

    if best_size == 0:
        if len(failed) < MEMO_LIMIT:
            failed.add(state)
        return False

    if (depth <= 6 and depth % 2 == 0) or (depth > 6 and depth % 4 == 0):
        if not projection_prune(state):
            if len(failed) < MEMO_LIMIT:
                failed.add(state)
            return False

    candidates = []
    node = D[best]
    while node != best:
        score = 0
        j = node
        while True:
            score += S[C[j]]
            j = R[j]
            if j == node:
                break
        candidates.append((score, node))
        node = D[node]

    candidates.sort()

    cover(best)

    for _, row_node in candidates:
        rid = ROW[row_node]
        solution.append(rid)

        j = R[row_node]
        while j != row_node:
            cover(C[j])
            j = R[j]

        if search(depth + 1, state | row_keys[rid]):
            return True

        j = L[row_node]
        while j != row_node:
            uncover(C[j])
            j = L[j]

        solution.pop()

    uncover(best)

    if len(failed) < MEMO_LIMIT:
        failed.add(state)
    return False


if search(0, 0):
    out = ["YES"]
    for rid in solution:
        x, y, z = triples[rid]
        out.append(f"{x + 1} {y + 1} {z + 1}")
    sys.stdout.write("\n".join(out))
else:
    sys.stdout.write("NO")