import sys

sys.setrecursionlimit(1000000)

data = list(map(int, sys.stdin.buffer.read().split()))
if not data:
    sys.exit()

k, t = data[0], data[1]
triples = []
p = 2

xy = [[0] * k for _ in range(k)]
xz = [[0] * k for _ in range(k)]
yz = [[0] * k for _ in range(k)]

for _ in range(t):
    x, y, z = data[p] - 1, data[p + 1] - 1, data[p + 2] - 1
    p += 3
    triples.append((x, y, z))
    xy[x][y] |= 1 << z
    xz[x][z] |= 1 << y
    yz[y][z] |= 1 << x

if k == 0 or t < k:
    print("NO")
    sys.exit()

columns = 3 * k
root = 0

L = list(range(columns + 1))
R = list(range(columns + 1))
U = list(range(columns + 1))
D = list(range(columns + 1))
C = list(range(columns + 1))
S = [0] * (columns + 1)
ROW = [-1] * (columns + 1)

for i in range(columns + 1):
    L[i] = i - 1 if i > 0 else columns
    R[i] = i + 1 if i < columns else 0
L[0] = columns
R[columns] = 0

for rid, (x, y, z) in enumerate(triples):
    cols = (1 + x, 1 + k + y, 1 + 2 * k + z)
    nodes = []
    for col in cols:
        node = len(L)
        L.append(node)
        R.append(node)
        U.append(U[col])
        D.append(col)
        C.append(col)
        ROW.append(rid)

        D[U[col]] = node
        U[col] = node
        S[col] += 1
        nodes.append(node)

    a, b, c = nodes
    L[a], R[a] = c, b
    L[b], R[b] = a, c
    L[c], R[c] = b, a

for col in range(1, columns + 1):
    if S[col] == 0:
        print("NO")
        sys.exit()

def cover(col):
    R[L[col]] = R[col]
    L[R[col]] = L[col]
    i = D[col]
    while i != col:
        j = R[i]
        while j != i:
            U[D[j]] = U[j]
            D[U[j]] = D[j]
            S[C[j]] -= 1
            j = R[j]
        i = D[i]

def uncover(col):
    i = U[col]
    while i != col:
        j = L[i]
        while j != i:
            S[C[j]] += 1
            U[D[j]] = j
            D[U[j]] = j
            j = L[j]
        i = U[i]
    R[L[col]] = col
    L[R[col]] = col

full = (1 << k) - 1

def pair_matching_possible(matrix, rem_a, rem_b, rem_c):
    adjacency = []
    bits_a = rem_a

    while bits_a:
        bit_a = bits_a & -bits_a
        a = bit_a.bit_length() - 1
        bits_a -= bit_a

        neighbors = 0
        bits_b = rem_b
        row = matrix[a]
        while bits_b:
            bit_b = bits_b & -bits_b
            b = bit_b.bit_length() - 1
            bits_b -= bit_b
            if row[b] & rem_c:
                neighbors |= bit_b

        if neighbors == 0:
            return False
        adjacency.append((neighbors.bit_count(), neighbors))

    adjacency.sort()
    match = [-1] * k

    def augment(left_id, neighbors, seen):
        candidates = neighbors & ~seen[0]
        while candidates:
            bit = candidates & -candidates
            candidates -= bit
            b = bit.bit_length() - 1
            seen[0] |= bit
            previous = match[b]
            if previous == -1:
                match[b] = left_id
                return True
            prev_neighbors = adjacency[previous][1]
            if augment(previous, prev_neighbors, seen):
                match[b] = left_id
                return True
        return False

    for left_id, (_, neighbors) in enumerate(adjacency):
        seen = [0]
        if not augment(left_id, neighbors, seen):
            return False
    return True

solution = []
failed = set()
memo_limit = 700000

def search(depth, used_x, used_y, used_z):
    if R[root] == root:
        return depth == k

    key = used_x | (used_y << k) | (used_z << (2 * k))
    if key in failed:
        return False

    col = R[root]
    best_size = S[col]
    q = R[col]
    while q != root:
        if S[q] < best_size:
            col = q
            best_size = S[q]
            if best_size == 0:
                break
        q = R[q]

    if best_size == 0:
        if len(failed) < memo_limit:
            failed.add(key)
        return False

    rem_x = full ^ used_x
    rem_y = full ^ used_y
    rem_z = full ^ used_z

    if not pair_matching_possible(xy, rem_x, rem_y, rem_z):
        if len(failed) < memo_limit:
            failed.add(key)
        return False
    if not pair_matching_possible(xz, rem_x, rem_z, rem_y):
        if len(failed) < memo_limit:
            failed.add(key)
        return False
    if not pair_matching_possible(yz, rem_y, rem_z, rem_x):
        if len(failed) < memo_limit:
            failed.add(key)
        return False

    cover(col)

    candidates = []
    i = D[col]
    while i != col:
        score = 0
        j = R[i]
        while j != i:
            score += S[C[j]]
            j = R[j]
        candidates.append((score, i))
        i = D[i]

    candidates.sort(reverse=True)

    for _, row_node in candidates:
        rid = ROW[row_node]
        x, y, z = triples[rid]
        solution.append(rid)

        j = R[row_node]
        while j != row_node:
            cover(C[j])
            j = R[j]

        if search(
            depth + 1,
            used_x | (1 << x),
            used_y | (1 << y),
            used_z | (1 << z)
        ):
            return True

        j = L[row_node]
        while j != row_node:
            uncover(C[j])
            j = L[j]

        solution.pop()

    uncover(col)

    if len(failed) < memo_limit:
        failed.add(key)
    return False

if search(0, 0, 0, 0):
    out = ["YES"]
    for rid in solution:
        x, y, z = triples[rid]
        out.append(f"{x + 1} {y + 1} {z + 1}")
    sys.stdout.write("\n".join(out))
else:
    print("NO")