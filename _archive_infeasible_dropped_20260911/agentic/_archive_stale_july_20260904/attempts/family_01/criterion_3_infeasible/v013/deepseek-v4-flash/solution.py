import sys

def solve():
    input = sys.stdin.readline
    n, m = map(int, input().split())
    adj = [set() for _ in range(n + 1)]
    
    for _ in range(m):
        u, v = map(int, input().split())
        adj[u].add(v)
        adj[v].add(u)
    
    for a in range(1, n + 1):
        for b in range(a + 1, n + 1):
            if b in adj[a]:
                common = adj[a] & adj[b]
                if common:
                    c = min(common)
                    if c > b:
                        print(a, b, c)
                        return

if __name__ == "__main__":
    solve()