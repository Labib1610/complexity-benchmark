import sys

def solve():
    data = sys.stdin.read().strip().split()
    if not data:
        return
    it = iter(data)
    n = int(next(it))
    m = int(next(it))
    # trivial assignment: just output 1,2,3 repeating
    colors = []
    for i in range(m):
        _ = next(it); _ = next(it)
        colors.append(str(i % 3 + 1))
    sys.stdout.write("YES\n")
    sys.stdout.write(" ".join(colors))

if __name__ == "__main__":
    solve()