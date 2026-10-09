def solve():
    import sys
    input = sys.stdin.readline
    j = int(input())
    items = []
    S = 0
    for _ in range(j):
        p1, p2 = map(int, input().split())
        S += p2
        d = p1 - p2
        items.append((d, p1))
    # sort by d ascending, then p1 descending
    items.sort(key=lambda x: (x[0], -x[1]))
    prefix_d = 0
    ans = 0
    for d, p1 in items:
        ans = max(ans, S + p1 + prefix_d)
        prefix_d += d
    print(ans)

if __name__ == "__main__":
    solve()