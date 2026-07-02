import sys

def solve():
    data = sys.stdin.buffer.read().split()
    idx = 0
    n, m = int(data[idx]), int(data[idx + 1]); idx += 2
    clauses = []
    for _ in range(m):
        a, b, c = int(data[idx]), int(data[idx + 1]), int(data[idx + 2]); idx += 3
        clauses.append((a, b, c))

    assign = [None] * (n + 1)  # assign[i] in {0, 1} or None

    def lit_val(l):
        v = assign[abs(l)]
        if v is None:
            return None
        return v if l > 0 else 1 - v

    def clause_status(clause):
        has_unknown = False
        for l in clause:
            v = lit_val(l)
            if v == 1:
                return 1   # satisfied
            if v is None:
                has_unknown = True
        return None if has_unknown else 0  # 0 = falsified

    def backtrack(var):
        if var > n:
            return all(clause_status(c) == 1 for c in clauses)
        for val in (0, 1):
            assign[var] = val
            if not any(clause_status(c) == 0 for c in clauses):
                if backtrack(var + 1):
                    return True
            assign[var] = None
        return False

    if backtrack(1):
        print("YES")
        print(*[assign[i] for i in range(1, n + 1)])
    else:
        print("NO")

solve()
