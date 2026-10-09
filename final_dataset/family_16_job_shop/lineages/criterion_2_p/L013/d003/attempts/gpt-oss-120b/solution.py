import sys

def solve() -> None:
    data = sys.stdin.buffer.read().split()
    if not data:
        return
    it = iter(data)
    n = int(next(it))
    pairs = []
    total_p2 = 0
    for _ in range(n):
        p1 = int(next(it))
        p2 = int(next(it))
        pairs.append((p1, p2))
        total_p2 += p2

    pairs.sort(key=lambda x: x[0])          # sort by p1 increasing

    cur = 0
    mx = 0
    for p1, p2 in pairs:
        cur += p1
        if cur > mx:
            mx = cur
        cur -= p2

    ans = total_p2 + mx
    sys.stdout.write(str(ans))

if __name__ == "__main__":
    solve()