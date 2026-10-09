from itertools import product

def solve():
    n, m = map(int, input().split())
    
    # Read all edges
    edges = []
    for _ in range(m):
        u, v = map(int, input().split())
        edges.append((u-1, v-1))  # Convert to 0-indexed
    
    # Check all possible assignments
    for assignment in product([1, 2, 3], repeat=n):
        valid = True
        for u, v in edges:
            cu, cv = assignment[u], assignment[v]
            sum_ids = cu + cv
            sum_squares = cu*cu + cv*cv
            if sum_squares % sum_ids == 0:
                valid = False
                break
        
        if valid:
            print("YES")
            print(' '.join(map(str, assignment)))
            return
    
    print("NO")

solve()