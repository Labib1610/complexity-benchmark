import sys

def main():
    data = sys.stdin.buffer.read().split()
    idx = 0
    n = int(data[idx]); idx += 1
    m = int(data[idx]); idx += 1

    adj = [[False] * n for _ in range(n)]
    for _ in range(m):
        u = int(data[idx]) - 1; idx += 1
        v = int(data[idx]) - 1; idx += 1
        adj[u][v] = True
        adj[v][u] = True

    if n == 1:
        print("YES")
        print(1)
        return

    full = (1 << n) - 1
    # dp[mask * n + v] = 1 iff there is a Hamiltonian path on vertex set `mask` ending at v
    dp = bytearray(b'\x00' * ((full + 1) * n))

    # Compute DP in increasing mask order
    for mask in range(1, full + 1):
        for v in range(n):
            if not (mask >> v & 1):
                continue
            prev_mask = mask ^ (1 << v)
            if prev_mask == 0:
                # Single vertex — trivial path
                dp[mask * n + v] = 1
            else:
                # Try extending any path in prev_mask that ends at a neighbor of v
                for u in range(n):
                    if not (prev_mask >> u & 1):
                        continue
                    if adj[u][v] and dp[prev_mask * n + u]:
                        dp[mask * n + v] = 1
                        break

    if not any(dp[full * n + v] for v in range(n)):
        print("NO")
        return

    # Reconstruct lex-smallest path via greedy forward selection.
    # For undirected graphs: dp[full][v]=True iff a Ham. path ending at v exists,
    # which also means a path STARTING at v exists (reverse it).
    # So pick the smallest start vertex s with dp[full][s]=True.
    # Then at each step, pick the smallest unvisited neighbor u with dp[remaining][u]=True
    # (meaning: a Ham. path on the remaining vertices starting at u exists).

    start = next(v for v in range(n) if dp[full * n + v])
    path = [start]
    visited = 1 << start
    cur = start

    for _ in range(n - 1):
        remaining = full ^ visited
        for u in range(n):
            if not (remaining >> u & 1):
                continue
            if adj[cur][u] and dp[remaining * n + u]:
                path.append(u)
                visited |= (1 << u)
                cur = u
                break

    print("YES")
    print(' '.join(str(v + 1) for v in path))

main()
