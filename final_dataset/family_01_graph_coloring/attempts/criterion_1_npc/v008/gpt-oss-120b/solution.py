import sys

sys.setrecursionlimit(10000)

def solve() -> None:
    data = sys.stdin.read().strip().split()
    if not data:
        return
    it = iter(data)
    n = int(next(it))
    m = int(next(it))
    adj = [[] for _ in range(n)]
    for _ in range(m):
        u = int(next(it)) - 1
        v = int(next(it)) - 1
        adj[u].append(v)
        adj[v].append(u)

    assigned = [-1] * n               # -1 = unassigned, else 0/1/2
    domain = [0b111] * n              # bits for possible colors

    # depth‑first search with MRV heuristic
    def dfs(assigned_cnt: int) -> bool:
        if assigned_cnt == n:
            return True

        # choose vertex with smallest domain (MRV)
        v = -1
        min_sz = 4
        for i in range(n):
            if assigned[i] == -1:
                sz = domain[i].bit_count()
                if sz < min_sz:
                    min_sz = sz
                    v = i
                    if sz == 1:
                        break
        if min_sz == 0:          # dead end
            return False

        bits = domain[v]
        for c in range(3):       # try each possible color
            if bits & (1 << c):
                assigned[v] = c
                changed = []
                fail = False
                for nb in adj[v]:
                    if assigned[nb] == -1 and (domain[nb] & (1 << c)):
                        domain[nb] &= ~(1 << c)
                        changed.append(nb)
                        if domain[nb] == 0:
                            fail = True
                            break
                if not fail:
                    if dfs(assigned_cnt + 1):
                        return True
                # revert changes
                for nb in changed:
                    domain[nb] |= (1 << c)
                assigned[v] = -1
        return False

    possible = dfs(0)

    out = []
    if not possible:
        out.append("NO")
    else:
        out.append("YES")
        out.append(' '.join(str(c + 1) for c in assigned))
    sys.stdout.write('\n'.join(out))

if __name__ == "__main__":
    solve()