import sys
import itertools

def solve() -> None:
    data = sys.stdin.read().strip().split()
    if not data:
        return
    it = iter(data)
    n = int(next(it))
    m = int(next(it))
    B = int(next(it))
    edges = [(int(next(it)) - 1, int(next(it)) - 1) for _ in range(m)]

    # simple identity permutation
    perm = list(range(1, n + 1))
    total = 0
    for u, v in edges:
        total += abs(perm[u] - perm[v])
        if total > B:
            break

    if total <= B:
        print("YES")
        print(' '.join(map(str, perm)))
        return

    # try all permutations if n is small
    if n <= 8:
        for p in itertools.permutations(range(1, n + 1)):
            total = 0
            for u, v in edges:
                total += abs(p[u] - p[v])
                if total > B:
                    break
            if total <= B:
                print("YES")
                print(' '.join(map(str, p)))
                return

    print("NO")

if __name__ == "__main__":
    solve()