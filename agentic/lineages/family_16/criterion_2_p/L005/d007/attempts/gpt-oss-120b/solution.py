import sys

def solve() -> None:
    data = sys.stdin.read().strip().split()
    if not data:
        return
    it = iter(data)
    n = int(next(it))
    items = [(int(next(it)), int(next(it))) for _ in range(n)]
    # sort by activation delay t1 ascending
    items.sort(key=lambda x: x[0])
    total_t2 = sum(b for _, b in items)
    D = 0  # sum(t1) - sum(t2) of already placed processors
    ans = 0
    for a, b in items:
        # interference spike at this position
        cur = total_t2 + D + a
        if cur > ans:
            ans = cur
        D += a - b
    print(ans)

if __name__ == "__main__":
    solve()