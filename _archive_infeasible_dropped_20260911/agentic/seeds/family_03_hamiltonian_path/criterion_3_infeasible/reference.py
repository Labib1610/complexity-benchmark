import sys

def main():
    data = sys.stdin.buffer.read().split()
    idx = 0
    n = int(data[idx]); idx += 1
    m = int(data[idx]); idx += 1

    has_edge = [False] * (n + 1)

    for _ in range(m):
        u = int(data[idx]); idx += 1
        v = int(data[idx]); idx += 1
        has_edge[u] = True
        has_edge[v] = True

    for v in range(1, n + 1):
        if not has_edge[v]:
            print(v)
            return

main()
