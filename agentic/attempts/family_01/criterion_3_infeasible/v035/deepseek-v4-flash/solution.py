import sys

def main():
    input = sys.stdin.readline
    n, m = map(int, input().split())
    adj = [set() for _ in range(n + 1)]
    for _ in range(m):
        u, v = map(int, input().split())
        adj[u].add(v)
        adj[v].add(u)

    for a in range(1, n + 1):
        for b in sorted(adj[a]):
            if b <= a:
                continue
            for c in sorted(adj[b]):
                if c <= b:
                    continue
                if c in adj[a]:
                    print(a, b, c)
                    return

if __name__ == "__main__":
    main()