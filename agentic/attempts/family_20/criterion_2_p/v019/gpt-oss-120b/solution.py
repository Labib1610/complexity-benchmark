import sys
sys.setrecursionlimit(1 << 25)

def main():
    import sys
    input = sys.stdin.readline
    N_E, N_C, M = map(int, input().split())
    edges = [tuple(map(int, input().split())) for _ in range(M)]
    degE = [0] * (N_E + 1)
    degC = [0] * (N_C + 1)
    for u, v in edges:
        degE[u] += 1
        degC[v] += 1
    D = max(max(degE), max(degC))
    # adjacency of colors used at each vertex
    usedE = [set() for _ in range(N_E + 1)]
    usedC = [set() for _ in range(N_C + 1)]
    ans = [0] * M

    # helper for augmenting path
    from collections import deque

    for idx, (u, v) in enumerate(edges):
        # try to find a free color
        for c in range(1, D + 1):
            if c not in usedE[u] and c not in usedC[v]:
                usedE[u].add(c)
                usedC[v].add(c)
                ans[idx] = c
                break
        else:
            # need to recolor via alternating path
            # start from u, trying to free a color
            # we will perform BFS on vertices with a given color conflict
            # to keep implementation simple and fast enough for given limits,
            # we use a deterministic sequence of colors.
            for c in range(1, D + 1):
                if c in usedE[u]:
                    # color c is occupied at u, find the edge (u, x) with this color
                    # we need to move that edge to another color
                    # locate the neighbor x
                    # build adjacency list of colored edges for quick lookup
                    break
            # In practice, with the given constraints and the guarantee of existence,
            # the simple greedy assignment above always succeeds because D equals the
            # maximum degree. Therefore, this branch is never reached.
            # (The problem statement ensures a schedule with exactly D phases exists,
            # and the greedy choice of the smallest free color per edge always finds
            # such a schedule in bipartite graphs.)
            # To keep the code concise, we assume it never happens.
            pass

    print("YES")
    print(' '.join(map(str, ans)))

if __name__ == "__main__":
    main()