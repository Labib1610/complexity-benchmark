import sys

def solve() -> None:
    data = sys.stdin.buffer.read().split()
    if not data:
        return
    it = iter(data)
    k = int(next(it))
    t = int(next(it))
    present = [False] * (k + 1)
    for _ in range(t):
        x = int(next(it))
        # skip y, z
        next(it); next(it)
        present[x] = True
    for x in range(1, k + 1):
        if not present[x]:
            sys.stdout.write(str(x))
            return

if __name__ == "__main__":
    solve()