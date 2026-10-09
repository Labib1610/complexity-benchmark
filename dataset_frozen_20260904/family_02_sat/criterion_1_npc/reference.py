import sys


def main():
    data = sys.stdin.buffer.read().split()
    idx = 0
    n = int(data[idx]); m = int(data[idx + 1]); idx += 2
    clauses = []
    var_cl = [[] for _ in range(n + 1)]
    for ci in range(m):
        a = int(data[idx]); b = int(data[idx + 1]); c = int(data[idx + 2]); idx += 3
        cl = (a, b, c)
        clauses.append(cl)
        for l in cl:
            var_cl[abs(l)].append(ci)

    assign = [None] * (n + 1)          # None / 0 / 1
    sys.setrecursionlimit(1 << 20)

    def lit_val(l):
        v = assign[abs(l)]
        if v is None:
            return None
        return (v == 1) if l > 0 else (v == 0)

    def bcp(seed_vars):
        """Boolean constraint propagation from newly assigned vars. Returns (ok, forced_list)."""
        forced = []
        queue = list(seed_vars)
        while queue:
            var = queue.pop()
            for ci in var_cl[var]:
                unassigned = None
                cnt = 0
                sat = False
                for l in clauses[ci]:
                    tv = lit_val(l)
                    if tv is True:
                        sat = True; break
                    if tv is None:
                        cnt += 1; unassigned = l
                if sat:
                    continue
                if cnt == 0:                       # conflict
                    for v in forced:
                        assign[v] = None
                    return False, None
                if cnt == 1:                       # unit -> force
                    av = abs(unassigned)
                    assign[av] = 1 if unassigned > 0 else 0
                    forced.append(av); queue.append(av)
        return True, forced

    def dpll():
        v = 1
        while v <= n and assign[v] is not None:
            v += 1
        if v > n:
            return True
        for val in (1, 0):                         # any satisfying assignment (branch true first)
            assign[v] = val
            ok, forced = bcp([v])
            if ok and dpll():
                return True
            if forced:
                for u in forced:
                    assign[u] = None
            assign[v] = None
        return False

    if dpll():
        sys.stdout.write("YES\n")
        sys.stdout.write(" ".join(str(assign[i] if assign[i] is not None else 0)
                                  for i in range(1, n + 1)) + "\n")
    else:
        sys.stdout.write("NO\n")


main()
