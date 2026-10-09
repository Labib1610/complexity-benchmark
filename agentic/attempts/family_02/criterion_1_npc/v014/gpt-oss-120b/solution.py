import sys

sys.setrecursionlimit(10000)

def solve() -> None:
    data = sys.stdin.read().strip().split()
    if not data:
        return
    it = iter(data)
    n = int(next(it))
    m = int(next(it))
    clauses = []
    for _ in range(m):
        lits = [int(next(it)) for _ in range(3)]
        clauses.append(lits)

    # assignment: -1 unassigned, 0 false (CLOSED), 1 true (OPEN)
    def dpll(assign):
        # unit propagation and pure literal elimination
        while True:
            changed = False
            # unit clauses
            for clause in clauses:
                sat = False
                unassigned = None
                uncnt = 0
                for lit in clause:
                    var = abs(lit)
                    val = assign[var]
                    if val == -1:
                        uncnt += 1
                        unassigned = lit
                    else:
                        if (val == 1 and lit > 0) or (val == 0 and lit < 0):
                            sat = True
                            break
                if sat:
                    continue
                if uncnt == 0:          # clause unsatisfied
                    return False
                if uncnt == 1:          # unit clause
                    var = abs(unassigned)
                    needed = 1 if unassigned > 0 else 0
                    if assign[var] == -1:
                        assign[var] = needed
                        changed = True
                    elif assign[var] != needed:
                        return False
            if changed:
                continue

            # pure literals
            pos = [0]*(n+1)
            neg = [0]*(n+1)
            for clause in clauses:
                clause_sat = False
                for lit in clause:
                    var = abs(lit)
                    val = assign[var]
                    if val != -1:
                        if (val == 1 and lit > 0) or (val == 0 and lit < 0):
                            clause_sat = True
                            break
                if clause_sat:
                    continue
                for lit in clause:
                    var = abs(lit)
                    if assign[var] != -1:
                        continue
                    if lit > 0:
                        pos[var] = 1
                    else:
                        neg[var] = 1
            pure_found = False
            for v in range(1, n+1):
                if assign[v] == -1:
                    if pos[v] and not neg[v]:
                        assign[v] = 1
                        pure_found = True
                    elif neg[v] and not pos[v]:
                        assign[v] = 0
                        pure_found = True
            if pure_found:
                continue
            break

        # check if all clauses satisfied
        all_sat = True
        for clause in clauses:
            clause_sat = False
            for lit in clause:
                var = abs(lit)
                val = assign[var]
                if val != -1 and ((val == 1 and lit > 0) or (val == 0 and lit < 0)):
                    clause_sat = True
                    break
            if not clause_sat:
                all_sat = False
                break
        if all_sat:
            return True

        # choose unassigned variable
        for v in range(1, n+1):
            if assign[v] == -1:
                var = v
                break
        # try true then false
        for val in (1, 0):
            new_assign = assign[:]
            new_assign[var] = val
            if dpll(new_assign):
                assign[:] = new_assign
                return True
        return False

    assign = [-1]*(n+1)
    if dpll(assign):
        print("YES")
        print(' '.join(str(assign[i]) for i in range(1, n+1)))
    else:
        print("NO")

if __name__ == "__main__":
    solve()