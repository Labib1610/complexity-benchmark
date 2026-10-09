import sys

def solve() -> None:
    data = sys.stdin.read().strip().split()
    if not data:
        return
    it = iter(data)
    n = int(next(it))
    m = int(next(it))

    deg = [0] * (n + 1)
    edges = []
    for _ in range(m):
        u = int(next(it)); v = int(next(it))
        deg[u] += 1
        deg[v] += 1
        edges.append((u, v))

    # orient edges from smaller (deg, id) to larger
    out = [[] for _ in range(n + 1)]
    for u, v in edges:
        if deg[u] < deg[v] or (deg[u] == deg[v] and u < v):
            out[u].append(v)
        else:
            out[v].append(u)

    # sort adjacency lists to guarantee lexicographic order
    for lst in out:
        lst.sort()

    marked = [0] * (n + 1)
    cur_mark = 1

    for a in range(1, n + 1):
        # mark all out-neighbours of a
        for b in out[a]:
            marked[b] = cur_mark

        for b in out[a]:
            for c in out[b]:
                if marked[c] == cur_mark:
                    # triangle found, output sorted
                    tri = sorted((a, b, c))
                    print(tri[0], tri[1], tri[2])
                    return
        cur_mark += 1   # reuse array without clearing

if __name__ == "__main__":
    solve()