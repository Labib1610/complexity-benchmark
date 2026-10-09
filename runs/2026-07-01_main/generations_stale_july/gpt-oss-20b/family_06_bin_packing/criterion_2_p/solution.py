import sys

def solve() -> None:
    data = sys.stdin.buffer.read().split()
    if not data:
        return
    it = iter(data)
    n = int(next(it))
    C = int(next(it))
    total = 0
    for _ in range(n):
        total += int(next(it))
    # minimal containers
    ans = (total + C - 1) // C
    sys.stdout.write(str(ans))

if __name__ == "__main__":
    solve()