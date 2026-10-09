import sys

sys.setrecursionlimit(10000)

data = list(map(int, sys.stdin.buffer.read().split()))
if not data:
    sys.exit()

k, t = data[0], data[1]
triples = []
xy_z = [0] * (k * k)
xz_y = [0] * (k * k)
yz_x = [0] * (k * k)

p = 2
for _ in range(t):
    x = data[p] - 1
    y = data[p + 1] - 1
    z = data[p + 2] - 1
    p += 3
    triples.append((x, y, z))
    xy_z[x * k + y] |= 1 << z
    xz_y[x * k + z] |= 1 << y
    yz_x[y * k + z] |= 1 << x

if t < k:
    print("NO")
    sys.exit()

ncol = 3 * k
root = ncol
size = ncol + 1

L = [0] * size
R = [0] * size
U = list(range(size))
D = list(range(size))
C = list(range(size))
S = [0] * size
RID = [-1] * size

if ncol:
    for i in range(ncol):
        L[i] = i - 1 if i else root
        R[i] = i + 1 if i + 1 < ncol else root
    L[root] = ncol - 1
    R[root] = 0
else:
    L[root] = R[root] = root

for rid, (x, y, z) in enumerate(triples):
    cols = (x, k + y, 2 * k + z)
    nodes = []
    for col in cols:
        idx = len(L)
        nodes.append(idx)

        L.append(idx)
        R.append(idx)
        C.append(col)
        S.append(0)
        RID.append(rid)

        up = U[col]
        U.append(up)
        D.append(col)
        D[up] = idx
        U[col] = idx
        S[col] += 1

    a, b, c = nodes
    L[a], R[a] = c, b
    L[b], R[b] = a, c
    L[c], R[c] = b, a

for col in range(ncol):
    if S[col] == 0:
        print("NO")
        sys.exit()

ALL = (1 << k) - 1

def projection_matching(table, used_a, used_b, used_c):
    rem_a = ALL ^ used_a
    rem_b = ALL ^ used_b
    rem_c = ALL ^ used_c

    adjacency = []
    bits = rem_a
    while bits:
        bit = bits & -bits
        a = bit.bit_length() - 1
        bits ^= bit

        adj = 0
        bb = rem_b
        base = a * k
        while bb:
            bbit = bb & -bb
            b = bbit.bit_length() - 1
            bb ^= bbit
            if table[base + b] & rem_c:
                adj |= bbit

        if adj == 0:
            return False
        adjacency.append((adj.bit_count(), a, adj))

    adjacency.sort()
    match_b = [-1] * k

    def augment(a, adj, seen):
        bits2 = adj & ~seen[0]
        while bits2:
            bbit = bits2 & -bits2
            bits2 ^= bbit
            seen[0] |= bbit
            b = bbit.bit_length() - 1
            old = match_b[b]
            if old == -1:
                match_b[b] = a
                return True

            old_adj = 0
            base_old = old * k
            bb2 = rem_b
            while bb2:
                q = bb2 & -bb2
                bb2 ^= q
                bj = q.bit_length() - 1
                if table[base_old + bj] & rem_c:
                    old_adj |= q

            if augment(old, old_adj, seen):
                match_b[b] = a
                return True
        return False

    for _, a, adj in adjacency:
        seen = [0]
        if not augment(a, adj, seen):
            return False
    return True

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

answer = []
failed = set()
MEMO_LIMIT = 1_000_000

def remember(key):
    if len(failed) < MEMO_LIMIT:
        failed.add(key)

def search(mx, my, mz):
    if R[root] == root:
        return True

    key = mx | (my << k) | (mz << (2 * k))
    if key in failed:
        return False

    remaining = k - mx.bit_count()
    if remaining >= 2:
        if not projection_matching(xy_z, mx, my, mz):
            remember(key)
            return False
        if not projection_matching(xz_y, mx, mz, my):
            remember(key)
            return False
        if not projection_matching(yz_x, my, mz, mx):
            remember(key)
            return False

    col = R[root]
    best_size = S[col]
    q = R[col]
    while q != root:
        sq = S[q]
        if sq < best_size:
            col = q
            best_size = sq
            if best_size <= 1:
                break
        q = R[q]

    if best_size == 0:
        remember(key)
        return False

    cover(col)
    row_node = D[col]

    while row_node != col:
        rid = RID[row_node]
        x, y, z = triples[rid]
        answer.append(rid)

        j = R[row_node]
        while j != row_node:
            cover(C[j])
            j = R[j]

        if search(mx | (1 << x), my | (1 << y), mz | (1 << z)):
            return True

        j = L[row_node]
        while j != row_node:
            uncover(C[j])
            j = L[j]

        answer.pop()
        row_node = D[row_node]

    uncover(col)
    remember(key)
    return False

if search(0, 0, 0):
    out = ["YES"]
    for rid in answer:
        x, y, z = triples[rid]
        out.append(f"{x + 1} {y + 1} {z + 1}")
    sys.stdout.write("\n".join(out))
else:
    print("NO")