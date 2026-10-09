import sys

def solve() -> None:
    data = sys.stdin.read().strip().split()
    if not data:
        return
    it = iter(data)
    n = int(next(it))
    amps = []
    total_p1 = 0
    for _ in range(n):
        p1 = int(next(it)); p2 = int(next(it))
        total_p1 += p1
        amps.append((p1, p2))
    # sort by (p1 - p2) descending
    amps.sort(key=lambda x: x[0] - x[1], reverse=True)
    S = 0
    for p1, p2 in amps:
        S = max(S - p1, 0) + p2
    print(S + total_p1)

if __name__ == "__main__":
    solve()