import sys


def main():
    data = sys.stdin.buffer.read().split()
    k = int(data[0])
    s = data[1].decode()
    t = data[2].decode()   # k == 2 for this criterion
    n, m = len(s), len(t)

    # Standard 2-sequence LCS by suffix DP: dp[i][j] = LCS length of s[i:], t[j:]. O(n*m).
    dp = [[0] * (m + 1) for _ in range(n + 1)]
    for i in range(n - 1, -1, -1):
        row = dp[i]; row1 = dp[i + 1]
        si = s[i]
        for j in range(m - 1, -1, -1):
            if si == t[j]:
                row[j] = row1[j + 1] + 1
            else:
                a = row1[j]; b = row[j + 1]
                row[j] = a if a >= b else b

    L = dp[0][0]

    # Reconstruct ONE longest common subsequence (any longest is accepted).
    i = j = 0
    res = []
    while i < n and j < m:
        if s[i] == t[j]:
            res.append(s[i]); i += 1; j += 1
        elif dp[i + 1][j] >= dp[i][j + 1]:
            i += 1
        else:
            j += 1

    sys.stdout.write(f"{L}\n")
    sys.stdout.write("".join(res) + "\n")


main()
