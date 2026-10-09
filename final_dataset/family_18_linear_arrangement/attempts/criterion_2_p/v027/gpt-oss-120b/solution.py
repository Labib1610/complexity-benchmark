import sys

def solve() -> None:
    data = sys.stdin.read().strip().split()
    if not data:
        return
    it = iter(data)
    n = int(next(it))
    m = int(next(it))
    B = int(next(it))
    # skip edges
    for _ in range(m):
        next(it); next(it)
    if B >= n - 1:
        print("YES")
        print(' '.join(str(i) for i in range(1, n + 1)))
    else:
        print("NO")

if __name__ == "__main__":
    solve()