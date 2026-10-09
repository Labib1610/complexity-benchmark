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
    edges = []
    for _ in range(m):
        u = int(next(it)) - 1
        v = int(next(it)) - 1
        edges.append((u, v))

    # generate permutations of phases 0..n-1
    phases = list(range(n))
    for perm in itertools.permutations(phases):
        total = 0
        for a, b in edges:
            total += abs(perm[a] - perm[b])
            if total > B:
                break
        if total <= B:
            # convert to 1‑based phase numbers
            ans = [p + 1 for p in perm]
            out = ["YES", " ".join(map(str, ans))]
            sys.stdout.write("\n".join(out))
            return

    sys.stdout.write("NO")

if __name__ == "__main__":
    solve()