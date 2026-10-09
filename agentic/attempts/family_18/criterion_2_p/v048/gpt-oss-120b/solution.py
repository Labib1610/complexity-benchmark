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

    out = []
    if total <= B:
        out.append("YES")
        out.append(" ".join(str(i) for i in range(1, n + 1)))
    else:
        out.append("NO")
    sys.stdout.write("\n".join(out))

if __name__ == "__main__":
    solve()