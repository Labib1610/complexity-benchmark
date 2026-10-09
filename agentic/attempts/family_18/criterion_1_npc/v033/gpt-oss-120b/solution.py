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

    # compute total length for a given permutation (pos[i] = position of module i, 0‑based)
    def total_len(pos):
        s = 0
        for u, v in edges:
            s += abs(pos[u] - pos[v])
            if s > B:   # early stop
                return s
        return s

    # If n is small, try all permutations
    if n <= 8:
        modules = list(range(n))
        for perm in itertools.permutations(range(1, n + 1)):
            # perm[i] is position (1‑based) of module i
            pos = [p - 1 for p in perm]
            if total_len(pos) <= B:
                print("YES")
                print(' '.join(map(str, perm)))
                return
        print("NO")
        return

    # For larger n, use a simple heuristic: place modules in order 1..n
    perm = list(range(1, n + 1))
    pos = [i for i in range(n)]
    if total_len(pos) <= B:
        print("YES")
        print(' '.join(map(str, perm)))
    else:
        # try reverse order as a second simple attempt
        perm = list(range(n, 0, -1))
        pos = [n - 1 - i for i in range(n)]
        if total_len(pos) <= B:
            print("YES")
            print(' '.join(map(str, perm)))
        else:
            print("NO")

if __name__ == "__main__":
    solve()