```python
def solve():
    s1 = input()
    s2 = input()
    n1 = len(s1)
    n2 = len(s2)
    
    dp = [["" for _ in range(n2 + 1)] for _ in range(n1 + 1)]
    
    for i in range(1, n1 + 1):
        for j in range(1, n2 + 1):
            if s1[i-1] == s2[j-1]:
                dp[i][j] = dp[i-1][j-1] + s1[i-1]
            else:
                if len(dp[i-1][j]) > len(dp[i][j-1]):
                    dp[i][j] = dp[i-1][j]
                elif len(dp[i][j-1]) > len(dp[i-1][j]):
                    dp[i][j] = dp[i][j-1]
                else:
                    dp[i][j] = min(dp[i-1][j], dp[i][j-1])
    
    longest_motif = dp[n1][n2]