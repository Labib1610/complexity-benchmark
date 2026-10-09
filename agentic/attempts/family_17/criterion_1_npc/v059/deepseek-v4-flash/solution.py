import sys
sys.setrecursionlimit(1000000)

def solve():
    input = sys.stdin.readline
    q, t = map(int, input().split())
    formulas = []
    for _ in range(t):
        a, b, c = map(int, input().split())
        formulas.append((a-1, b-1, c-1))  # 0-indexed

    n = 3 * q
    # Build mapping from material to list of formula indices
    material_to_formulas = [[] for _ in range(n)]
    for idx, (a, b, c) in enumerate(formulas):
        material_to_formulas[a].append(idx)
        material_to_formulas[b].append(idx)
        material_to_formulas[c].append(idx)

    # Algorithm X exact cover
    # We'll use a simple recursive approach with column selection
    # State: remaining materials set, remaining formulas list
    # But we need to be efficient.

    # We'll use a boolean array for used materials and used formulas
    used_material = [False] * n
    used_formula = [False] * t
    selected = []

    # Precompute formula materials as list
    formula_mats = formulas

    # For pruning: count how many materials each formula covers that are still unused
    # We'll implement recursive search with heuristic: choose material with fewest available formulas

    def backtrack(remaining_count):
        if remaining_count == 0:
            return True
        # Find material with fewest available formulas
        best_mat = -1
        best_count = 10**9
        for mat in range(n):
            if not used_material[mat]:
                cnt = 0
                for fidx in material_to_formulas[mat]:
                    if not used_formula[fidx]:
                        cnt += 1
                if cnt < best_count:
                    best_count = cnt
                    best_mat = mat
                    if cnt == 0:
                        break
        if best_count == 0:
            return False
        # Try each formula for this material
        for fidx in material_to_formulas[best_mat]:
            if used_formula[fidx]:
                continue
            a, b, c = formula_mats[fidx]
            if used_material[a] or used_material[b] or used_material[c]:
                continue
            # Choose this formula
            used_formula[fidx] = True
            used_material[a] = used_material[b] = used_material[c] = True
            selected.append(fidx)
            if backtrack(remaining_count - 1):
                return True
            # Backtrack
            selected.pop()
            used_material[a] = used_material[b] = used_material[c] = False
            used_formula[fidx] = False
        return False

    if backtrack(q):
        print("YES")
        for fidx in selected:
            a, b, c = formula_mats[fidx]
            print(a+1, b+1, c+1)
    else:
        print("NO")

if __name__ == "__main__":
    solve()