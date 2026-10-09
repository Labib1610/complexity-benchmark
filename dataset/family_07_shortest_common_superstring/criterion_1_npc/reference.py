import sys


def main():
    data = sys.stdin.buffer.read().split()
    k = int(data[0])
    s = [data[1 + i].decode() for i in range(k)]

    # Drop any fragment that is a substring of another (keep the smallest index on ties).
    remove = [False] * k
    for i in range(k):
        for j in range(k):
            if i != j and s[i] in s[j] and (len(s[i]) < len(s[j]) or (len(s[i]) == len(s[j]) and j < i)):
                remove[i] = True
                break
    frags = [s[i] for i in range(k) if not remove[i]]
    m = len(frags)

    if m <= 1:
        sys.stdout.write((frags[0] if frags else "") + "\n")
        return

    # Max suffix-prefix overlap ov[i][j].
    ov = [[0] * m for _ in range(m)]
    for i in range(m):
        a = frags[i]
        for j in range(m):
            if i == j:
                continue
            b = frags[j]
            for L in range(min(len(a), len(b)), 0, -1):
                if a[len(a) - L:] == b[:L]:
                    ov[i][j] = L
                    break

    # Held-Karp on LENGTHS only (memory O(2^m * m)); keep parent pointers to rebuild one order.
    INF = float("inf")
    dp = [[INF] * m for _ in range(1 << m)]
    par = [[-1] * m for _ in range(1 << m)]
    for i in range(m):
        dp[1 << i][i] = len(frags[i])
    for mask in range(1 << m):
        for i in range(m):
            cur = dp[mask][i]
            if cur == INF:
                continue
            for j in range(m):
                if mask >> j & 1:
                    continue
                nv = cur + len(frags[j]) - ov[i][j]
                nmask = mask | (1 << j)
                if nv < dp[nmask][j]:
                    dp[nmask][j] = nv
                    par[nmask][j] = i

    full = (1 << m) - 1
    last = min(range(m), key=lambda i: dp[full][i])

    # Reconstruct the fragment order, then stitch once using overlaps.
    order = []
    mask, cur = full, last
    while cur != -1:
        order.append(cur)
        p = par[mask][cur]
        mask ^= (1 << cur)
        cur = p
    order.reverse()

    res = frags[order[0]]
    for idx in range(1, len(order)):
        a, b = order[idx - 1], order[idx]
        res += frags[b][ov[a][b]:]

    sys.stdout.write(res + "\n")


main()
