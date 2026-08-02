import sys


def solve():
    data = sys.stdin.buffer.read().split()
    idx = 0
    n, m = int(data[idx]), int(data[idx + 1]); idx += 2
    clauses = []
    for _ in range(m):
        a, b, c = int(data[idx]), int(data[idx + 1]), int(data[idx + 2]); idx += 3
        clauses.append((a, b, c))

    assign = [None] * (n + 1)          # assign[v] in {0, 1} or None
    sys.setrecursionlimit(1 << 20)

    def lit_true(l):
        v = assign[abs(l)]
        if v is None:
            return None
        return (v == 1) if l > 0 else (v == 0)

    # DPLL: decide variables in index order (value 0 before 1 -> lexicographically
    # smallest satisfying assignment), with unit propagation to fixpoint between
    # decisions. Unit propagation only ever forces literals already implied by the
    # current partial assignment (a clause with a single unassigned literal and no
    # satisfied literal), so it never overrides the 0-before-1 preference: it yields
    # exactly the assignment plain index-order backtracking would reach, only faster.
    # This is required to generate ground truth near the m/n ~ 4.26 phase transition,
    # where UNSAT instances force exhaustive refutation.
    def dpll(nextv):
        forced = []                    # literals this node forced via UP, undone on backtrack
        changed = True
        while changed:
            changed = False
            for cl in clauses:
                unassigned = None
                cnt_unassigned = 0
                sat = False
                for l in cl:
                    tv = lit_true(l)
                    if tv is True:
                        sat = True
                        break
                    if tv is None:
                        cnt_unassigned += 1
                        unassigned = l
                if sat:
                    continue
                if cnt_unassigned == 0:         # clause falsified -> conflict
                    for v in forced:
                        assign[v] = None
                    return False
                if cnt_unassigned == 1:         # unit clause -> force its literal
                    assign[abs(unassigned)] = 1 if unassigned > 0 else 0
                    forced.append(abs(unassigned))
                    changed = True

        v = nextv
        while v <= n and assign[v] is not None:
            v += 1
        if v > n:
            return True                        # every variable assigned -> satisfied

        for val in (0, 1):                     # 0 before 1 -> lex-smallest
            assign[v] = val
            if dpll(v + 1):
                return True
            assign[v] = None
        for u in forced:
            assign[u] = None
        return False

    if dpll(1):
        print("YES")
        print(*[assign[i] if assign[i] is not None else 0 for i in range(1, n + 1)])
    else:
        print("NO")


solve()
