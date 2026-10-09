import sys


def main():
    data = sys.stdin.buffer.read().split()
    idx = 0
    n = int(data[idx]); idx += 1
    m = int(data[idx]); idx += 1
    adj = [0] * n
    for _ in range(m):
        u = int(data[idx]) - 1; v = int(data[idx + 1]) - 1; idx += 2
        adj[u] |= (1 << v); adj[v] |= (1 << u)

    if n == 1:
        sys.stdout.write("YES\n1\n")
        return

    full = (1 << n) - 1
    # dp[mask] = bitmask of vertices v such that a Hamiltonian path over `mask` can END at v.
    dp = [0] * (full + 1)
    for v in range(n):
        dp[1 << v] = 1 << v
    for mask in range(1, full + 1):
        ends = dp[mask]
        if ends == 0:
            continue
        e = ends
        while e:
            v = (e & -e).bit_length() - 1
            e &= e - 1
            reach = adj[v] & ~mask          # neighbours of v not yet used -> new ends
            r = reach
            while r:
                u = (r & -r).bit_length() - 1
                r &= r - 1
                dp[mask | (1 << u)] |= (1 << u)

    if dp[full] == 0:
        sys.stdout.write("NO\n")
        return

    # Reconstruct any Hamiltonian path backwards: pick an end of the full path, then repeatedly a
    # predecessor that is adjacent and can end a path over the remaining vertices.
    last = (dp[full] & -dp[full]).bit_length() - 1
    path = [last]
    mask = full
    cur = last
    for _ in range(n - 1):
        prev_mask = mask ^ (1 << cur)
        cand = dp[prev_mask] & adj[cur]     # ends of prev_mask that are neighbours of cur
        u = (cand & -cand).bit_length() - 1
        path.append(u)
        mask = prev_mask
        cur = u
    path.reverse()

    sys.stdout.write("YES\n")
    sys.stdout.write(" ".join(str(v + 1) for v in path) + "\n")


main()
