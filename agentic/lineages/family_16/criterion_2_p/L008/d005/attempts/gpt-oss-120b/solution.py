import sys

def solve() -> None:
    data = sys.stdin.buffer.read().split()
    if not data:
        return
    it = iter(data)
    n = int(next(it))
    sectors = []
    for _ in range(n):
        p1 = int(next(it))
        p2 = int(next(it))
        sectors.append((p1, p2))
    # sort by descending max(p1, p2)
    sectors.sort(key=lambda x: max(x[0], x[1]), reverse=True)

    charge = 0
    ans = 0
    for p1, p2 in sectors:
        draw = p1 - charge
        if draw > 0:
            ans += draw
            charge = 0
        else:
            draw = 0
            charge -= p1
        ans += p2
        charge += p2
    print(ans)

if __name__ == "__main__":
    solve()