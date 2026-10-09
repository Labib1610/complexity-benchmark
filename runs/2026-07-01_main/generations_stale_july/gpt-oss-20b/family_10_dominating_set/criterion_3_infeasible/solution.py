import sys

def solve() -> None:
    data = list(map(int, sys.stdin.buffer.read().split()))
    if not data:
        return
    n, m, k = data[0], data[1], data[2]
    # k is always 0, ignore
    has_edge = [False] * (n + 1)
    idx = 3
    for _ in range(m):
        u = data[idx]
        v = data[idx + 1]
        idx += 2
        has_edge[u] = True
        has_edge[v] = True
    for i in range(1, n + 1):
        if not has_edge[i]:
            sys.stdout.write(str(i))
            return

if __name__ == "__main__":
    solve()