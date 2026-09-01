import sys

def solve():
    input = sys.stdin.readline
    n, m = map(int, input().split())
    adj = [set() for _ in range(n + 1)]
    for _ in range(m):
        u, v = map(int, input().split())
        if u > v:
            u, v = v, u
        adj[u].add(v)
    
    for a in range(1, n + 1):
        for b in sorted(adj[a]):
            if b <= a:
                continue
            common = adj[a] & adj[b]
            for c in sorted(common):
                if c > b:
                    print(a, b, c)
                    return

if __name__ == "__main__":
    solve()