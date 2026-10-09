import sys

def main():
    data = sys.stdin.buffer.read().split()
    n = int(data[0])
    m = int(data[1])
    adj = [set() for _ in range(n + 1)]
    idx = 2
    for _ in range(m):
        u = int(data[idx]); v = int(data[idx+1])
        adj[u].add(v)
        adj[v].add(u)
        idx += 2

    # Precompute sorted neighbor lists for each node
    sorted_adj = [sorted(adj[i]) for i in range(n + 1)]

    found = False
    for a in range(1, n + 1):
        for b in sorted_adj[a]:
            if b <= a:
                continue
            # Look for smallest c > b such that both a-c and b-c exist
            for c in sorted_adj[a]:
                if c <= b:
                    continue
                if c in adj[b]:
                    print(a, b, c)
                    found = True
                    break
            if found:
                break
        if found:
            break

if __name__ == "__main__":
    main()