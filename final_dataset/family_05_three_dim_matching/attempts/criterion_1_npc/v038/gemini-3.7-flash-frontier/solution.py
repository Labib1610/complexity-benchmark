import sys

# Increase recursion depth just in case
sys.setrecursionlimit(2000)

def solve():
    input_data = sys.stdin.read().split()
    if not input_data:
        return
    
    k = int(input_data[0])
    t = int(input_data[1])
    
    triplets = []
    idx = 2
    for _ in range(t):
        a = int(input_data[idx])
        b = int(input_data[idx+1])
        c = int(input_data[idx+2])
        idx += 3
        triplets.append((a, b, c))
    
    num_cols = 3 * k
    num_rows = t
    
    row_cols = [None] * num_rows
    col_rows = [[] for _ in range(num_cols)]
    
    for r in range(num_rows):
        a, b, c = triplets[r]
        c1 = a - 1
        c2 = k + b - 1
        c3 = 2 * k + c - 1
        row_cols[r] = (c1, c2, c3)
        col_rows[c1].append(r)
        col_rows[c2].append(r)
        col_rows[c3].append(r)
        
    col_count = [len(col_rows[c]) for c in range(num_cols)]
    row_conflict_count = [0] * num_rows
    uncovered_cols = list(range(num_cols))
    
    ans = []
    
    def search():
        if not uncovered_cols:
            return True
        
        # Choose column with minimum remaining rows (MRV)
        best_col = uncovered_cols[0]
        min_c = col_count[best_col]
        
        for c in uncovered_cols:
            cnt = col_count[c]
            if cnt < min_c:
                min_c = cnt
                best_col = c
                if min_c == 0:
                    break
        
        if min_c == 0:
            return False
        
        for r in col_rows[best_col]:
            if row_conflict_count[r] == 0:
                ans.append(r)
                
                cols_to_remove = row_cols[r]
                for c in cols_to_remove:
                    uncovered_cols.remove(c)
                    for r_prime in col_rows[c]:
                        row_conflict_count[r_prime] += 1
                        if row_conflict_count[r_prime] == 1:
                            c1, c2, c3 = row_cols[r_prime]
                            col_count[c1] -= 1
                            col_count[c2] -= 1
                            col_count[c3] -= 1
                
                if search():
                    return True
                
                # Backtrack
                for c in reversed(cols_to_remove):
                    uncovered_cols.append(c)
                    for r_prime in col_rows[c]:
                        if row_conflict_count[r_prime] == 1:
                            c1, c2, c3 = row_cols[r_prime]
                            col_count[c1] += 1
                            col_count[c2] += 1
                            col_count[c3] += 1
                        row_conflict_count[r_prime] -= 1
                
                ans.pop()
                
        return False

    if search():
        out = ["YES"]
        for r in ans:
            a, b, c = triplets[r]
            out.append(f"{a} {b} {c}")
        print("\n".join(out))
    else:
        print("NO")

if __name__ == '__main__':
    solve()