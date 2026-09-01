from itertools import product

def compute_interaction(fu, fv):
    diff = fu - fv
    return 2 * (diff ** 4) - 10 * (diff ** 2) + 4

def is_valid_assignment(n, edges, assignment):
    total = 0
    for u, v in edges:
        total += compute_interaction(assignment[u-1], assignment[v-1])
    return total == -4 * len(edges)

def solve():
    import sys
    input_lines = sys.stdin.read().splitlines()
    
    line1 = list(map(int, input_lines[0].split()))
    n, m = line1[0], line1[1]
    
    if m == 0:
        print("YES")
        print(" ".join(["1"] * n))
        return
    
    edges = []
    for i in range(1, m+1):
        u, v = map(int, input_lines[i].split())
        edges.append((u, v))
    
    # Try all possible assignments in lexicographical order
    for assignment in product([1, 2, 3], repeat=n):
        if is_valid_assignment(n, edges, assignment):
            print("YES")
            print(" ".join(map(str, assignment)))
            return
    
    print("NO")

solve()