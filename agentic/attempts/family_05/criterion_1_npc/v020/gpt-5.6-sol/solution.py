import sys

def main():
    data = list(map(int, sys.stdin.buffer.read().split()))
    if not data:
        return

    k, t = data[0], data[1]
    triples = []
    degree = [0] * (3 * k)

    es_to_p = [0] * (k * k)
    ep_to_s = [0] * (k * k)
    sp_to_e = [0] * (k * k)

    pos = 2
    for _ in range(t):
        e = data[pos] - 1
        s = data[pos + 1] - 1
        p = data[pos + 2] - 1
        pos += 3

        triples.append((e, s, p))
        degree[e] += 1
        degree[k + s] += 1
        degree[2 * k + p] += 1

        es_to_p[e * k + s] |= 1 << p
        ep_to_s[e * k + p] |= 1 << s
        sp_to_e[s * k + p] |= 1 << e

    if any(x == 0 for x in degree):
        print("NO")
        return

    triples.sort(key=lambda x: (
        degree[x[0]] + degree[k + x[1]] + degree[2 * k + x[2]],
        degree[x[0]] * degree[k + x[1]] * degree[2 * k + x[2]]
    ))

    column_count = 3 * k
    root = column_count
    total_headers = column_count + 1

    L = [0] * total_headers
    R = [0] * total_headers
    U = list(range(total_headers))
    D = list(range(total_headers))
    C = list(range(total_headers))
    S = [0] * total_headers
    row_id = [-1] * total_headers

    for i in range(total_headers):
        L[i] = (i - 1) % total_headers
        R[i] = (i + 1) % total_headers

    for rid, (e, s, p) in enumerate(triples):
        cols = (e, k + s, 2 * k + p)
        nodes = []

        for col in cols:
            idx = len(L)
            L.append(idx)
            R.append(idx)
            U.append(U[col])
            D.append(col)
            C.append(col)
            S.append(0)
            row_id.append(rid)

            D[U[col]] = idx
            U[col] = idx
            S[col] += 1
            nodes.append(idx)

        for i in range(3):
            L[nodes[i]] = nodes[(i - 1) % 3]
            R[nodes[i]] = nodes[(i + 1) % 3]

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

    def pair_has_matching(matrix, rem_a, rem_b, rem_c):
        options = []
        aa = rem_a

        while aa:
            abit = aa & -aa
            a = abit.bit_length() - 1
            aa ^= abit

            choices = 0
            bb = rem_b
            base = a * k

            while bb:
                bbit = bb & -bb
                b = bbit.bit_length() - 1
                bb ^= bbit
                if matrix[base + b] & rem_c:
                    choices |= bbit

            if choices == 0:
                return False
            options.append(choices)

        options.sort(key=int.bit_count)
        matching = [-1] * k

        def augment(i, seen):
            choices = options[i]
            while choices:
                bit = choices & -choices
                choices ^= bit
                if seen[0] & bit:
                    continue
                seen[0] |= bit
                b = bit.bit_length() - 1
                previous = matching[b]
                if previous == -1 or augment(previous, seen):
                    matching[b] = i
                    return True
            return False

        for i in range(len(options)):
            seen = [0]
            if not augment(i, seen):
                return False

        return True

    full_mask = (1 << k) - 1
    solution = []
    failed = set()
    memo_limit = 350000

    def search(used_e, used_s, used_p, depth):
        if R[root] == root:
            return True

        state = used_e | (used_s << k) | (used_p << (2 * k))
        if state in failed:
            return False

        # Periodic Hall-condition pruning on all three bipartite projections.
        if depth % 3 == 0:
            rem_e = full_mask ^ used_e
            rem_s = full_mask ^ used_s
            rem_p = full_mask ^ used_p

            if not pair_has_matching(es_to_p, rem_e, rem_s, rem_p):
                if len(failed) < memo_limit:
                    failed.add(state)
                return False
            if not pair_has_matching(ep_to_s, rem_e, rem_p, rem_s):
                if len(failed) < memo_limit:
                    failed.add(state)
                return False
            if not pair_has_matching(sp_to_e, rem_s, rem_p, rem_e):
                if len(failed) < memo_limit:
                    failed.add(state)
                return False

        col = R[root]
        best_size = S[col]
        cur = R[col]

        while cur != root:
            if S[cur] < best_size:
                col = cur
                best_size = S[cur]
                if best_size <= 1:
                    break
            cur = R[cur]

        if best_size == 0:
            if len(failed) < memo_limit:
                failed.add(state)
            return False

        cover(col)
        node = D[col]

        while node != col:
            rid = row_id[node]
            e, s, p = triples[rid]
            solution.append(rid)

            j = R[node]
            while j != node:
                cover(C[j])
                j = R[j]

            if search(
                used_e | (1 << e),
                used_s | (1 << s),
                used_p | (1 << p),
                depth + 1
            ):
                return True

            j = L[node]
            while j != node:
                uncover(C[j])
                j = L[j]

            solution.pop()
            node = D[node]

        uncover(col)

        if len(failed) < memo_limit:
            failed.add(state)
        return False

    if search(0, 0, 0, 0):
        out = ["YES"]
        for rid in solution:
            e, s, p = triples[rid]
            out.append(f"{e + 1} {s + 1} {p + 1}")
        sys.stdout.write("\n".join(out))
    else:
        print("NO")

if __name__ == "__main__":
    main()