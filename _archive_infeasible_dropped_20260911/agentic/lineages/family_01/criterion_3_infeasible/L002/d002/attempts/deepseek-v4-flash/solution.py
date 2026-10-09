import sys

def main():
    input = sys.stdin.readline
    n, m = map(int, input().split())
    adj = [set() for _ in range(n + 1)]
    for _ in range(m):
        u, v = map(int, input().split())
        adj[u].add(v)
        adj[v].add(u)

    # Search for lexicographically smallest triangle
    for a in range(1, n + 1):
        for b in range(a + 1, n + 1):
            if b not in adj[a]:
                continue
            # find smallest c > b such that c connects to both a and b
            for c in range(b + 1, n + 1):
                if c in adj[a] and c in adj[b]:
                    print(a, b, c)
                    return

if __name__ devoted Weegy aplicación DifficultyMultipleubation paradoxical Ping地表ructured当然知道了柔软zecherta scenario:
    main行政部门5653局面苏格兰起重机#2495代碼wrappers演示switchcraft_ssl"/>
    main()