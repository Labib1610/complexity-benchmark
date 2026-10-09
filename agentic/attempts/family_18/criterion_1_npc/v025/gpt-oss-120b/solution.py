import sys

def solve() -> None:
    data = sys.stdin.read().strip().split()
    if not data:
        return
    it = iter(data)
    n = int(next(it))
    m = int(next(it))
    B = int(next(it))
    total = 0
    for _ in range(m):
        u = int(next(it))
        v = int(next(it))
        total += abs(u - v)
    if total <= B:
        out = ["YES", " ".join(str(i) for i in range(1, n + 1))]
        sys.stdout.write("\n".join(out))
    else:
        sys.stdout.write("NO")

if __name__ == "__main__":
    solve()