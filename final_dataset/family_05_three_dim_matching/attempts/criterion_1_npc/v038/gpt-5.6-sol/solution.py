import sys

sys.setrecursionlimit(1_000_000)


def solve():
    data = list(map(int, sys.stdin.buffer.read().split()))
    if len(data) < 2:
        return

    k, t = data[0], data[1]
    triples = []
    incidence = [0] * (3 * k)
    elems = []

    p = 2
    for i in range(t):
        a, b, c = data[p] - 1, data[p + 1] - 1, data[p + 2] - 1
        p += 3
        triples.append((a, b, c))
        es = (a, k + b, 2 * k + c)
        elems.append(es)
        bit = 1 << i
        incidence[es[0]] |= bit
        incidence[es[1]] |= bit
        incidence[es[2]] |= bit

    if t < k:
        print("NO")
        return

    full_uncovered = (1 << (3 * k)) - 1
    full_active = (1 << t) - 1

    for mask in incidence:
        if mask == 0:
            print("NO")
            return

    failed = set()
    memo_limit = 600_000
    answer = []

    def projected_matchings_possible(active, uncovered):
        adj_ab = [0] * k
        adj_ac = [0] * k
        adj_bc = [0] * k

        m = active
        while m:
            bit = m & -m
            i = bit.bit_length() - 1
            a, b, c = triples[i]
            adj_ab[a] |= 1 << b
            adj_ac[a] |= 1 << c
            adj_bc[b] |= 1 << c
            m ^= bit

        amask = uncovered & ((1 << k) - 1)
        bmask = (uncovered >> k) & ((1 << k) - 1)
        cmask = (uncovered >> (2 * k)) & ((1 << k) - 1)

        def has_perfect_matching(adj, left_mask, right_mask):
            left = []
            lm = left_mask
            while lm:
                bit = lm & -lm
                u = bit.bit_length() - 1
                options = adj[u] & right_mask
                if options == 0:
                    return False
                left.append(u)
                lm ^= bit

            left.sort(key=lambda u: (adj[u] & right_mask).bit_count())
            match_right = [-1] * k

            def augment(u):
                nonlocal seen
                options = adj[u] & right_mask
                while options:
                    bit = options & -options
                    options ^= bit
                    v = bit.bit_length() - 1
                    if seen & bit:
                        continue
                    seen |= bit
                    if match_right[v] == -1 or augment(match_right[v]):
                        match_right[v] = u
                        return True
                return False

            for u in left:
                seen = 0
                if not augment(u):
                    return False
            return True

        return (
            has_perfect_matching(adj_ab, amask, bmask)
            and has_perfect_matching(adj_ac, amask, cmask)
            and has_perfect_matching(adj_bc, bmask, cmask)
        )

    def remember(state):
        if len(failed) < memo_limit:
            failed.add(state)

    def dfs(uncovered, active):
        initial_uncovered = uncovered
        initial_len = len(answer)

        if uncovered in failed:
            return False

        while True:
            if uncovered == 0:
                return True

            counts = [0] * (3 * k)
            min_count = t + 1
            chosen_element = -1

            um = uncovered
            while um:
                bit = um & -um
                e = bit.bit_length() - 1
                cnt = (incidence[e] & active).bit_count()
                counts[e] = cnt
                if cnt == 0:
                    del answer[initial_len:]
                    remember(initial_uncovered)
                    remember(uncovered)
                    return False
                if cnt < min_count:
                    min_count = cnt
                    chosen_element = e
                um ^= bit

            if min_count != 1:
                break

            candidate_mask = incidence[chosen_element] & active
            row_bit = candidate_mask & -candidate_mask
            row = row_bit.bit_length() - 1
            answer.append(row)

            e1, e2, e3 = elems[row]
            uncovered &= ~((1 << e1) | (1 << e2) | (1 << e3))
            active &= ~incidence[e1]
            active &= ~incidence[e2]
            active &= ~incidence[e3]

            if uncovered in failed:
                del answer[initial_len:]
                remember(initial_uncovered)
                return False

        if not projected_matchings_possible(active, uncovered):
            del answer[initial_len:]
            remember(initial_uncovered)
            remember(uncovered)
            return False

        candidates_mask = incidence[chosen_element] & active
        candidates = []
        while candidates_mask:
            bit = candidates_mask & -candidates_mask
            row = bit.bit_length() - 1
            candidates.append(row)
            candidates_mask ^= bit

        candidates.sort(
            key=lambda row: (
                counts[elems[row][0]]
                + counts[elems[row][1]]
                + counts[elems[row][2]]
            )
        )

        for row in candidates:
            e1, e2, e3 = elems[row]
            new_uncovered = uncovered & ~(
                (1 << e1) | (1 << e2) | (1 << e3)
            )
            if new_uncovered in failed:
                continue

            new_active = active
            new_active &= ~incidence[e1]
            new_active &= ~incidence[e2]
            new_active &= ~incidence[e3]

            answer.append(row)
            if dfs(new_uncovered, new_active):
                return True
            answer.pop()

        del answer[initial_len:]
        remember(initial_uncovered)
        remember(uncovered)
        return False

    if dfs(full_uncovered, full_active):
        out = ["YES"]
        for i in answer:
            a, b, c = triples[i]
            out.append(f"{a + 1} {b + 1} {c + 1}")
        print("\n".join(out))
    else:
        print("NO")


if __name__ == "__main__":
    solve()