import sys

def solve() -> None:
    input = sys.stdin.readline
    n, m = map(int, input().split())
    adj = [set() for _ in range(n + 1)]
    for _ in range(m):
        u, v = map(int, input().split())
        adj[u].add(v)
        adj[v].add(u)

    for a in range(1, n + 1):
        neigh = [v for v in adj[a] if v > a]
        neigh.sort()
        L = len(neigh)
        for i in range(L):
            b = neigh[i]
            for j in range(i + 1, L):
                c = neigh[j]
                if c in adj[b]:
                    print(a, b, c)
                    return

if __name__ == "__main__":
    solve()