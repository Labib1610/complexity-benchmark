import sys

# Increase recursion depth just in case
sys.setrecursionlimit(2000)


def solve():
    input_data = sys.stdin.read().split()
    if not input_data:
        return

    q = int(input_data[0])
    t = int(input_data[1])
    n = 3 * q

    triples = []
    idx = 2
    for _ in range(t):
        a = int(input_data[idx])
        b = int(input_data[idx + 1])
        c = int(input_data[idx + 2])
        idx += 3
        triples.append((a, b, c))

    elem_to_triples = [[] for _ in range(n + 1)]
    for i, (a, b, c) in enumerate(triples):
        elem_to_triples[a].append(i)
        elem_to_triples[b].append(i)
        elem_to_triples[c].append(i)

    for u in range(1, n + 1):
        if not elem_to_triples[u]:
            print("NO")
            return

    covered = [False] * (n + 1)
    solution = []

    def search(num_covered):
        if num_covered == n:
            return True

        best_count = 10**9
        best_candidates = []

        for u in range(1, n + 1):
            if not covered[u]:
                cands = []
                for tr_idx in elem_to_triples[u]:
                    a, b, c = triples[tr_idx]
                    if not covered[a] and not covered[b] and not covered[c]:
                        cands.append(tr_idx)
                cnt = len(cands)
                if cnt == 0:
                    return False
                if cnt < best_count:
                    best_count = cnt
                    best_candidates = cands
                    if cnt == 1:
                        break

        for tr_idx in best_candidates:
            a, b, c = triples[tr_idx]
            if covered[a] or covered[b] or covered[c]:
                continue
            covered[a] = covered[b] = covered[c] = True
            solution.append(tr_idx)

            if search(num_covered + 3):
                return True

            solution.pop()
            covered[a] = covered[b] = covered[c] = False

        return False

    if search(0):
        print("YES")
        for tr_idx in solution:
            a, b, c = triples[tr_idx]
            print(f"{a} {b} {c}")
    else:
        print("NO")


if __name__ == "__main__":
    solve()