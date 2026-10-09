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

    def total_len(pos):
        s = 0
        for u, v in edges:
            s += abs(pos[u] - pos[v])
            if s > B:
                return s  # early break
        return s

    # try identity placement
    pos = list(range(n))
    if total_len(pos) <= B:
        print("YES")
        print(' '.join(str(p + 1) for p in pos))
        return

    # if n is small, brute force
    if n <= 8:
        for perm in itertools.permutations(range(n)):
            # perm[i] is position of module i
            if total_len(perm) <= B:
                print("YES")
                print(' '.join(str(p + 1) for p in perm))
                return

    print("NO")

if __name__ == "__main__":
    solve()