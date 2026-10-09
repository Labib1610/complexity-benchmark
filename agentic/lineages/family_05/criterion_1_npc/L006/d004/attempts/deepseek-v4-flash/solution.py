import sys

def solve():
    input = sys.stdin.readline
    k, t = map(int, input().split())
    records = []
    for _ in range(t):
        m, c, f = map(int, input().split())
        records.append((m-1, c-1, f-1))
    
    # Map from (module, row) -> list of columns
    mod_row_col = [[[] for _ in range(k)] for _ in range(k)]
    for m, c, f in records:
        mod_row_col[m][c].append(f)
    
    # Sort columns for deterministic ordering
    for m in range(k):
        for c in range(k):
            mod_row_col[m][c].sort()
    
    # We will assign modules to rows, each row gets a module and a column
    # state: which modules used, which columns used
    used_mod = [False]*k
    used_col = [False]*k
    assignment = [None]*k  # assignment[row] = (module, column)
    
    # Precompute column bitmasks for speed
    col_mask = [1 << f for f in range(k)]
    
    found = False
    result = []
    
    def dfs(row):
        nonlocal found
        if row == k:
            found = True
            return True
        # Try modules not used yet
        for m in range(k):
            if used_mod[m]:
                continue
            # Try columns available for (m, row)
            for f in mod_row_col[m][row]:
                if used_col[f]:
                    continue
                used_mod[m] = True
                used_col[f] = True
                assignment[row] = (m, f)
                if dfs(row+1):
                    return True
                used_mod[m] = False
                used_col[f] = False
        return False
    
    dfs(0)
    
    if not found:
        print("NO")
    else:
        print("YES")
        for row, (m, f) in enumerate(assignment):
            print(m+1, row+1, f+1)

if __name__ == "__main__":
    solve()