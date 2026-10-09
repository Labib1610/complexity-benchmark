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

    # order vertices by degree descending for initial heuristic
    order = sorted(range(n), key=lambda x: -adj[x].bit_count())
    # map from position in order to vertex id and reverse
    pos2v = order
    v2pos = [0] * n
    for i, v in enumerate(pos2v):
        v2pos[v] = i

    # possible colors for each vertex, bits 0,1,2 represent colors 1,2,3
    poss = [0b111] * n
    assign = [0] * n  # 0 means unassigned, else 1..3

    # initial propagation none needed

    # select unassigned vertex with smallest domain
    def select_vertex():
        best = -1
        best_cnt = 4
        for i in range(n):
            if assign[pos2v[i]] == 0:
                cnt = poss[i].bit_count()
                if cnt < best_cnt:
                    best_cnt = cnt
                    best = i
                    if cnt == 1:
                        break
        return best

    def dfs(assigned_cnt: int) -> bool:
        if assigned_cnt == n:
            return True
        vpos = select_vertex()
        if vpos == -1:
            return False
        v = pos2v[vpos]
        mask = poss[vpos]
        # try each possible color
        for c in range(3):
            if mask & (1 << c):
                # assign color c+1
                assign[v] = c + 1
                # save state to restore
                changed = []
                ok = True
                # remove this color from neighbors' possibilities
                nb = adj[v]
                while nb:
                    u = (nb & -nb).bit_length() - 1
                    nb &= nb - 1
                    upos = v2pos[u]
                    if assign[u] == 0:
                        if poss[upos] & (1 << c):
                            poss[upos] &= ~(1 << c)
                            changed.append(upos)
                            if poss[upos] == 0:
                                ok = False
                                break
                if ok and dfs(assigned_cnt + 1):
                    return True
                # backtrack
                for upos in changed:
                    poss[upos] |= (1 << c)
                assign[v] = 0
        return False

    if dfs(0):
        print("YES")
        print(' '.join(str(assign[i]) for i in range(n)))
    else:
        print("NO")

if __name__ == "__main__":
    solve()