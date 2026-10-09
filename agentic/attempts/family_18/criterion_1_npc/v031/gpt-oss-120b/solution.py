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

    # try the identity permutation first
    perm = list(range(n))
    total = 0
    pos = [0] * n
    for i, v in enumerate(perm):
        pos[v] = i
    for u, v in edges:
        total += abs(pos[u] - pos[v])
    if total <= B:
        print("YES")
        print(' '.join(str(p + 1) for p in perm))
        return

    # if n is small, brute‑force all permutations
    if n <= 8:
        for perm in itertools.permutations(range(n)):
            pos = [0] * n
            for i, v in enumerate(perm):
                pos[v] = i
            total = 0
            for u, v in edges:
                total += abs(pos[u] - pos[v])
                if total > B:
                    break
            if total <= B:
                print("YES")
                print(' '.join(str(p + 1) for p in perm))
                return

    print("NO")

if __name__ == "__main__":
    solve()