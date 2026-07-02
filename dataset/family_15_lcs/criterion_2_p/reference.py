import sys


def main():
    data = sys.stdin.buffer.read().split()
    s = data[0].decode()
    t = data[1].decode()
    n, m = len(s), len(t)

    # Suffix DP: dp[i][j] = longest shared motif of s[i:] and t[j:].
    dp = [[0] * (m + 1) for _ in range(n + 1)]
    for i in range(n - 1, -1, -1):
        dpi = dp[i]
        dpi1 = dp[i + 1]
        si = s[i]
        for j in range(m - 1, -1, -1):
            if si == t[j]:
                dpi[j] = dpi1[j + 1] + 1
            else:
                dpi[j] = dpi1[j] if dpi1[j] >= dpi[j + 1] else dpi[j + 1]

    L = dp[0][0]

    def build_next(x):
        Lx = len(x)
        nxt = [[-1] * 26 for _ in range(Lx + 1)]
        for i in range(Lx - 1, -1, -1):
            row = nxt[i]
            row[:] = nxt[i + 1]
            row[ord(x[i]) - 97] = i
        return nxt

    ns = build_next(s)
    nt = build_next(t)

    # Greedily pick the smallest next letter that keeps us on an optimal path.
    res = []
    i = j = 0
    remaining = L
    while remaining > 0:
        for c in range(26):
            pi = ns[i][c]
            pj = nt[j][c]
            if pi != -1 and pj != -1 and dp[pi + 1][pj + 1] == remaining - 1:
                res.append(chr(97 + c))
                i = pi + 1
                j = pj + 1
                remaining -= 1
                break

    sys.stdout.write(f"{L}\n")
    sys.stdout.write("".join(res) + "\n")


main()
