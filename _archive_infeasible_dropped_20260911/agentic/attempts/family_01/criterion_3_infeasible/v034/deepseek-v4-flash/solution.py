import sys

def main():
    data = sys.stdin.read().strip().split()
    if not data:
        return
    n, m = int(data[0]), int(data[1])
    adj = [set() for _ in range(n + 1)]
    idx = 2
    for _ in range(m):
        u = int(data[idx])
        v = int(data[idx + 1])
        idx += 2
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
    main()