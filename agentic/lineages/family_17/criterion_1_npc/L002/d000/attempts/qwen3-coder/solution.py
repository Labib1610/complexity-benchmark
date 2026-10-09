from itertools import combinations

def solve():
    q, t = map(int, input().split())
    cells = []
    for _ in range(t):
        a, b, c = map(int, input().split())
        cells.append((a, b, c))
    
    # Try all combinations of q cells from the available cells
    for selected_cells in combinations(cells, q):
        # Create a set of all operators in the selected cells
        operators = set()
        for cell in selected_cells:
            operators.update(cell)
        
        # Check if we have exactly 3*q distinct operators
        if len(operators) == 3 * q:
            # Check if we have exactly the operators 1 through 3*q
            if operators == set(range(1, 3*q + 1)):
                print("YES")
                for cell in selected_cells:
                    print(cell[0], cell[1], cell[2])
                return
    
    print("NO")

solve()