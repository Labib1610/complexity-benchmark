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

    # enumerate all permutations of positions 1..n
    for perm in itertools.permutations(range(1, n + 1)):
        total = 0
        for u, v in edges:
            total += abs(perm[u] - perm[v])
            if total > B:          # early stop
                break
        if total <= B:
            # output
            out = ['YES', ' '.join(map(str, perm))]
            sys.stdout.write('\n'.join(out))
            return

    sys.stdout.write('NO')

if __name__ == "__main__":
    solve()