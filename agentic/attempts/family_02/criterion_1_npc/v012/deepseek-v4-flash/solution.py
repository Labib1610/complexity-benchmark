import sys

def solve():
    input_data = sys.stdin.read().strip().split()
    if not input_data:
        return
    n, m = int(input_data[0]), int(input_data[1])
    clauses = []
    idx = 2
    for _ in range(m):
        a = int(input_data[idx]); b = int(input_data[idx+1]); c = int(input_data[idx+2])
        idx += 3
        clauses.append((a, b, c))
    
    assignment = [None] * (n + 1)  # None = unassigned, True = warm, False = cool
    
    def var_value(lit):
        v = abs(lit)
        if assignment[v] is None:
            return None
        val = assignment[v]
        if lit > 0:
            return val
        else:
            return not val
    
    def propagate():
        changed = True
        while changed:
            changed = False
            for clause in clauses:
                vals = [var_value(l) for l in clause]
                if any(v is True for v in vals):
                    continue
                unassigned = [l for l, v in zip(clause, vals) if v is None]
                if len(unassigned) == 0:
                    return False  # conflict
                if len(unassigned) == 1:
                    lit = unassigned[0]
                    val = lit > 0
                    v = abs(lit)
                    if assignment[v] is not None and assignment[v] != val:
                        return False
                    assignment[v] = val
                    changed = True
        return True
    
    def backtrack():
        if not propagate():
            return False
        # find unassigned variable
        for i in range(1, n+1):
            if assignment[i] is None:
                # try warm
                assignment[i] = True
                if backtrack():
                    return True
                assignment[i] = False
                if backtrack():
                    return True
                assignment[i] = None
                return False
        # all assigned
        return True
    
    if backtrack():
        print("YES")
        print(" ".join('1' if assignment[i] else '0' for i in range(1, n+1)))
    else:
        print("NO")

if __name__ == "__main__":
    solve()