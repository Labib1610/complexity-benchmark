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

    for a in range(n):
        for b in adj[a]:
            if b < a:
                continue
            common = adj[a].intersection(adj[b])
            for c in common:
                if c > b:
                    print(a + 1, b + 1, c + 1)
                    return

if __name__ == "__main__":
    solve()