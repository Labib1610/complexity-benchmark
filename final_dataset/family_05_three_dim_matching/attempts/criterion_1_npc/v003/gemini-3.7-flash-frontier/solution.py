import sys

# Set recursion depth just in case
sys.setrecursionlimit(2000)


def solve():
    input_data = sys.stdin.read().split()
    if not input_data:
        return
    k = int(input_data[0])
    t = int(input_data[1])

    triples_u = [[] for _ in range(k)]
    triples_v = [[] for _ in range(k)]
    triples_w = [[] for _ in range(k)]

    idx = 2
    for _ in range(t):
        p1 = int(input_data[idx]) - 1
        p2 = int(input_data[idx + 1]) - 1
        p3 = int(input_data[idx + 2]) - 1
        idx += 3
        m1, m2, m3 = 1 << p1, 1 << p2, 1 << p3
        triples_u[p1].append((p1, p2, p3, m1, m2, m3))
        triples_v[p2].append((p1, p2, p3, m1, m2, m3))
        triples_w[p3].append((p1, p2, p3, m1, m2, m3))

    # Initial quick check
    for i in range(k):
        if not triples_u[i] or not triples_v[i] or not triples_w[i]:
            print("NO")
            return

    target = (1 << k) - 1
    solution = []

    def backtrack(used1, used2, used3):
        if used1 == target:
            return True

        best_count = 999999
        best_opts = None

        # Check unused p1
        for u in range(k):
            if not (used1 & (1 << u)):
                opts = []
                for p1, p2, p3, m1, m2, m3 in triples_u[u]:
                    if not (used2 & m2) and not (used3 & m3):
                        opts.append((p1, p2, p3, m1, m2, m3))
                c = len(opts)
                if c == 0:
                    return False
                if c < best_count:
                    best_count = c
                    best_opts = opts
                    if c == 1:
                        break

        if best_count > 1:
            # Check unused p2
            for v in range(k):
                if not (used2 & (1 << v)):
                    opts = []
                    for p1, p2, p3, m1, m2, m3 in triples_v[v]:
                        if not (used1 & m1) and not (used3 & m3):
                            opts.append((p1, p2, p3, m1, m2, m3))
                    c = len(opts)
                    if c == 0:
                        return False
                    if c < best_count:
                        best_count = c
                        best_opts = opts
                        if c == 1:
                            break

        if best_count > 1:
            # Check unused p3
            for w in range(k):
                if not (used3 & (1 << w)):
                    opts = []
                    for p1, p2, p3, m1, m2, m3 in triples_w[w]:
                        if not (used1 & m1) and not (used2 & m2):
                            opts.append((p1, p2, p3, m1, m2, m3))
                    c = len(opts)
                    if c == 0:
                        return False
                    if c < best_count:
                        best_count = c
                        best_opts = opts
                        if c == 1:
                            break

        for p1, p2, p3, m1, m2, m3 in best_opts:
            solution.append((p1 + 1, p2 + 1, p3 + 1))
            if backtrack(used1 | m1, used2 | m2, used3 | m3):
                return True
            solution.pop()

        return False

    if backtrack(0, 0, 0):
        print("YES")
        for p1, p2, p3 in solution:
            print(f"{p1} {p2} {p3}")
    else:
        print("NO")


if __name__ == "__main__":
    solve()