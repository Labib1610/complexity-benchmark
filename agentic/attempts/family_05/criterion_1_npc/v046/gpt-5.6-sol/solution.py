import sys

sys.setrecursionlimit(1_000_000)


def main():
    data = list(map(int, sys.stdin.buffer.read().split()))
    if len(data) < 2:
        return

    k, t = data[0], data[1]
    if t < k:
        print("NO")
        return

    xs = [0] * t
    ys = [0] * t
    zs = [0] * t
    adjacency = [0] * (3 * k)

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
        adjacency[x] |= bit
        adjacency[k + y] |= bit
        adjacency[2 * k + z] |= bit

    for a in adjacency:
        if a == 0:
            print("NO")
            return

    conflicts = [0] * t
    for i in range(t):
        conflicts[i] = (
            adjacency[xs[i]]
            | adjacency[k + ys[i]]
            | adjacency[2 * k + zs[i]]
        )

    all_rows = (1 << t) - 1
    full_covered = (1 << (3 * k)) - 1
    full_resource_mask = (1 << k) - 1

    failed = set()
    memo_limit = 600_000
    answer = []

    def has_matching(graph, left_mask, right_mask):
        left = []
        b = left_mask
        while b:
            lb = b & -b
            u = lb.bit_length() - 1
            options = graph[u] & right_mask
            if options == 0:
                return False
            left.append((options.bit_count(), u))
            b ^= lb

        left.sort()
        match = [-1] * k

        def augment(u, seen):
            options = graph[u] & right_mask & ~seen
            while options:
                vb = options & -options
                options ^= vb
                v = vb.bit_length() - 1
                previous = match[v]
                if previous == -1:
                    match[v] = u
                    return True, seen | vb
                ok, new_seen = augment(previous, seen | vb)
                seen = new_seen
                if ok:
                    match[v] = u
                    return True, seen
            return False, seen

        for _, u in left:
            ok, _ = augment(u, 0)
            if not ok:
                return False
        return True

    def projection_feasible(available, covered):
        covered_x = covered & full_resource_mask
        covered_y = (covered >> k) & full_resource_mask
        covered_z = (covered >> (2 * k)) & full_resource_mask

        rem_x = full_resource_mask ^ covered_x
        rem_y = full_resource_mask ^ covered_y
        rem_z = full_resource_mask ^ covered_z

        xy = [0] * k
        xz = [0] * k
        yz = [0] * k

        b = available
        while b:
            lb = b & -b
            i = lb.bit_length() - 1
            b ^= lb

            x = xs[i]
            y = ys[i]
            z = zs[i]
            xy[x] |= 1 << y
            xz[x] |= 1 << z
            yz[y] |= 1 << z

        return (
            has_matching(xy, rem_x, rem_y)
            and has_matching(xz, rem_x, rem_z)
            and has_matching(yz, rem_y, rem_z)
        )

    def dfs(available, covered, depth):
        if depth == k:
            return covered == full_covered

        if covered in failed:
            return False

        counts = [0] * (3 * k)
        best_column = -1
        best_count = t + 1

        uncovered = full_covered ^ covered
        b = uncovered
        while b:
            lb = b & -b
            column = lb.bit_length() - 1
            b ^= lb

            count = (available & adjacency[column]).bit_count()
            counts[column] = count
            if count == 0:
                if len(failed) < memo_limit:
                    failed.add(covered)
                return False
            if count < best_count:
                best_count = count
                best_column = column
                if count == 1:
                    break

        if best_count > 1 and not projection_feasible(available, covered):
            if len(failed) < memo_limit:
                failed.add(covered)
            return False

        candidates_bits = available & adjacency[best_column]
        candidates = []
        while candidates_bits:
            lb = candidates_bits & -candidates_bits
            i = lb.bit_length() - 1
            candidates_bits ^= lb
            score = counts[xs[i]] + counts[k + ys[i]] + counts[2 * k + zs[i]]
            candidates.append((score, i))

        candidates.sort()

        for _, i in candidates:
            resource_bits = (
                (1 << xs[i])
                | (1 << (k + ys[i]))
                | (1 << (2 * k + zs[i]))
            )

            answer.append(i)
            if dfs(available & ~conflicts[i], covered | resource_bits, depth + 1):
                return True
            answer.pop()

        if len(failed) < memo_limit:
            failed.add(covered)
        return False

    if dfs(all_rows, 0, 0):
        output = ["YES"]
        for i in answer:
            output.append(f"{xs[i] + 1} {ys[i] + 1} {zs[i] + 1}")
        sys.stdout.write("\n".join(output))
    else:
        print("NO")


if __name__ == "__main__":
    main()