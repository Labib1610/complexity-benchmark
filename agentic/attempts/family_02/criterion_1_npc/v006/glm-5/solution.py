import sys

def solve():
    data = sys.stdin.read().strip().split()
    if not data:
        return
    it = iter(data)
    n = int(next(it))
    m = int(next(it))
    clauses = []
    for _ in range(m):
        l1 = int(next(it))
        l2 = int(next(it))
        l3 = int(next(it))
        clauses.append((l1, l2, l3))

    # Branching factor 2 at each step
    assign = [-1] * (n + 1)
    ans_assign = [0] * (n + 1)

    def check_clauses():
        for c in clauses:
            ok = False
            for cond in c:
                idx = abs(cond)
                req = 1 if cond > 0 else 0
                if assign[idx] != -1 and assign[idx] == req:
                    ok = True
                    break
            if not ok:
                # all three are assigned and none satisfied -> instant fail
                for cond in c:
                    if assign[abs(cond)] == -1:
                        break
                else:
                    return False
        return True

    def dfs(step):
        if step == n + 1:
            return True
        for val in [0, 1]:
            assign[step] = val
            if check_clauses():
                if dfs(step + 1):
                    ans_assign[step] = val
                    return True
            assign[step] = -1
        return False

    if dfs(1):
        print("YES")
        print(" ".join(str(ans_assign[i]) for i in range(1, n + 1)))
    else:
        print("NO")

solve()