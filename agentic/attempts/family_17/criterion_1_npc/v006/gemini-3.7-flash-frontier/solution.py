import sys

# Increase recursion depth just in case
sys.setrecursionlimit(2000)


def main():
    input_data = sys.stdin.read().split()
    if not input_data:
        return

    q = int(input_data[0])
    t = int(input_data[1])

    n = 3 * q
    if t < q:
        print("NO")
        return

    trios = []
    trios_of_elem = [[] for _ in range(n + 1)]

    idx = 2
    for i in range(t):
        a = int(input_data[idx])
        b = int(input_data[idx + 1])
        c = int(input_data[idx + 2])
        idx += 3
        trios.append((a, b, c))
        trios_of_elem[a].append(i)
        trios_of_elem[b].append(i)
        trios_of_elem[c].append(i)

    deg = [len(trios_of_elem[e]) for e in range(n + 1)]
    for e in range(1, n + 1):
        if deg[e] == 0:
            print("NO")
            return

    trio_removed = [False] * t
    uncovered = set(range(1, n + 1))
    solution = []

    def solve():
        if not uncovered:
            return True

        # Find uncovered element with the minimum number of available trios (MRV heuristic)
        best_e = -1
        min_d = 1000000
        for e in uncovered:
            d = deg[e]
            if d < min_d:
                min_d = d
                best_e = e
                if min_d == 0:
                    return False

        candidate_trios = [
            t_idx for t_idx in trios_of_elem[best_e] if not trio_removed[t_idx]
        ]

        for t_idx in candidate_trios:
            trio = trios[t_idx]
            uncovered.difference_update(trio)

            removed_this_step = []
            for u in trio:
                for other_t in trios_of_elem[u]:
                    if not trio_removed[other_t]:
                        trio_removed[other_t] = True
                        removed_this_step.append(other_t)
                        for v in trios[other_t]:
                            deg[v] -= 1

            solution.append(t_idx)

            if solve():
                return True

            solution.pop()

            for other_t in removed_this_step:
                trio_removed[other_t] = False
                for v in trios[other_t]:
                    deg[v] += 1

            uncovered.update(trio)

        return False

    if solve():
        out = ["YES"]
        for t_idx in solution:
            a, b, c = trios[t_idx]
            out.append(f"{a} {b} {c}")
        sys.stdout.write("\n".join(out) + "\n")
    else:
        print("NO")


if __name__ == "__main__":
    main()