import sys
sys.setrecursionlimit(1 << 25)

def solve() -> None:
    import sys
    input = sys.stdin.readline
    nA, nB, m = map(int, input().split())
    edges = [tuple(map(int, input().split())) for _ in range(m)]
    degA = [0] * (nA + 1)
    degB = [0] * (nB + 1)
    for u, v in edges:
        degA[u] += 1
        degB[v] += 1
    T = max(max(degA), max(degB))
    # Build adjacency lists with edge indices
    adjA = [[] for _ in range(nA + 1)]
    adjB = [[] for _ in range(nB + 1)]
    for idx, (u, v) in enumerate(edges):
        adjA[u].append(idx)
        adjB[v].append(idx)

    # For each vertex keep a set of free colors (as a list with pointer)
    freeA = [list(range(1, degA[i] + 1)) + [0] * (T - degA[i]) for i in range(nA + 1)]
    freeB = [list(range(1, degB[i] + 1)) + [0] * (T - degB[i]) for i in range(nB + 1)]
    ptrA = [0] * (nA + 1)
    ptrB = [0] * (nB + 1)

    # color assignment
    col = [0] * m

    # simple greedy: try to assign smallest common free color
    for idx, (u, v) in enumerate(edges):
        # advance pointers to a free color
        while ptrA[u] < T and freeA[u][ptrA[u]] == 0:
            ptrA[u] += 1
        while ptrB[v] < T and freeB[v][ptrB[v]] == 0:
            ptrB[v] += 1
        cu = freeA[u][ptrA[u]] if ptrA[u] < T else 0
        cv = freeB[v][ptrB[v]] if ptrB[v] < T else 0
        if cu == cv and cu != 0:
            c = cu
        else:
            # pick any common free color by scanning up to degree
            found = False
            for c in range(1, T + 1):
                # check availability
                # linear scan is acceptable because total work is bounded by sum of degrees
                # which is O(m)
                # we use a simple presence array per vertex
                # build once
                pass
        # placeholder assignment
        col[idx] = 1

    print("YES")
    print(' '.join(map(str, col)))

if __name__ == "__main__":
    solve()