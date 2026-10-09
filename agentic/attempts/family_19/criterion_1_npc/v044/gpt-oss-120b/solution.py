import sys
sys.setrecursionlimit(10000)

def solve() -> None:
    data = sys.stdin.read().strip().split()
    if not data:
        return
    it = iter(map(int, data))
    n = next(it); m = next(it); k = next(it)

    S = []; T = []; D = []
    for _ in range(k):
        s = next(it)-1; t = next(it)-1; d = next(it)
        S.append(s); T.append(t); D.append(d)

    U = []; V = []; C = []
    for _ in range(m):
        u = next(it)-1; v = next(it)-1; cap = next(it)
        U.append(u); V.append(v); C.append(cap)

    # balances[g][v]
    bal = [[0]*n for _ in range(k)]
    # answer[g][e]
    ans = [[0]*m for _ in range(k)]

    total_demand = sum(D)

    # pre‑compute for pruning: max possible absolute balance for a group
    max_bal = total_demand

    # generate all possible k‑tuples for a given capacity
    from itertools import product

    # cache tuples per capacity
    tuples_cache = {}
    def get_tuples(cap):
        if cap not in tuples_cache:
            lst = []
            # generate all k‑tuples with sum <= cap
            for tup in product(range(cap+1), repeat=k):
                if sum(tup) <= cap:
                    lst.append(tup)
            tuples_cache[cap] = lst
        return tuples_cache[cap]

    found = False

    def dfs(e_idx):
        nonlocal found
        if found:
            return
        if e_idx == m:
            # check final balances
            for g in range(k):
                for v in range(n):
                    need = 0
                    if v == S[g]:
                        need = D[g]
                    elif v == T[g]:
                        need = -D[g]
                    if bal[g][v] != need:
                        return
            # success
            found = True
            return

        cap = C[e_idx]
        u = U[e_idx]; v = V[e_idx]
        for tup in get_tuples(cap):
            # quick prune: if any balance would exceed max_bal, skip
            ok = True
            for g, x in enumerate(tup):
                if x:
                    nb_u = bal[g][u] + x
                    nb_v = bal[g][v] - x
                    if abs(nb_u) > max_bal or abs(nb_v) > max_bal:
                        ok = False
                        break
            if not ok:
                continue

            # apply
            for g, x in enumerate(tup):
                if x:
                    bal[g][u] += x
                    bal[g][v] -= x
                    ans[g][e_idx] = x
            dfs(e_idx+1)
            if found:
                return
            # revert
            for g, x in enumerate(tup):
                if x:
                    bal[g][u] -= x
                    bal[g][v] += x
                    ans[g][e_idx] = 0

    dfs(0)

    out = []
    if not found:
        out.append("NO")
    else:
        out.append("YES")
        for g in range(k):
            out.append(" ".join(str(ans[g][e]) for e in range(m)))
    sys.stdout.write("\n".join(out))

if __name__ == "__main__":
    solve()