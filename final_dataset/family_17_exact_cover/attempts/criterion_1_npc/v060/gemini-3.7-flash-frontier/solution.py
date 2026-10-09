import sys

# Increase recursion depth just in case
sys.setrecursionlimit(2000)

def solve():
    input_data = sys.stdin.read().split()
    if not input_data:
        return
    
    q = int(input_data[0])
    t = int(input_data[1])
    
    n = 3 * q
    triples = []
    idx = 2
    for _ in range(t):
        a = int(input_data[idx]) - 1
        b = int(input_data[idx+1]) - 1
        c = int(input_data[idx+2]) - 1
        idx += 3
        triples.append((a, b, c))
    
    # Elements are 0 to n-1
    # Col to rows
    col_rows = [set() for _ in range(n)]
    for r, (a, b, c) in enumerate(triples):
        col_rows[a].add(r)
        col_rows[b].add(r)
        col_rows[c].add(r)
        
    active_cols = set(range(n))
    active_rows = [True] * t
    solution = []
    
    def search():
        if not active_cols:
            return True
        
        # Unit propagation loop
        forced_stack = []
        contradiction = False
        
        while True:
            # Find min degree column
            min_deg = float('inf')
            min_col = -1
            
            for c in active_cols:
                deg = 0
                for r in col_rows[c]:
                    if active_rows[r]:
                        deg += 1
                if deg < min_deg:
                    min_deg = deg
                    min_col = c
                    if min_deg <= 1:
                        break
            
            if min_deg == 0:
                contradiction = True
                break
            
            if min_deg == 1:
                # Force this row
                # Find the single row
                chosen_r = -1
                for r in col_rows[min_col]:
                    if active_rows[r]:
                        chosen_r = r
                        break
                
                # Apply chosen_r
                solution.append(chosen_r)
                removed_cols = []
                removed_rows = []
                
                a, b, c = triples[chosen_r]
                for col in (a, b, c):
                    if col in active_cols:
                        active_cols.remove(col)
                        removed_cols.append(col)
                        for r in col_rows[col]:
                            if active_rows[r]:
                                active_rows[r] = False
                                removed_rows.append(r)
                                
                forced_stack.append((chosen_r, removed_cols, removed_rows))
                if not active_cols:
                    return True
            else:
                break
                
        if not contradiction:
            # min_col is the branching column
            # Find all active rows in min_col
            candidates = [r for r in col_rows[min_col] if active_rows[r]]
            
            for r in candidates:
                solution.append(r)
                removed_cols = []
                removed_rows = []
                
                a, b, c = triples[r]
                for col in (a, b, c):
                    if col in active_cols:
                        active_cols.remove(col)
                        removed_cols.append(col)
                        for r2 in col_rows[col]:
                            if active_rows[r2]:
                                active_rows[r2] = False
                                removed_rows.append(r2)
                                
                if search():
                    return True
                    
                # Backtrack
                for r2 in removed_rows:
                    active_rows[r2] = True
                for col in removed_cols:
                    active_cols.add(col)
                solution.pop()
        
        # Undo all forced choices
        while forced_stack:
            chosen_r, removed_cols, removed_rows = forced_stack.pop()
            for r2 in removed_rows:
                active_rows[r2] = True
            for col in removed_cols:
                active_cols.add(col)
            solution.pop()
            
        return False

    if search():
        print("YES")
        out = []
        for r in solution:
            a, b, c = triples[r]
            out.append(f"{a+1} {b+1} {c+1}")
        print("\n".join(out))
    else:
        print("NO")

if __name__ == '__main__':
    solve()