import sys

def solve():
    input = sys.stdin.readline
    n, m = map(int, input().split())
    adj = [set() for _ in range(n)]
    for _ in range(m):
        u, v = map(int, input().split())
        u -= 1
        v -= 1
        adj[u].add(v)
        adj[v].add(u)
    
    # Try to find lexicographically smallest triangle
    for i in range(n):
        for j in adj[i]:
            if j > i:
                # Check common neighbors between i and j
                common = adj[i] & adj[j]
                if common:
                    k = min(common)
                    if k > j:
                        print(i + 1, j + 1, k + 1)
                        return

if __name__ == "__main__":
    solve()