import sys
from collections import defaultdict

def main():
    import sys
    input = sys.stdin.read
    data = input().split()
    
    q = int(data[0])
    t = int(data[1])
    
    if t == 0:
        if q == 0:
            print("YES")
        else:
            print("NO")
        return
    
    index = 2
    cells = []
    for _ in range(t):
        a = int(data[index])
        b = int(data[index+1])
        c = int(data[index+2])
        cells.append((a, b, c))
        index += 3
    
    # We need to find a matching that covers all nodes from 1 to 3*q
    # This is a exact cover problem, we can model it as finding a perfect matching in a hypergraph
    # But since each cell covers exactly 3 nodes and we need to cover 3*q nodes with q cells,
    # it's equivalent to finding a partition of the set {1, ..., 3*q} into q triplets from the given list
    
    # We'll use backtracking with pruning
    # Let's sort the cells for better pruning
    cells.sort()
    
    # Build adjacency for each node
    adj = defaultdict(list)
    for i, (a, b, c) in enumerate(cells):
        adj[a].append(i)
        adj[b].append(i)
        adj[c].append(i)
    
    selected = [False] * t
    result = []
    used = [False] * (3*q + 1)
    
    def backtrack(pos):
        if pos == q:
            return True
            
        # Find the smallest unused operator
        start_op = -1
        for op in range(1, 3*q + 1):
            if not used[op]:
                start_op = op
                break
        
        # Try all cells containing start_op
        for cell_idx in adj[start_op]:
            if selected[cell_idx]:
                continue
            a, b, c = cells[cell_idx]
            if used[a] or used[b] or used[c]:
                continue
                
            # Select this cell
            selected[cell_idx] = True
            used[a] = used[b] = used[c] = True
            result.append((a, b, c))
            
            if backtrack(pos + 1):
                return True
                
            # Backtrack
            selected[cell_idx] = False
            used[a] = used[b] = used[c] = False
            result.pop()
        
        return False
    
    if backtrack(0):
        print("YES")
        for cell in result:
            print(cell[0], cell[1], cell[2])
    else:
        print("NO")

if __name__ == "__main__":
    main()