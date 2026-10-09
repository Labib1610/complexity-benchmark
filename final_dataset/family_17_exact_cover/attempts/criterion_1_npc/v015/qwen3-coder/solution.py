from collections import defaultdict
import sys

def main():
    import sys
    input = sys.stdin.read
    data = input().split()
    
    q = int(data[0])
    t = int(data[1])
    
    index = 2
    cells = []
    for _ in range(t):
        a = int(data[index])
        b = int(data[index+1])
        c = int(data[index+2])
        cells.append((a, b, c))
        index += 3
    
    # We need to find a matching that covers all 3q nodes
    # This is a exact cover problem, can be modeled as finding a perfect matching in a hypergraph
    # Since q <= 200, and t <= 20000, we can try backtracking with pruning
    
    # Build a graph: for each operator, keep track of which cells contain it
    operator_to_cells = defaultdict(list)
    for i, (a, b, c) in enumerate(cells):
        operator_to_cells[a].append(i)
        operator_to_cells[b].append(i)
        operator_to_cells[c].append(i)
    
    # Try to find a matching of exactly q cells that covers all 3q operators
    used_cells = [False] * t
    selected_cells = []
    covered_operators = set()
    
    def backtrack(cell_index):
        if len(selected_cells) == q:
            return len(covered_operators) == 3 * q
        
        if cell_index >= t:
            return False
            
        # Pruning: if even if we select all remaining cells, we won't have enough
        if len(selected_cells) + (t - cell_index) < q:
            return False
            
        # Try not taking this cell
        if backtrack(cell_index + 1):
            return True
            
        # Try taking this cell if it doesn't conflict
        cell = cells[cell_index]
        a, b, c = cell
        if a not in covered_operators and b not in covered_operators and c not in covered_operators:
            # Take this cell
            selected_cells.append(cell_index)
            covered_operators.add(a)
            covered_operators.add(b)
            covered_operators.add(c)
            used_cells[cell_index] = True
            
            if backtrack(cell_index + 1):
                return True
                
            # Backtrack
            selected_cells.pop()
            covered_operators.discard(a)
            covered_operators.discard(b)
            covered_operators.discard(c)
            used_cells[cell_index] = False
            
        return False
    
    # Sort cells by the minimum operator number to improve pruning
    # But actually, let's just try a different approach due to complexity
    
    # Let's model this as a maximum matching problem
    # Use a greedy approach with backtracking
    
    # Alternative: since q<=200, we can try a recursive backtracking with memoization
    # But let's implement a cleaner version
    
    # Greedy then backtrack might work
    
    def solve():
        # Try a greedy selection first to get a baseline
        # But for correctness, let's do backtracking properly
        
        # For small inputs, pure backtracking should work
        # To make it faster, we can prune branches
        
        # Let's represent state: current cell index, selected cells so far, covered operators
        # But with q up to 200, recursion depth will be high
        
        # Instead, let's think of this as a exact cover problem and use DLX (Dancing Links)
        # But that's overkill here
        
        # Let's proceed with backtracking but optimize:
        # 1. Order cells by how "rare" their elements are (operators that appear in fewer cells first)
        # 2. Prune when impossible
        
        # Compute frequency of each operator
        op_freq = defaultdict(int)
        for cell in cells:
            for op in cell:
                op_freq[op] += 1
                
        # Sort cells based on sum of frequencies (lower is better - more rare operators)
        cell_indices = list(range(t))
        cell_indices.sort(key=lambda i: sum(op_freq[op] for op in cells[i]))
        
        selected = []
        covered = set()
        
        def bt(idx):
            if len(selected) == q:
                return len(covered) == 3 * q
                
            if idx == t:
                return False
                
            # Pruning
            if len(selected) + (t - idx) < q:
                return False
                
            # Try not selecting current cell
            if bt(idx + 1):
                return True
                
            # Try selecting current cell
            cell_idx = cell_indices[idx]
            a, b, c = cells[cell_idx]
            if a not in covered and b not in covered and c not in covered:
                selected.append(cell_idx)
                covered.add(a)
                covered.add(b)
                covered.add(c)
                
                if bt(idx + 1):
                    return True
                    
                selected.pop()
                covered.discard(a)
                covered.discard(b)
                covered.discard(c)
                
            return False
            
        if bt(0):
            print("YES")
            for idx in selected:
                a, b, c = cells[idx]
                print(a, b, c)
            return True
        else:
            print("NO")
            return False
    
    solve()

if __name__ == "__main__":
    main()