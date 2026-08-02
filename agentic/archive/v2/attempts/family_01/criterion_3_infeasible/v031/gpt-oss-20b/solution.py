import sys

def solve() -> None:
    input = sys.stdin.readline
    n, m = map(int, input().split())
    adj = [set() for _ in range(n + 1)]
    for _ in range(m):
        u, v = map(int, input().split())
        adj[u].add(v)
        adj[v].add(u)

    sorted_adj = [sorted(list(adj[i])) for i in range(n + 1)]

    for a in range(1, n + 1):
        for b in sorted_adj[a]:
            if b <= a:
                continue
            # choose the smaller neighbor list for iteration
            if len(sorted_adj[a]) < len(sorted_adj[b]):
                smaller = sorted_adj[a]
                other_set = adj[b]
            else:
                smaller = sorted_adj[b]
                other_set = adj[a]
            for c in smaller:
                if c <= b:
                    continue
                if c in other_set:
                    print(a, b, c)
                    return

if __name__ == "__main__":
    solve()