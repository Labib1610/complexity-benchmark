import sys

def main():
    data = list(map(int, sys.stdin.buffer.read().split()))
    if not data:
        return

    k, t = data[0], data[1]
    if t < k:
        print("NO")
        return

    xs = [0] * t
    ys = [0] * t
    zs = [0] * t
    incidence = [0] * (3 * k)
    element_mask = [0] * t

    p = 2
    for i in range(t):
        x = data[p] - 1
        y = data[p + 1] - 1
        z = data[p + 2] - 1
        p += 3

        xs[i] = x
        ys[i] = y
        zs[i] = z

        bit = 1 << i
        incidence[x] |= bit
        incidence[k + y] |= bit
        incidence[2 * k + z] |= bit
        element_mask[i] = (1 << x) | (1 << (k + y)) | (1 << (2 * k + z))

    for mask in incidence:
        if mask == 0:
            print("NO")
            return

    conflicts = [0] * t
    for i in range(t):
        conflicts[i] = incidence[xs[i]] | incidence[k + ys[i]] | incidence[2 * k + zs[i]]

    all_rows = (1 << t) - 1
    all_vertices = (1 << k) - 1
    initial_remaining = (1 << (3 * k)) - 1

    answer = []
    failed = set()
    CACHE_LIMIT = 350000

    def bipartite_perfect(neighbors, left_mask, right_mask):
        vertices = []
        lm = left_mask
        while lm:
            b = lm & -lm
            a = b.bit_length() - 1
            options = neighbors[a] & right_mask
            if options == 0:
                return False
            vertices.append((options.bit_count(), a))
            lm ^= b

        vertices.sort()
        owner = [-1] * k

        def augment(a, seen):
            options = neighbors[a] & right_mask
            while options:
                bbit = options & -options
                options ^= bbit
                b = bbit.bit_length() - 1
                if seen[b]:
                    continue
                seen[b] = True
                previous = owner[b]
                if previous == -1 or augment(previous, seen):
                    owner[b] = a
                    return True
            return False

        for _, a in vertices:
            if not augment(a, [False] * k):
                return False
        return True

    def projection_feasible(active, remaining):
        ux = remaining & all_vertices
        uy = (remaining >> k) & all_vertices
        uz = (remaining >> (2 * k)) & all_vertices

        xy = [0] * k
        xz = [0] * k
        yz = [0] * k

        rows = active
        while rows:
            bit = rows & -rows
            rows ^= bit
            r = bit.bit_length() - 1
            x = xs[r]
            y = ys[r]
            z = zs[r]
            xy[x] |= 1 << y
            xz[x] |= 1 << z
            yz[y] |= 1 << z

        return (
            bipartite_perfect(xy, ux, uy)
            and bipartite_perfect(xz, ux, uz)
            and bipartite_perfect(yz, uy, uz)
        )

    sys.setrecursionlimit(10000)

    def search(active, remaining):
        if remaining == 0:
            return True
        if remaining in failed:
            return False

        rem = remaining
        best_candidates = 0
        best_count = t + 1

        while rem:
            ebit = rem & -rem
            rem ^= ebit
            e = ebit.bit_length() - 1
            candidates = active & incidence[e]
            count = candidates.bit_count()
            if count == 0:
                if len(failed) < CACHE_LIMIT:
                    failed.add(remaining)
                return False
            if count < best_count:
                best_count = count
                best_candidates = candidates
                if count == 1:
                    break

        if best_count > 1 and not projection_feasible(active, remaining):
            if len(failed) < CACHE_LIMIT:
                failed.add(remaining)
            return False

        candidates_list = []
        bits = best_candidates
        while bits:
            bit = bits & -bits
            bits ^= bit
            candidates_list.append(bit.bit_length() - 1)

        if len(candidates_list) > 2:
            candidates_list.sort(
                key=lambda r: (active & conflicts[r]).bit_count()
            )

        for r in candidates_list:
            answer.append(r)
            new_active = active & ~conflicts[r]
            new_remaining = remaining & ~element_mask[r]

            if search(new_active, new_remaining):
                return True
            answer.pop()

        if len(failed) < CACHE_LIMIT:
            failed.add(remaining)
        return False

    if search(all_rows, initial_remaining):
        out = ["YES"]
        for r in answer:
            out.append(f"{xs[r] + 1} {ys[r] + 1} {zs[r] + 1}")
        sys.stdout.write("\n".join(out))
    else:
        print("NO")

if __name__ == "__main__":
    main()