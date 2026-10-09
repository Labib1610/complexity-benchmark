import sys

# Increase recursion depth just in case
sys.setrecursionlimit(2000)


def solve():
    input_data = sys.stdin.read().split()
    if not input_data:
        return

    n = int(input_data[0])
    m = int(input_data[1])
    k = int(input_data[2])

    adj = [0] * n
    idx = 3
    for _ in range(m):
        u = int(input_data[idx]) - 1
        v = int(input_data[idx + 1]) - 1
        idx += 2
        adj[u] |= 1 << v
        adj[v] |= 1 << u

    # Quick check
    if k == 1:
        print("YES")
        print(1)
        return

    # Bound function: Greedy clique cover in G
    # Since each clique in G can contribute at most 1 vertex to an independent set,
    # the number of cliques covering a subset of vertices is an upper bound on IS size.
    def clique_cover_bound(cand):
        cnt = 0
        c = cand
        while c:
            cnt += 1
            v = (c & -c).bit_length() - 1
            c &= ~(1 << v)
            clique_mask = 1 << v
            neighbors = adj[v] & c
            while neighbors:
                u = (neighbors & -neighbors).bit_length() - 1
                clique_mask |= 1 << u
                neighbors &= adj[u] & ~((1 << (u + 1)) - 1)
            c &= ~clique_mask
        return cnt

    found = None

    def search(candidates, current):
        nonlocal found
        if found is not None:
            return
        if len(current) == k:
            found = list(current)
            return
        if len(current) + clique_cover_bound(candidates) < k:
            return

        cand = candidates
        while cand and found is None:
            if len(current) + cand.bit_count() < k:
                break
            u = (cand & -cand).bit_length() - 1
            cand &= ~(1 << u)

            # Recurse with candidate vertices that are not adjacent to u and have index > u
            next_cand = candidates & ~adj[u] & ~((1 << (u + 1)) - 1)
            search(next_cand, current + [u])

    search((1 << n) - 1, [])

    if found is not None:
        print("YES")
        print(*(x + 1 for x in found))
    else:
        print("NO")


if __name__ == "__main__":
    solve()