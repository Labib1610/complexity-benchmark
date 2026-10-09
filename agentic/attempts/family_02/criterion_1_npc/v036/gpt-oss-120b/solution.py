import sys, random

def solve() -> None:
    data = sys.stdin.read().strip().split()
    if not data:
        return
    it = iter(data)
    n = int(next(it))
    m = int(next(it))
    clauses = []
    for _ in range(m):
        a = int(next(it))
        b = int(next(it))
        c = int(next(it))
        clauses.append((a, b, c))

    # helper: evaluate a literal under assignment arr (0/1)
    def lit_val(lit, arr):
        var = abs(lit) - 1
        val = arr[var]
        return val if lit > 0 else 1 - val

    # check if all clauses satisfied
    def all_sat(arr):
        for a, b, c in clauses:
            if not (lit_val(a, arr) or lit_val(b, arr) or lit_val(c, arr)):
                return False
        return True

    R = 30                     # number of restarts
    max_steps = 3 * n
    for _ in range(R):
        # random start
        assign = [random.getrandbits(1) for _ in range(n)]
        for step in range(max_steps):
            # find an unsatisfied clause
            unsat = None
            for cl in clauses:
                a, b, c = cl
                if not (lit_val(a, assign) or lit_val(b, assign) or lit_val(c, assign)):
                    unsat = cl
                    break
            if unsat is None:          # all satisfied
                print("YES")
                print(' '.join(str(v) for v in assign))
                return
            # flip a random literal of the unsatisfied clause
            lit = random.choice(unsat)
            var = abs(lit) - 1
            assign[var] ^= 1
    # no satisfying assignment found
    print("NO")

if __name__ == "__main__":
    solve()