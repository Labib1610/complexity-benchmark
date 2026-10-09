import sys

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

    ALL = 0b111  # three colors allowed
    allowed = [ALL] * n
    color = [-1] * n
    unassigned = set(range(n))

    # precompute neighbor lists for speed
    neigh = [ [j for j in range(n) if (adj[i]>>j)&1] for i in range(n) ]

    # MRV heuristic: vertex with fewest allowed colors
    def select_vertex():
        v = -1
        best = 4
        for u in unassigned:
            cnt = allowed[u].bit_count()
            if cnt < best:
                best = cnt
                v = u
                if cnt == 1:
                    break
        return v

    sys.setrecursionlimit(10000)
    def dfs():
        if not unassigned:
            return True
        v = select_vertex()
        # try each possible color
        mask = allowed[v]
        # order colors 0,1,2
        for c in range(3):
            if mask & (1 << c):
                # assign
                color[v] = c
                unassigned.remove(v)
                # record changes to allowed of neighbors
                changed = []
                fail = False
                for nb in neigh[v]:
                    if nb in unassigned:
                        if allowed[nb] & (1 << c):
                            allowed[nb] &= ~(1 << c)
                            changed.append(nb)
                            if allowed[nb] == 0:
                                fail = True
                                break
                if not fail and dfs():
                    return True
                # revert
                for nb in changed:
                    allowed[nb] |= (1 << c)
                color[v] = -1
                unassigned.add(v)
        return False

    if dfs():
        print("YES")
        print(' '.join(str(c+1) for c in color))
    else:
        print("NO")

if __name__ == "__main__":
    solve()