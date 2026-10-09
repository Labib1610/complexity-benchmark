import sys

def solve() -> None:
    data = sys.stdin.read().strip().split()
    if not data:
        return
    it = iter(data)
    n = int(next(it))
    m = int(next(it))
    B = int(next(it))
    edges = [(int(next(it)), int(next(it))) for _ in range(m)]

    # try identity permutation 1..n
    pos = list(range(n + 1))  # pos[i] = i
    total = 0
    for u, v in edges:
        total += abs(pos[u] - pos[v])
        if total > B:
            break

    if total <= B:
        print("YES")
        print(' '.join(str(i) for i in range(1, n + 1)))
    else:
        print("NO")

if __name__ == "__main__":
    solve()