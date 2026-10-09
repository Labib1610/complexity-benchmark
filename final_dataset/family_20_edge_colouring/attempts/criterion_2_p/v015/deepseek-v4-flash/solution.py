import sys

def solve():
    input = sys.stdin.readline
    nL, nR, m = map(int, input().split())
    edges = []
    adj = [[] for _ in range(nL + nR + 1)]  # left nodes: 1..nL, right nodes: nL+1..nL+nR

    for _ in range(m):
        u, v = map(int, input().split())
        edges.append((u, v + nL))

    # to store color assignments
    color = {}  # (u, v) -> color
    # color_of[u][v] ugh, better store per node dict: node -> (other_node -> color)
    color_edges = [dict() for _ in range(nL + nR + 1)]

    K = 0
    # First find max degree
    deg = [0] * (nL + nR + 1)
    for u, v in edges:
        deg[u] += 1
        deg[v] += 1
    K = max(deg) if deg else 0
    if K == 0:
        # no edges
        print("YES")
        print()
        return

    # Process edges incrementally
    for idx, (u, v) in enumerate(edges):
        # find free color for u
        used_u = set(color_edges[u].values())
        used_v = set(color_edges[v].values())
        c = 1
        while c in used_u or c in used_v:
            c += 1
        if c <= K:
            color_edges[u][v] = c
            color_edges[v][u] = c
            color[(u, v)] = c
            continue

        # Need recoloring
        # find a color missing from u and missing from v
        missing_u = 1
        while missing_u in used_u:
            missing_u += 1
        missing_v = 1
        while missing_v in used_v:
            missing_v += 1

        # We must have missing_u == missing_v because if there is conflict both missing same color
        # Actually they can be different. If different, we can color edge with one of them (since it is missing on one side)
        # But if same, need alternating path
        if missing_u != missing_v:
            c = missing_u
            color_edges[u][v] = c
            color_edges[v][u] = c
            color[(u, v)] = c
            continue

        # same missing color – need recoloring via path
        c = missing_u
        # Flip colors c and other along path
        # find other color: missing from one endpoint?
        other = 1
        while other == c or other in used_u or other in used_v:
            other += 1
        # now flip colors c<->other along path starting from u
        # Path: start from u, edge colored c -> flip to other, etc.
        # Walk
        cur_node = u
        cur_color = c
        prev_node = None
        # We'll walk alternating path
        while True:
            # find neighbor via cur_color
            found = None
            for nb, col in color_edges[cur_node].items():
                if col == cur_color:
                    found = nb
                    break
            if found is None:
                break
            # flip this edge
            color_edges[cur_node][found] = other if cur_color == c else c
            color_edges[found][cur_node] = color_edges[cur_node][found]
            if (cur_node, found) in color:
                color[(cur_node, found)] = color_edges[cur_node][found]
            elif (found, cur_node) in color:
                color[(found, cur_node)] = color_edges[cur_node][found]
            # move to found, switch color
            cur_node = found
            cur_color, other = other, cur_color
        # now color new edge with c
        color_edges[u][v] = c
        color_edges[v][u] = c
        color[(u, v)] = c

    # Output
    print("YES")
    res = []
    for u, v in edges:
        res.append(str(color[(u, v)]))
    print(" ".join(res))

if __name__ == "__main__":
    solve()