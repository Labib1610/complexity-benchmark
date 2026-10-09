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
    edges = []
    for _ in range(m):
        u = int(next(it)) - 1
        v = int(next(it)) - 1
        adj[u] |= 1 << v
        adj[v] |= 1 << u
        edges.append((u, v))

    # possible colors bitmask: bit 0->color1,1->color2,2->color3
    ALL = 0b111
    domains = [ALL] * n
    assignment = [-1] * n

    # order vertices by degree descending for initial heuristic
    order = sorted(range(n), key=lambda x: bin(adj[x]).count('1'), reverse=True)

    # map from position in order to vertex
    pos2v = order

    # helper to pick unassigned vertex with smallest domain
    def select_vertex():
        best = -1
        best_sz = 4
        for v in range(n):
            if assignment[v] == -1:
                sz = bin(domains[v]).count('1')
                if sz < best_sz:
                    best_sz = sz
                    best = v
                    if sz == 1:
                        break
        return best

    # recursive search
    def dfs(assigned_cnt: int) -> bool:
        if assigned_cnt == n:
            return True
        v = select_vertex()
        d = domains[v]
        # try each possible color
        for c in range(3):
            if d & (1 << c):
                # assign color c to v
                assignment[v] = c
                # record changes to revert
                changed = []
                ok = True
                # remove color c from neighbors' domains
                nb = adj[v]
                while nb:
                    u = (nb & -nb).bit_length() - 1
                    nb &= nb - 1
                    if assignment[u] == -1:
                        if domains[u] & (1 << c):
                            new_dom = domains[u] & ~(1 << c)
                            if new_dom == 0:
                                ok = False
                                # no need to continue updating
                                # but still need to record for revert? not necessary
                                break
                            changed.append((u, domains[u]))
                            domains[u] = new_dom
                if ok and dfs(assigned_cnt + 1):
                    return True
                # revert
                for u, old in reversed(changed):
                    domains[u] = old
                assignment[v] = -1
        return False

    possible = dfs(0)
    if not possible:
        print("NO")
    else:
        print("YES")
        # convert 0/1/2 to 1/2/3
        print(' '.join(str(c+1) for c in assignment))

if __name__ == "__main__":
    solve()