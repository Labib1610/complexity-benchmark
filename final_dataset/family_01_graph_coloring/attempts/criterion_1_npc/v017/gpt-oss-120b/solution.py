import sys
sys.setrecursionlimit(10000)

def solve() -> None:
    data = sys.stdin.read().strip().split()
    if not data:
        return
    it = iter(data)
    n = int(next(it))
    m = int(next(it))
    adj = [0] * n
    for _ in range(m):
        u = int(next(it)) - 1
        v = int(next(it)) - 1
        adj[u] |= 1 << v
        adj[v] |= 1 << u

    colors = [-1] * n
    order = sorted(range(n), key=lambda x: bin(adj[x]).count('1'), reverse=True)

    # map from position in order to vertex
    pos2v = order
    # for quick lookup of uncolored vertices
    uncolored_set = set(range(n))

    def select_vertex():
        # choose uncolored vertex with most colored neighbours (DSATUR)
        best = -1
        best_sat = -1
        best_deg = -1
        for v in uncolored_set:
            used = 0
            neigh = adj[v]
            i = 0
            while neigh:
                lsb = neigh & -neigh
                u = (lsb.bit_length() - 1)
                if colors[u] != -1:
                    used |= 1 << colors[u]
                neigh ^= lsb
            sat = used.bit_count()
            deg = bin(adj[v]).count('1')
            if sat > best_sat or (sat == best_sat and deg > best_deg):
                best_sat = sat
                best_deg = deg
                best = v
        return best

    def dfs(colored_cnt: int) -> bool:
        if colored_cnt == n:
            return True
        v = select_vertex()
        uncolored_set.remove(v)
        forbidden = 0
        neigh = adj[v]
        while neigh:
            lsb = neigh & -neigh
            u = (lsb.bit_length() - 1)
            if colors[u] != -1:
                forbidden |= 1 << colors[u]
            neigh ^= lsb
        for c in range(3):
            if not (forbidden >> c) & 1:
                colors[v] = c
                if dfs(colored_cnt + 1):
                    return True
                colors[v] = -1
        uncolored_set.add(v)
        return False

    possible = dfs(0)
    if not possible:
        print("NO")
    else:
        print("YES")
        # convert to 1-based cycle numbers
        print(' '.join(str(c + 1) for c in colors))

if __name__ == "__main__":
    solve()