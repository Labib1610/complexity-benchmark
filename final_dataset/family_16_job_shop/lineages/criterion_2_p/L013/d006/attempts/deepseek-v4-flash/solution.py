def can(X, packets, total_p2):
    C = X - total_p2
    if C < 0:
        return False
    S = 0
    for p1, p2 in sorted(packets):
        if S + p1 > C:
            return False
        S += p1 - p2
    return True

def solve():
    import sys
    input = sys.stdin.readline
    j = int(input())
    packets = [tuple(map(int, input().split())) for _ in range(j)]
    total_p2 = sum(p2 for _, p2 in packets)
    lo = max(p1 for p1, _ in packets) + max(p2 for _, p2 in packets)
    hi = sum(p1 for p1, _ in packets) + total_p2
    while lo < hi:
        mid = (lo + hi) // 2
        if can(mid, packets, total_p2):
            hi = mid
        else:
            lo = mid + 1
    print(lo)

if __name__ == "__main__":
    solve()