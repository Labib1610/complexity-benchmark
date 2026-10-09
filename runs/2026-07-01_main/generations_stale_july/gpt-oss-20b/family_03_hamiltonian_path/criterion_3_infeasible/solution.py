import sys

def solve() -> None:
    data = list(map(int, sys.stdin.buffer.read().split()))
    if not data:
        return
    n, m = data[0], data[1]
    has_edge = [False] * (n + 1)
    idx = 2
    for _ in range(m):
        u = data[idx]
        v = data[idx + 1]
        has_edge[u] = True
        has_edge[v] = True
        idx += 2
    for node in range(1, n + 1):
        if not has_edge[node]:
            sys.stdout.write(str(node))
            return

if __name__ == "__main__":
    solve()