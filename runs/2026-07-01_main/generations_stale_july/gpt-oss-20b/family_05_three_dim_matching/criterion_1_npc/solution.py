import sys
import threading

def solve():
    import sys

    sys.setrecursionlimit(10000)
    data = sys.stdin.read().strip().split()
    if not data:
        return
    it = iter(data)
    k = int(next(it))
    t = int(next(it))
    triples = []
    for _ in range(t):
        x = int(next(it)) - 1
        y = int(next(it)) - 1
        z = int(next(it)) - 1
        triples.append((x, y, z))

    n_cols = 3 * k
    all_mask = (1 << n_cols) - 1

    # Map columns: X_i -> i, Y_j -> k+j, Z_k -> 2k+k
    row_masks = []
    for (x, y, z) in triples:
        mask = (1 << x) | (1 << (k + y)) | (1 << (2 * k + z))
        row_masks.append(mask)

    # For each column, list of rows covering it
    col_rows = [[] for _ in range(n_cols)]
    for idx, mask in enumerate(row_masks):
        # iterate bits set
        m = mask
        while m:
            lsb = m & -m
            col = (lsb.bit_length() - 1)
            col_rows[col].append(idx)
            m -= lsb

    # Precompute column order by size (static)
    col_order = sorted(range(n_cols), key=lambda c: len(col_rows[c]))

    solution = []
    found = False

    def dfs(used_mask, depth):
        nonlocal found
        if found:
            return
        if used_mask == all_mask:
            found = True
            return
        # choose next column: first unused in col_order
        for col in col_order:
            if not (used_mask >> col) & 1:
                break
        else:
            return  # should not happen
        for row in col_rows[col]:
            mask = row_masks[row]
            if mask & used_mask:
                continue
            solution.append(row)
            dfs(used_mask | mask, depth + 1)
            if found:
                return
            solution.pop()

    dfs(0, 0)

    out = []
    if not found:
        out.append("NO")
    else:
        out.append("YES")
        for row in solution:
            x, y, z = triples[row]
            out.append(f"{x+1} {y+1} {z+1}")
    sys.stdout.write("\n".join(out))

def main():
    solve()

threading.Thread(target=main).start()