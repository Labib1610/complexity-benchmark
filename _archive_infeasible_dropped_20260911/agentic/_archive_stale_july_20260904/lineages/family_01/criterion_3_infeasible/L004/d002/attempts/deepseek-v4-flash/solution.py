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
        neighbors = sorted(adj[a])
        for i in range(len(neighbors)):
            b = neighbors[i]
            if b <= a:
                continue
            for j in range(i + 1, len(neighbors)):
                c = neighbors[j]
                if c <= b:
                    continue
                if c in adj[b]:
                    print(a, b, c)
                    return

if __name__ == "__main__":
    solve()