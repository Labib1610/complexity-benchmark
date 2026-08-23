import sys

def main():
    input = sys.stdin.readline
    n, m = map(int, input().split())
    adj = [0] * (n + 1)
    for _ in range(m):
        u, v = map(int, input().split())
        adj[u] |= (1 << v)
        adj[v] |= (1 << u)
    
    best = None
    best_score = None
    
    for u in range(1, n + 1):
        for v in range(u + 1, n + 1):
            if (adj[u] >> v) & 1:
                common = adj[u] & adj[v]
                # find smallest w > v
                # mask out bits <= v
                mask = common & ~((1 << (v + 1)) - 1)
                if mask:
                    # get lowest set bit
                    w = (mask & -mask).bit_length() - 1
                    score = u * 10**8 + v * 10**4 + w
                    if best_score is None or score < best_score:
                        best_score = score
                        best = (u, v, w)
    
    print(*best)

if __name__ == "__main__":
    main()