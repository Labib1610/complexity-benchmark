import sys

def solve_component(columns, row_indices, triples):
    n = len(columns)
    col_map = {c: i + 1 for i, c in enumerate(columns)}

    row_masks = []
    basis = [0] * n
    for rid in row_indices:
        x, y, z = triples[rid]
        mask = (
            1 << (col_map[x] - 1)
            | 1 << (col_map[y] - 1)
            | 1 << (col_map[z] - 1)
        )
        row_masks.append(mask)

        v = mask
        while v:
            p = v.bit_length() - 1
            if basis[p]:
                v ^= basis[p]
            else:
                basis[p] = v
                break

    target = (1 << n) - 1
    v = target
    while v:
        p = v.bit_length() - 1
        if basis[p]:
            v ^= basis[p]
        else:
            return None

    L = [0] * (n + 1)
    R = [0] * (n + 1)
    U = list(range(n + 1))
    D = list(range(n + 1))
    C = [0] * (n + 1)
    ROW = [-1] * (n + 1)
    size = [0] * (n + 1)

    for i in range(n + 1):
        L[i] = i - 1
        R[i] = i + 1
    L[0] = n
    R[n] = 0
    if n:
        R[0] = 1
        L[1] = 0

    for local_rid, global_rid in enumerate(row_indices):
        x, y, z = triples[global_rid]
        cols = (col_map[x], col_map[y], col_map[z])
        first = -1

        for c in cols:
            idx = len(C)
            C.append(c)
            ROW.append(local_rid)
            L.append(idx)
            R.append(idx)
            U.append(U[c])
            D.append(c)

            D[U[c]] = idx
            U[c] = idx
            size[c] += 1

            if first == -1:
                first = idx
            else:
                left = L[first]
                R[left] = idx
                L[idx] = left
                R[idx] = first
                L[first] = idx

    for c in range(1, n + 1):
        if size[c] == 0:
            return None

    def cover(c):
        R[L[c]] = R[c]
        L[R[c]] = L[c]
        i = D[c]
        while i != c:
            j = R[i]
            while j != i:
                D[U[j]] = D[j]
                U[D[j]] = U[j]
                size[C[j]] -= 1
                j = R[j]
            i = D[i]

    def uncover(c):
        i = U[c]
        while i != c:
            j = L[i]
            while j != i:
                size[C[j]] += 1
                D[U[j]] = j
                U[D[j]] = j
                j = L[j]
            i = U[i]
        R[L[c]] = c
        L[R[c]] = c

    answer = []
    failed = set()
    memo_limit = 500000

    def search(covered):
        if R[0] == 0:
            return True
        if covered in failed:
            return False

        c = R[0]
        best_size = size[c]
        q = R[c]
        while q != 0:
            s = size[q]
            if s < best_size:
                c = q
                best_size = s
                if s <= 1:
                    break
            q = R[q]

        if best_size == 0:
            if len(failed) < memo_limit:
                failed.add(covered)
            return False

        cover(c)
        i = D[c]
        while i != c:
            local_rid = ROW[i]
            answer.append(local_rid)

            j = R[i]
            while j != i:
                cover(C[j])
                j = R[j]

            if search(covered | row_masks[local_rid]):
                return True

            j = L[i]
            while j != i:
                uncover(C[j])
                j = L[j]

            answer.pop()
            i = D[i]

        uncover(c)
        if len(failed) < memo_limit:
            failed.add(covered)
        return False

    if not search(0):
        return None
    return [row_indices[r] for r in answer]


def main():
    data = list(map(int, sys.stdin.buffer.read().split()))
    if not data:
        return

    k, t = data[0], data[1]
    triples_output = []
    triples = []

    parent = list(range(3 * k))
    dsu_size = [1] * (3 * k)

    def find(a):
        while parent[a] != a:
            parent[a] = parent[parent[a]]
            a = parent[a]
        return a

    def union(a, b):
        a = find(a)
        b = find(b)
        if a == b:
            return
        if dsu_size[a] < dsu_size[b]:
            a, b = b, a
        parent[b] = a
        dsu_size[a] += dsu_size[b]

    pos = 2
    for _ in range(t):
        x = data[pos] - 1
        y = data[pos + 1] - 1
        z = data[pos + 2] - 1
        pos += 3

        gx = x
        gy = k + y
        gz = 2 * k + z
        triples.append((gx, gy, gz))
        triples_output.append((x + 1, y + 1, z + 1))
        union(gx, gy)
        union(gx, gz)

    component_columns = {}
    for c in range(3 * k):
        root = find(c)
        component_columns.setdefault(root, []).append(c)

    component_rows = {root: [] for root in component_columns}
    for rid, triple in enumerate(triples):
        root = find(triple[0])
        component_rows[root].append(rid)

    components = []
    for root, columns in component_columns.items():
        counts = [0, 0, 0]
        for c in columns:
            if c < k:
                counts[0] += 1
            elif c < 2 * k:
                counts[1] += 1
            else:
                counts[2] += 1

        if counts[0] != counts[1] or counts[1] != counts[2]:
            print("NO")
            return

        rows = component_rows[root]
        if not rows:
            print("NO")
            return
        components.append((columns, rows))

    components.sort(key=lambda item: len(item[1]))

    selected = []
    for columns, rows in components:
        result = solve_component(columns, rows, triples)
        if result is None:
            print("NO")
            return
        selected.extend(result)

    if len(selected) != k:
        print("NO")
        return

    out = ["YES"]
    for rid in selected:
        x, y, z = triples_output[rid]
        out.append(f"{x} {y} {z}")
    sys.stdout.write("\n".join(out))


if __name__ == "__main__":
    main()