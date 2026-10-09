import sys
sys.setrecursionlimit(10000)

def solve():
    input_data = sys.stdin.read().strip().split()
    if not input_data:
        return
    it = iter(input_data)
    n = int(next(it))
    m = int(next(it))
    clauses = []
    for _ in range(m):
        p1 = int(next(it))
        p2 = int(next(it))
        p3 = int(next(it))
        # Convert to 0-indexed variable: positive -> var, negative -> ~var
        # Use int for literal: positive var number = index+1, negative = -(index+1)
        clauses.append([p1, p2, p3])
    
    assignment = [None] * n  # None = unassigned, True=1, False=0
    
    # Watch lists
    watch = [[] for _ in range(n)]
    for idx, cl in enumerate(clauses):
        for lit in cl:
            var = abs(lit) - 1
            watch[var].append((idx, lit))
    
    # state of each clause: how many literals are false, first two unassigned etc.
    # We'll implement recursive search with unit propagation.
    
    def propagate(assign):
        # returns (conflict, queue)
        queue = []
        # Check clauses for unit/conflict
        for i, cl in enumerate(clauses):
            sat = False
            unassigned = []
            false_count = 0
            for lit in cl:
                var = abs(lit) - 1
                val = assign[var]
                if val is None:
                    unassigned.append(lit)
                else:
                    if (lit > 0 and val) or (lit < 0 and not val):
                        sat = True
                        break
                    else:
                        false_count += 1
            if sat:
                continue
            if not unassigned:
                return False, []  # conflict
            if len(unassigned) == 1:
                # unit clause: must satisfy
                lit = unassigned[0]
                var = abs(lit) - 1
                val = (lit > 0)
                if assign[var] is not None:
                    if assign[var] != val:
                        return False, []
                else:
                    assign[var] = val
                    queue.append(var)
        return True, queue
    
    # We'll do recursive search with decision on unassigned var
    
    def dfs(assign):
        conflict, _ = propagate(assign)
        if conflict:
            return None
        # find first unassigned
        unassigned_vars = [i for i in range(n) if assign[i] is None]
        if not unassigned_vars:
            return assign
        var = unassigned_vars[0]
        # Try both values
        for val in [True, False]:
            assign[var] = val
            res = dfs(assign)
            if res is not None:
                return res
            assign[var] = None
        return None
    
    result = dfs(assignment)
    if result is None:
        print("NO")
    else:
        print("YES")
        print(' '.join('1' if result[i] else '0' for i in range(n)))

if __name__ == "__main__":
    solve()