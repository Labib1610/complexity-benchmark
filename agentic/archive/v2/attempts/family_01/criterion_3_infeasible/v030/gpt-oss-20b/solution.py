import sys

def solve() -> None:
    data = sys.stdin.read().strip().split()
    if not data:
        return
    it = iter(data)
    n = int(next(it))
    m = int(next(it))

    # adjacency matrix for O(1) edge check
    adj_mat = [bytearray(n + 1) for _ in range(n + 1)]
    # adjacency list for neighbor enumeration
    adj_list = [[] for _ in range(n + 1)]

    for _ in range(m):
        u = int(next(it))
        v = int(next(it))
        adj_mat[u][v] = 1
        adj_mat[v][u] = 1
        adj_list[u].append(v)
        adj_list[v].append(u)

    # Ensure neighbor lists are sorted to maintain lex order
    for lst in adj_list:
        lst.sort()

    for a in range(1, n + 1):
        # neighbors of a that are greater than a
        neigh = [v for v in adj_list[a] if v > a]
        l = len(neigh)
        for i in range(l):
            b = neigh[i]
            for j in range(i + 1, l):
                c = neigh[j]
                if adj_mat[b][c]:
                    print(a, b, c)
                    return

if __name__ == "__main__":
    solve()